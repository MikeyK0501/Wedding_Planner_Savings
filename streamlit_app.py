import streamlit as st
import datetime

# This is the main function that will be run when the app starts
def display_wedding_savings_calculator():
    # Your wedding savings calculator code here
    st.write("This is where your savings calculator logic will go.")
    # Example: Placeholder code for wedding savings calculator
    st.subheader("Wedding Savings Calculator")

def main():
    # Set the title of the app
    st.title("🎈 Wedding Savings App")

    # Select a page using a selectbox
    page = st.selectbox("Choose a Page", ["Home", "Wedding Savings"], key="page_selectbox")

    if page == "Home":
        st.write("Welcome to the home page!")
    elif page == "Wedding Savings":
        display_wedding_savings_calculator()  # Call the function directly here

if __name__ == "__main__":
    main()
