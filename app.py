import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

#python -m streamlit run app.py --server.enableCORS=false --server.enableXsrfProtection=false
load_dotenv() 
API_KEY = os.getenv("gemini_API_KEY") 
genai.configure(api_key=API_KEY)

llm_model = genai.GenerativeModel('gemini-flash-latest')

# Load Data 
@st.cache_data
def load_data():
    process_path = 'Process_Data'
    raw_path = 'Raw_Data'
    reorder_df = pd.read_csv(os.path.join(process_path, 'reorder_recommendations.csv'))
    mba_rules_df = pd.read_csv(os.path.join(process_path, 'market_basket.csv'))
    orders_df = pd.read_csv(os.path.join(raw_path, 'orders.csv'))
    return reorder_df, mba_rules_df , orders_df

reorder_df, mba_rules_df , orders_df = load_data()

def get_mba_insights(product_a, top_n=3):
    rules = mba_rules_df[mba_rules_df['product_name_A'].str.lower() == product_a.lower()]
    if rules.empty: return None, None
    
    sorted_rules = rules.sort_values(by='lift', ascending=False).head(top_n)
    items_list = [f"{row['product_name_B']}" for _, row in sorted_rules.iterrows()]
    return items_list, sorted_rules

def get_user_insights(user_id_input, top_n=3):
    try: uid = int(user_id_input) 
    except ValueError: return None, None, None, None
    
    # Check if user exists in reorder data
    user_reorder_data = reorder_df[reorder_df['user_id'] == uid]
    if user_reorder_data.empty: return None, None, None, None
    
    # Get Top Reorder Items
    top_items_df = user_reorder_data.sort_values(by='rank').head(top_n)
    items_list = top_items_df['product_name'].tolist()
    
    # 2. Extract Real Time Behavior from orders_df
    user_orders = orders_df[orders_df['user_id'] == uid]
    
    if not user_orders.empty:
        # Find the most frequent day and hour 
        best_dow = user_orders['order_dow'].mode()[0]
        best_hour = user_orders['order_hour_of_day'].mode()[0]
        
        # Map integer to Day name (0 = Sunday in Instacart data)
        days_map = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        fav_day = days_map[int(best_dow)]
        
        # Format Hour to AM/PM
        am_pm = "AM" if best_hour < 12 else "PM"
        display_hour = best_hour if best_hour <= 12 else best_hour - 12
        display_hour = 12 if display_hour == 0 else display_hour
        fav_hour = f"{int(display_hour)}:00 {am_pm}"
    else:
        fav_day = "their usual day"
        fav_hour = "their usual time"
        
    return items_list, top_items_df, fav_day, fav_hour

# Streamlit UI & Chat Logic
st.set_page_config(page_title="Instacart AI Agent", layout="wide")
st.title("Instacart AI Marketing Agent ")
st.write("Enter **Customer ID** or **Product Name** to generate targeted campaigns.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "data_df" in message and message["data_df"] is not None:
            with st.expander("View Raw Data & Analytics"):
                st.write(message["data_description"])
                st.dataframe(message["data_df"], use_container_width=True)

if prompt := st.chat_input("Enter Customer ID (e.g., 3) or Product Name..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    ai_prompt = ""
    raw_data_df = None
    data_desc = ""

    if prompt.isdigit(): 
        user_id = prompt
        reorder_items, reorder_df_raw, fav_day, fav_hour = get_user_insights(user_id)
        
        if reorder_items:
            main_item = reorder_items[0]
            cross_sell_items, mba_df_raw = get_mba_insights(main_item)
            
            raw_data_df = reorder_df_raw[['product_name', 'probability', 'rank']]
            data_desc = f"Top Reorder Predictions for User {user_id} (Fav Time: {fav_day} {fav_hour})"
            
            ai_prompt = f"""
            You are a Professional AI Marketing Assistant.
            
            Customer Profile:
            - Customer ID: {user_id}
            - Shopping Habit: Most frequently shops on {fav_day} around {fav_hour}.
            - Likely to reorder: {', '.join(reorder_items)}
            
            Market Basket Insights:
            - Because they buy '{main_item}', they are highly likely to also buy: {', '.join(cross_sell_items) if cross_sell_items else 'None'}
            
            Task:
            Write a short, engaging push notification. 
            Mention their favorite shopping time context (e.g., preparing for Sunday morning).
            Remind them of their reorder items and offer a seamless cross-sell promotion.
            (Respond strictly in English. Do not use any emojis.)
            """
        else:
            error_msg = f"No purchase history found for Customer ID {user_id}."
            st.chat_message("assistant").markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            st.stop()

    else:
        product_name = prompt
        cross_sell_items, mba_df_raw = get_mba_insights(product_name)
        
        if cross_sell_items:
            raw_data_df = mba_df_raw[['product_name_A', 'product_name_B', 'confidence', 'lift']]
            data_desc = f"Market Basket Rules for '{product_name}'"
            
            ai_prompt = f"""
            Main Product: '{product_name}' 
            Frequently bought together (MBA): {', '.join(cross_sell_items)}
            
            Task: Briefly explain the business logic of why these items go well together and suggest a specific bundle pricing strategy.
            (Respond strictly in English. Do not use any emojis.)
            """
        else:
            error_msg = f"No Association Rules data available for '{product_name}'."
            st.chat_message("assistant").markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            st.stop()

    with st.spinner("Analyzing data and generating campaign..."):
        try:
            response = llm_model.generate_content(ai_prompt)
            ai_reply = response.text
        except Exception as e:
            ai_reply = f"Error: {e}"

    with st.chat_message("assistant"):
        st.markdown(ai_reply)
        if raw_data_df is not None:
            with st.expander("View Raw Data & Analytics"):
                st.write(data_desc)
                st.dataframe(raw_data_df, use_container_width=True)
                
    st.session_state.messages.append({
        "role": "assistant", 
        "content": ai_reply,
        "data_df": raw_data_df,
        "data_description": data_desc
    })