import streamlit as st

# Assuming `streamlit_app.py` is the core of the app and contains the function `display_wedding_savings_calculator`

def main():
    st.title("🎈 New App")

    # Use a unique key for the selectbox widget
    page = st.selectbox("Choose a Page", ["Home", "Wedding Savings"], key="page_selectbox")

    if page == "Home":
        st.write("Welcome to the home page!")

    elif page == "Wedding Savings":
        import streamlit_app  # Import the core logic here
        streamlit_app.display_wedding_savings_calculator()

if __name__ == "__main__":
    main()
