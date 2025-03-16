import streamlit as st

st.title("🎈 New App")

# Use streamlit's built-in page navigation
page = st.selectbox("Choose a Page", ["Home", "Wedding Savings"])

if page == "Home":
    st.write("Welcome to the home page!")

elif page == "Wedding Savings":
    import streamlit_app  # Import the core logic here
    streamlit_app.display_wedding_savings_calculator()
