import streamlit as st
import requests

API_URI = "http://127.0.0.1:8000/execute"

st.title("General Question Answer.")

query = st.text_area("Enter your query")

if st.button("Submit Query"):
    if query:
        try:
            response = requests.post(API_URI, json={"messages": query}, verify=False)
            if response.status_code == 200:
                st.success("Response Received:")
                # st.write(response.json()["messages"][-1]["content"])
                st.markdown(response.json()["messages"][-1]["content"], unsafe_allow_html=True)
            else:
                st.error(f"Error {response.status_code}: Could not process the request.")
        except Exception as e:
            st.error(f"Exception occurred: {e}")
    else:
        st.error("Please enter both userid and query...")