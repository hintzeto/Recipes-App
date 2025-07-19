import streamlit as st
from backend.scraper import scrape_url


st.set_page_config(page_title="AI Recipe Extractor", layout="wide")

st.title("🍽️ AI Recipe Extractor")
url = st.text_input("Enter the URL of the recipe page:")

if st.button("Extract Recipe"):
    with st.spinner("Fetching page..."):
        html = scrape_url(url)
        if html:
            st.success("Page fetched successfully!")
            st.text_area("HTML Content", html[:5000], height=300)
        else:
            st.error("Failed to fetch the page. Please check the URL and try again.")