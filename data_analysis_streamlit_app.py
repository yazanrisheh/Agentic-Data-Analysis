import os
os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"] = "2000"
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Set Streamlit to wide mode
st.set_page_config(layout="wide", page_title="Main Dashboard", page_icon="📊")


data_visualisation_page = st.Page(
    "./Pages/python_visualisation_agent.py", title="Data Visualisation", icon="📈"
)

Pages = st.navigation(
    {
        "Visualisation Agent": [data_visualisation_page]
    }
)

Pages.run()