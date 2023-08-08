import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
import pickle

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with open('email_model.pkl', 'rb') as file:
    model, cv = pickle.load(file)

# Preprocessing user entry
def user_entry(email):
    converted_email = cv.transform([email])
    return converted_email

# Prediction
def predict(converted_email):
    return model.predict(converted_email)[0]

def main():
    st.title("Email Spam Detector")
    email = st.text_input("Enter the message")
    if email:
        converted_email = user_entry(email)
        ans = predict(converted_email=converted_email)

        if(ans==0):
            st.success("🟢 Message is not spam")

        else:
            st.error("🔴 Message is spam")


if __name__=='__main__':
    main()