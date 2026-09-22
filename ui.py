import streamlit as st
import joblib
import pandas as pd


# -------------------- Loading resources --------------------

model = joblib.load('bmi_model.joblib')
scaler = joblib.load('data_scaler.joblib')


# -------------------- Page configuration --------------------

st.set_page_config(
    page_title='BMI Health Classification',
    layout='centered',
    page_icon='🩺'
)


# -------------------- Title --------------------

st.subheader('🩺 BMI Health Classification')


# -------------------- About section --------------------

with st.expander('📄 About this webpage'):

    st.write('''
    This model estimates the BMI category using:

    👤 **Gender:** Male / Female

    📏 **Height:** Number (cm)

    ⚖️ **Weight:** Number (Kg)

    ### 🎯 BMI Categories

    **0 – Extremely Weak**

    **1 – Weak**

    **2 – Normal**

    **3 – Overweight**

    **4 – Obesity**

    **5 – Extreme Obesity**

    🔮 The model uses these inputs to predict your BMI category.
    ''')


# -------------------- User input --------------------

with st.expander("🔮 Predict your BMI Category"):

    Gender = st.radio(
        'Gender',
        ['Male', 'Female']
    )

    Height = st.slider(
        "Select your height in centimeters",
        min_value=140,
        max_value=199
    )

    Weight = st.slider(
        "Select your weight in kilograms",
        min_value=50,
        max_value=160
    )

    p_button = st.button(
        "🔮 Predict",
        use_container_width=True
    )


# -------------------- Prediction --------------------

if p_button:

    # Convert Gender into one-hot encoded values
    female = float(1 if Gender == 'Female' else 0)
    male = float(1 if Gender == 'Male' else 0)


    # Create DataFrame containing numeric features
    numeric_features = pd.DataFrame({
        'Height': [Height],
        'Weight': [Weight]
    })


    # Scale Height and Weight
    scaled_features = scaler.transform(numeric_features)


    # Create the exact features expected by the trained model
    input_features = pd.DataFrame({
        'cat__Gender_Female': [female],
        'cat__Gender_Male': [male],
        'num__Height': [scaled_features[0][0]],
        'num__Weight': [scaled_features[0][1]]
    })


    # Make prediction
    prediction = model.predict(input_features)


    # -------------------- Prediction effects --------------------

    if prediction[0] == 0:

        st.warning("⚡ Extremely Weak")
        st.write("Your predicted BMI category is **Extremely Weak**.")

    elif prediction[0] == 1:

        st.warning("⚠️ Weak")
        st.write("Your predicted BMI category is **Weak**.")

    elif prediction[0] == 2:

        st.balloons()
        st.success("🎉 Normal")
        st.write("Your predicted BMI category is **Normal**.")

    elif prediction[0] == 3:

        st.info("💡 Overweight")
        st.write("Your predicted BMI category is **Overweight**.")

    elif prediction[0] == 4:

        st.warning("⚠️ Obesity")
        st.write("Your predicted BMI category is **Obesity**.")

    elif prediction[0] == 5:

        st.error("🚨 Extreme Obesity")
        st.write("Your predicted BMI category is **Extreme Obesity**.")