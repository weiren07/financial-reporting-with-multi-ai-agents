import streamlit as st
from analysis_core import run_stock_analysis

st.set_page_config(page_title="Stock Analysis Report",layout="wide")
st.title("📈 Stock Analysis Report")
st.markdown("")
ticker = st.text_input("Ticker Symbol",).upper( )
if st.button("🚀 Analyze"):
    if not ticker:
        st.error("Please enter a valid ticker symbol.")
    else:
        with st.spinner(f"Analyzing {ticker}..."):
            report, output_file = run_stock_analysis(ticker)
        st.markdown("## Analysis Report")
        st.markdown(report)
        st.success(f"Report saved to: **{output_file}**")
else:
    st.info("Enter a ticker symbol and click 'Analyze' to begin.")