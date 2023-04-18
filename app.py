import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the dataset into a pandas dataframe
df = pd.read_csv("winequality-red.csv")


# Check for missing values
print(df.isnull().sum())
print(df)
# Replace missing values with the mean
df.fillna(df.mean(), inplace=True)

# # Check for outliers
# # You can use box plots or scatter plots to identify outliers
# # Remove outliers that are more than 3 standard deviations away from the mean
df = df[(df["quality"] - df["quality"].mean()).abs() < 2 * df["quality"].std()]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df.drop("quality", axis=1), df["quality"], test_size=0.2, random_state=42
)

# Train a random forest regression model on the training set
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Create a Streamlit app
st.set_page_config(page_title='Red Wine Quality Predictor')
st.title("Red Wine Quality Predictor")
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/8678044.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# Create a form for the user to input features
form = st.form(key='input_form')
fixed_acidity = form.number_input("Fixed Acidity")
volatile_acidity = form.number_input("Volatile Acidity")
citric_acid = form.number_input("Citric Acid")
residual_sugar = form.number_input("Residual Sugar")
chlorides = form.number_input("Chlorides")
free_sulfur_dioxide = form.number_input("Free Sulfur Dioxide")
total_sulfur_dioxide = form.number_input("Total Sulfur Dioxide")
density = form.number_input("Density")
pH = form.number_input("pH")
sulphates = form.number_input("Sulphates")
alcohol = form.number_input("Alcohol")

submit_button = form.form_submit_button(label='Submit')

# Make a prediction based on the user's input
if submit_button:
    input_data = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]]

    prediction = model.predict(input_data)[0]
    st.header(f"The predicted quality is {prediction:.2f}")
