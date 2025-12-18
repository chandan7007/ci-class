import streamlit as st 
#Streamlit UI
st.title("power calculator")
st.write("Enter a number to calculate exponents")

#get user input
n=st.number_input("enter a number",value=1,step=1)

#calculate the results
square=n**2
cube=n**3
fifth=n**5

####display results
st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is : {cube}")
st.write(f"the fifth power of {n} is : {fifth}")