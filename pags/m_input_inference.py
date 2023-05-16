import streamlit as st
import pandas as pd
from utils.load_model import load_model

def main():

    model = load_model()

    #['lstat', 'rm', 'ptratio', 'indus']

    input1 = st.number_input("lstat", value=0.00)
    input2 = st.number_input("rm", value=0.00)
    input3 = st.number_input("ptratio", value=0.00)
    input4 = st.number_input("indus", value=0.00)



    data = {
        "lstat": [input1],
        "rm": [input2],
        "ptratio": [input3],
        "indus": [input4],
    }

    df = pd.DataFrame(data)
    st.dataframe(df)
    y = model.predict(df)

    prediction = round(y[0], 2)
    prediction_color = "white"

    # Display the prediction with the specified color
    st.write("Prediction: ", f'<span style="color:{prediction_color}">{prediction}</span>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()