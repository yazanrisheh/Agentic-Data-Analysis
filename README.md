# Agentic Data Analysis

This is an AI agent built in LangGraph that can perform data analysis on a provided dataset.

## Getting Setup

Sample dataset

https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets/data 

Youll then need to install the requirements by running the following command:

```bash
pip install -r requirements.txt
```

and run the streamlit dashboard by running the following command:

```bash
streamlit run data_analysis_streamlit_app.py --server.maxUploadSize 2000
```

Update the OpenAI API key in the data_analysis_streamlit_app.py file with your own.
