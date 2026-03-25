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

