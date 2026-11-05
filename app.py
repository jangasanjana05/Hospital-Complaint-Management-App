
import streamlit as st

st.set_page_config(
    page_title="Hospital Complaint Management",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Hospital Complaint Management System")

st.write(
    "An NLP-based application for hospital complaint "
    "classification and priority prediction."
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a page",
    [
        "Home",
        "Complaint Prediction",
        "Complaint History",
        "Dashboard",
        "About Project"
    ]
)

if page == "Home":
    st.header("Welcome")
    st.info("Welcome to the Hospital Complaint Management System.")
    st.write("Use the navigation menu to explore the application.")

elif page == "Complaint Prediction":
    st.header("📝 Complaint Prediction")
    complaint = st.text_area("Enter Hospital Complaint")
    if st.button("Predict Complaint"):
        if complaint.strip():
            st.success("Complaint received successfully!")
            st.write("Prediction feature will be added in the next step.")
        else:
            st.warning("Please enter a complaint.")

elif page == "Complaint History":
    st.header("📋 Complaint History")
    st.info("Complaint history feature will be added.")

elif page == "Dashboard":
    st.header("📊 Dashboard")
    st.info("Dashboard charts will be added.")

elif page == "About Project":
    st.header("ℹ️ About Project")
    st.write("""
    Project: Hospital Complaint Classification and
    Priority Prediction Using Natural Language Processing.

    Technologies:
    - Python
    - Streamlit
    - Natural Language Processing
    - Machine Learning
    """)
