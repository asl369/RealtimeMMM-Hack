import numpy as np
import streamlit as st

st.title("Test Streamlit App")

if __name__=="__main__":
    cols = st.columns((0.2,0.6,0.2))

    cols[0].write("1st part")
    cols[1].write("2nd part")
    cols[2].write("3rd part")