import streamlit as st
import ktrain
from ktrain import text

# Load the saved predictor
save_directory = 'C:/Users/HP/Desktop/Project_Deployment'
predictor = ktrain.load_predictor(save_directory)

st.title("BERT Model Prediction App")
text_input = st.text_area("Enter text:", "")
if st.button("Predict"):
    if text_input:
        prediction = predictor.predict(text_input)
        st.write(f"Predicted Label: {prediction}")
