import streamlit as st

st.title("📌 About This Model")

# ===== LOGO CENTERED =====
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("photo.jpg",width=350)

st.markdown("""
### 🤖 Model Used: Linear Regression

This app uses a simple Machine Learning algorithm called Linear Regression.

It predicts delivery time based on distance using the equation:

**Time = m × Distance + c**

---

### 📊 What it means:
- Distance increases → Time increases
- The relationship is linear

---


### 🎯 Why this model?
- Simple and fast
- Works well for linear relationships
- Easy to interpret

---

### 🚀 Future Improvements:
- Add traffic conditions
- Add weather data
- Use advanced ML models
""")