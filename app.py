import streamlit as st

st.title("Minimal Test App")
st.write("This is a minimal Streamlit app with no extra dependencies.")

if st.button("Click me"):
  st.success("Button clicked!")
