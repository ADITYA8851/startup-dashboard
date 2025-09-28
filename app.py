import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset safely (works locally & on Streamlit Cloud)
file_path = os.path.join(os.path.dirname(__file__), "startup_cleaned.csv")
df = pd.read_csv(file_path)

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one', ['overall analysis','startup','Investor'])

# --- Overall Analysis ---
def overall_analysis():
    st.title("Overall Analysis")
    st.write("Coming soon...")

# --- Startup Analysis ---
def startup_analysis(selected_startup):
    st.title("Startup Analysis")
    startup_info = df[df['startup'] == selected_startup][['date','vertical','round','investors','amount']]
    st.subheader(f"Details of {selected_startup}")
    st.dataframe(startup_info)

# --- Investor Analysis ---
def investor_analysis(selected_investor):
    st.title("Investor Analysis")
    investor_info = df[df['investors'].str.contains(selected_investor, na=False)][['date','startup','vertical','round','amount']]
    st.subheader(f"Investments by {selected_investor}")
    st.dataframe(investor_info)

# Sidebar Navigation
if option == 'overall analysis':
    overall_analysis()

elif option == 'startup':
    selected_startup = st.sidebar.selectbox('Select Startup', sorted(df['startup'].dropna().unique().tolist()))
    if st.sidebar.button('Find Startup Details'):
        startup_analysis(selected_startup)

elif option == 'Investor':
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(df['investors'].dropna().unique().tolist()))
    if st.sidebar.button('Find Investor Details'):
        investor_analysis(selected_investor)
