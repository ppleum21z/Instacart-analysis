# Instacart Analytics: End-to-End Data Science & Data analysis
**A comprehensive, end-to-end data project covering Data Analytics, Predictive Machine Learning, and Generative AI to extract actionable business insights from Instacart's 3 million+ grocery basket dataset.**


---

### Data Source
The dataset used in this project is the public **Instacart Market Basket Analysis** dataset from Kaggle. It contains anonymized data of over 3 million grocery orders from more than 200,000 Instacart users.
- **Source:** [Instacart Market Basket Analysis (Kaggle)](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis)
- **Data includes:** Order details, product information, aisles/departments, and the sequence of products added to the cart.
  
---

## Project Overview & Key Features

This project is divided into 4 main pillars to solve real-world e-commerce challenges:

### 1. Business Intelligence Dashboard (Power BI)
- Designed an interactive dashboard to provide the management team with a high-level overview of business performance.
- Tracked customer retention, peak purchasing hours, and drilled down into department and aisle-level product performance.

### 2. Reorder Prediction (Machine Learning)
- **Objective:** Predict whether a customer will reorder a specific product in their next purchase.
- **Tech Stack:** `XGBoost` & `CatBoost`
- **Process:** Conducted robust feature engineering based on user historical behavior. The trained models are saved locally (e.g., `xgb_reorder_model.json`) utilizing relative paths for seamless cross-platform execution.

### 3. Market Basket Analysis (Custom Algorithm)
- **Objective:** Uncover hidden patterns in customer purchasing behavior to identify cross-selling opportunities (Association Rules).
- **Engineering Highlight:** Instead of using standard libraries like `mlxtend` (which easily cause Out-Of-Memory errors on 3M+ rows due to heavy matrix transformations), **I engineered a custom, memory-efficient algorithm using `collections.Counter` and `itertools.combinations`.**
- **Metrics Calculated:** Support, Confidence, and Lift metrics were generated flawlessly without crashing the system, proving readiness for Big Data environments.

### 4. AI Agent Chatbot (Generative AI)
- **Objective:** Develop a smart assistant capable of querying data insights and providing product recommendations using Natural Language.
- **Tech Stack:** `Python`, `LLM APIs`, 
- **Security:** API keys are strictly managed via a `.env` file (excluded from GitHub via `.gitignore`) to ensure enterprise-level security standards.
- **[Try the live AI Agent demo here](https://huggingface.co/spaces/fighter21z/Instacart-AIAgent)**
<img width="1895" height="725" alt="image" src="https://github.com/user-attachments/assets/f77f1cf3-ce10-4d9f-a7cc-be51b54ebb34" />


---

## Tech Stack & Tools
- **Data Manipulation:** Python (Pandas, NumPy, Polars)
- **Machine Learning:** LightGBM, XGBoost, CatBoost
- **Data Visualization:** Power BI, Matplotlib, Seaborn
- **AI / LLM Integration:** Google API (Gemini)
- **Web App / UI:** Streamlit / Python (for `app.py`)

---

## Downloads (Data & Dashboard)
Due to GitHub's file size limits (>100MB), the raw datasets and the complete Power BI file are hosted securely on external cloud storage. You can access them here:

- **[Download Power BI Dashboard (.pbix) - 331 MB](https://drive.google.com/file/d/1u_8GokNC_ck8vbR5_rLZ4jxjnuzOgJ-m/view?usp=sharing)**
- **[Download Raw & Processed Data (.zip)](https://drive.google.com/file/d/1kkq8Bd3bJvDdN8uDiPqy5x-RuqAMsDjh/view?usp=sharing)**

---
## Preview Dashboard
<img width="1303" height="721" alt="image" src="https://github.com/user-attachments/assets/6db9b565-bb7f-4ef9-8422-5b8d80eb54b5" />
<img width="1300" height="733" alt="image" src="https://github.com/user-attachments/assets/00685dfc-049d-4683-9035-c245d2cc79dd" />
<img width="1330" height="745" alt="image" src="https://github.com/user-attachments/assets/80a548c2-95b3-4a11-8236-2f46b445846d" />
<img width="1323" height="758" alt="image" src="https://github.com/user-attachments/assets/26ebc975-2301-4946-936a-beee5f30fd3e" />
<img width="1330" height="747" alt="image" src="https://github.com/user-attachments/assets/3354c8be-6370-4d38-b899-6eeb216edece" />

## Insight 
### Business Performance Overview
- Produce (29%) and Dairy Eggs (17%) dominate total sales, acting as the primary revenue drivers.
- Sales are highly concentrated: a small group of top products generates a disproportionate share of total volume (Pareto effect).
- Customers purchase an average of 9.9 items per order (median: 7), indicating a right‑skewed basket distribution driven by heavy buyers.
- Each customer places approximately 16.6 orders on average, reflecting strong engagement.
- Weekend-Heavy Peak Times: The Day/Hour heatmap reveals a highly concentrated shopping window on Sundays and Mondays between 09:00 AM and 04:00 PM (peaking specifically from 09:00 to 12:00).

### Customer Behavior & Loyalty
- Overall Reorder Rate is 59%, demonstrating strong customer retention.
- The median reorder cycle is 7 days, indicating a predominantly weekly shopping pattern.
- Mature User Base: The customer base is currently dominated by 'Regular Customers' (39%), while 'New Customers' make up only 11.6%. This indicates a mature platform where growth strategies must pivot heavily from acquisition toward upselling and maximizing Customer Lifetime Value (CLTV).
- VIP customers exhibit the highest basket size and strongest organic preference (34%), indicating higher-value and more health-oriented behavior.
- Fresh and organic produce items are the most common first purchases, positioning Produce as a key customer acquisition driver.
- Highly Engaged Core: Combined, 'Loyal' and 'VIP' customers make up nearly 50% (49.32%) of the total user base. This indicates a highly resilient business model that is not overly dependent on constant new customer acquisition.

### Product Portfolio & Loyalty Dynamics
- Dairy Eggs emerges as a “Star Category” (high volume, high loyalty).
- Produce leads in volume but has slightly lower loyalty than Dairy, suggesting an opportunity to improve repeat engagement.
- Top 10 Reorder Rate list, Organic Milk variations command the top spots with staggering retention rates exceeding 85%, proving that milk is the ultimate habit-forming product.
- Hidden Gems (Niche but Sticky): The Department Performance Matrix reveals that non-core categories like Pets, Bulk, and Alcohol achieve reorder rates significantly above the 59% average, acting as low-volume but high-loyalty drivers.
- Categories Requiring Intervention: Household and Personal Care fall into the lower-right quadrant (low loyalty, moderate volume), highlighting a clear need for retention strategies in these departments.

### Market Basket & Cross-Sell Opportunities
- Banana frequently co-occurs with Organic Avocado and other fresh produce, highlighting strong cross-sell potential within healthy product segments.
- Cross-sell relationships are strongest within fresh and organic categories, suggesting opportunity for bundle-based promotions.

### Strategic Implications
- Develop healthy bundle promotions (e.g., Banana + Avocado + Citrus).
- Launch "Monthly Stock-Up / Payday" campaigns targeting the 30-day replenishment cohort with bulk-buy incentives.
- Optimize the Checkout UI ("Frequently Bought Together" widget) to prioritize High-Confidence items (e.g., Avocados/Lemons over Pears) to maximize immediate cart conversions.
- Implement targeted loyalty campaigns for lower-retention categories (e.g., Household).
- Leverage association rules to power personalized recommendations and promotional strategies.

