import streamlit as st

# Page configuration
st.set_page_config(page_title="The Vitality Link", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    /* HEADER IMAGE */
    .header-container {
        text-align: center;
        margin-bottom: 20px;
    }

    .header-container img {
        max-width: 100%;
        height: auto;
        border-radius: 12px;
    }

    /* TAB STYLING */
    div[data-testid="stTabs"] button {
        color: #CD7F32;
        font-weight: bold;
        background-color: #F9F5EF;
        border-bottom: 2px solid transparent;
    }

    div[data-testid="stTabs"] button:hover {
        color: #D8A25C !important;
        border-bottom: 2px solid #D8A25C;
        background-color: #fefbf8;
    }

    div[data-testid="stTabs"] button[aria-selected="true"] {
        color: #CD7F32 !important;
        border-bottom: 3px solid #CD7F32 !important
