import streamlit as st

def loan_approval(client_name, income, credit_score, loan_amount):
    # Basic loan approval logic (you can customize this according to your bank's criteria)
    if income > 50000 and credit_score > 700 and loan_amount < income * 0.5:
        return True
    else:
        return False

def main():
    st.title("Loan Approval App")

    client_name = st.text_input("Enter client name:")
    income = st.number_input("Enter client's monthly income:")
    credit_score = st.number_input("Enter client's credit score:")
    loan_amount = st.number_input("Enter requested loan amount:")

    if st.button("Check Loan Eligibility"):
        if loan_approval(client_name, income, credit_score, loan_amount):
            st.success(f"Congratulations! {client_name} is eligible for the loan.")
        else:
            st.error(f"Sorry, {client_name} is not eligible for the loan.")

if __name__ == "__main__":
    main()
