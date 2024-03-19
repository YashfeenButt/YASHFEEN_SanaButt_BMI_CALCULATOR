import streamlit as st

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    st.title("Even/Odd Number Checker")
    number = st.number_input("Enter a number:")
    
    if st.button("Check"):
        result = is_even_or_odd(number)
        st.write(f"The number {number} is {result}.")

if __name__ == "__main__":
    main()
