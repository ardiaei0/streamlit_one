import streamlit as st

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))

def add_two(num_1,num_2):
    result = num1 + num2
    return result

def main():
    st.title('Add two numbers')
    num1 = st.number_input('enter a number')
    num2 = st.number_input('enter a number')
    
total = add_two(num1,num2)
st.write(total)