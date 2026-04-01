import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

st.title("📈 Delivery Time Prediction")

# ===== FILE UPLOAD =====
st.subheader("📂 Upload Your Dataset (Optional)")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# ===== LOAD DATA =====
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Normalize column names
    df.columns = [col.lower() for col in df.columns]

    # Validate columns
    if 'distance' in df.columns and 'time' in df.columns:
        st.success("✅ Custom dataset loaded successfully!")
    else:
        st.error("❌ CSV must contain 'Distance' and 'Time' columns")
        st.stop()
else:
    df = pd.read_csv('delivery_data_sample.csv')
    df = df.rename(columns={'Distance': 'distance', 'Time': 'time'})

# ===== DATA PREVIEW =====
with st.expander("📊 Dataset Preview"):
    st.dataframe(df.head())

# ===== MODEL TRAINING =====
X = df[['distance']]
y = df['time']

model = LinearRegression()
model.fit(X, y)

# ===== INPUT SECTION =====
st.subheader("📍 Enter Distance")

distance = st.number_input(
    "Enter distance (in km)",
    min_value=0.0,
    max_value=50.0,
    step=0.5
)

# ===== PREDICTION =====
if st.button("Predict Delivery Time"):
    prediction = model.predict([[distance]])

    st.success(f"🚀 Estimated Delivery Time: {prediction[0]:.2f} minutes")

    # Smart message
    if prediction[0] < 25:
        st.info("⚡ Super fast delivery expected!")
    elif prediction[0] < 40:
        st.warning("🕒 Moderate delivery time")
    else:
        st.error("⏳ Delivery might take longer than usual")

# ===== METRICS =====
st.subheader("📊 Insights")

col1, col2 = st.columns(2)
col1.metric("📏 Avg Distance", f"{df['distance'].mean():.2f} km")
col2.metric("⏳ Avg Time", f"{df['time'].mean():.2f} min")

# ===== GRAPH =====
st.subheader("📉 Visualization")

fig, ax = plt.subplots(figsize=(4, 2.5))

ax.scatter(df['distance'], df['time'])

m, b = np.polyfit(df['distance'], df['time'], 1)
x = np.linspace(df['distance'].min(), df['distance'].max(), 100)
y_line = m * x + b

ax.plot(x, y_line)

ax.set_xlabel("Distance")
ax.set_ylabel("Time")

st.pyplot(fig)

# ===== FORMAT GUIDE =====
with st.expander("📄 Expected CSV Format"):
    st.markdown("""
    Your CSV must have:

    Distance,Time  
    2,15  
    5,30  
    8,50  

    - Distance → in km  
    - Time → in minutes  
    """)

if df.isnull().sum().sum() > 0:
    st.warning("⚠️ Dataset contains missing values")
# ===== MODEL INFO =====
st.subheader("📌 Model Details")
st.write(f"Slope (m): {model.coef_[0]:.2f}")
st.write(f"Intercept (c): {model.intercept_:.2f}")