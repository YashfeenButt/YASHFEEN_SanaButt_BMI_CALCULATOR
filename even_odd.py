import streamlit as st

def is_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
       import streamlit as st

def is_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    st.title("Even-Odd Checker")
    num = st.number_input("Enter a number:")
    
    if st.button("Check"):
        result = is_even_or_odd(num)
        st.write(f"The number {num} is {result}.")

if _name_ == "_main_":
    main()
   return "odd"

def main():
    st.title("Even-Odd Checker")
    num = st.number_input("Enter a number:")
    
    if st.button("Check"):
        result = is_even_or_odd(num)
        st.write(f"The number {num} is {result}.")

if _name_ == "_main_":
    main()
  
