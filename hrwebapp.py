import pandas as pd
import numpy as np
import streamlit as st
import pickle


with open("hr_model",'rb') as f:
    model=pickle.load(f)

def hr_pred(input_data, Employee_name):
    data_as_array = np.asarray(input_data).reshape(1, -1)
    prediction=model.predict(data_as_array)

    if(prediction[0]==0):
        return f"The Employee {Employee_name} is not likely to leave the company"
    
    else:
        return f"The Employee {Employee_name} is  likely to leave  the company"
    
def main():
    st.title("Employee Retention Prediction")
    st.write("A web application that predicts if your employee is likely to leave the company or not based on the given parameters.")

    # name -> text input
    # satisfaction level -> slider
    # average monthly working hours -> input number
    # promotion in the last 5 years -> Yes or No radio
    # Work accident  -> Yes or No check box
    # salary -> high low medium select_slider

    Employee_name = st.text_input("Enter the Employee name")
    satisfaction_level = st.slider("Enetr Satisfaction level in percentage", 0, 100)
    st.write(f"Employee Satisfaction Level is {satisfaction_level} %.")
    satisfaction_level=satisfaction_level/100
    avg_hours = st.number_input("Enter the average monthly working hours")
    st.write(f"The average month working hours is {avg_hours} hrs")
    promotion = st.radio("Did the Employee get any promotion in the last 5 years ?",('Yes','No'))
    if promotion=='Yes':
        st.write("The Employee has got a promotion in the last 5 years")
        promotion=1
    else:
        st.write("The Employee has not got any promotion in the last 5 years")
        promotion=0
    work_accident = st.radio("Did the Employee have any work accident ?",('Yes','No'))
    if work_accident=='Yes':
        work_accident=1
    else:
        work_accident=0
    salary = st.select_slider("Enter range of the Employee Salary", options=['low','medium','high'])

    if salary=='high':
        high=1; medium=0
    elif salary=='medium':
        high=0; medium=1
    else:
        high=0; medium=0

    pred=''
    if st.button("Predict"):
        pred=hr_pred([satisfaction_level, avg_hours, promotion, work_accident, high, medium], Employee_name)
        if 'not' in pred:
            st.success(pred)
        else:
            st.error(pred)

if __name__ == '__main__':
    main()
    


