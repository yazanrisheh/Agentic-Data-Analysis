# Agentic Data Analysis

This is an AI agent built in LangGraph that can perform data analysis on a provided dataset. It is to accompany my Youtube video to showcase some advanced LangGraph techniques.


## Getting Setup

If you want to use the same dataset as me, you can download it from Kaggle below:

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
