import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit App UI
st.title("📊 Data Quality Checker")

# Upload File
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview:")
    st.dataframe(df.head())

    # Primary Key Finder
    st.write("### 🔑 Primary Key Analysis")
    primary_keys = [col for col in df.columns if df[col].is_unique]
    if primary_keys:
        st.success(f"Possible Primary Keys: {', '.join(primary_keys)}")
    else:
        st.warning("No Primary Key found.")

    # Data Quality Report
    st.write("### 📊 Data Quality Report")
    missing_values = df.isnull().sum()
    duplicates = df.duplicated().sum()

    st.write("🛑 **Missing Values:**")
    st.write(missing_values[missing_values > 0])

    st.write(f"🔁 **Duplicate Rows:** {duplicates}")

    # Missing Values Heatmap
    st.write("### 🖼 Missing Values Heatmap")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cmap="viridis", cbar=False, yticklabels=False)
    st.pyplot(plt)
