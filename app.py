import streamlit as st

st.set_page_config(page_title="Delivery Predictor", page_icon="🚚", layout="wide")

# ===== TITLE =====
st.title("🚚 Smart Delivery Time Predictor")

# ===== LOGO CENTERED =====
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("new.jpg",width=350)

# ===== TAGLINE =====
st.markdown("## ⏱ Why wait blindly when you can predict your delivery time?")

st.markdown("""
Get instant delivery time predictions using Machine Learning 🚀  
Plan smarter. Save time. Stay ahead.
""")

st.markdown("---")

st.markdown("👉 Go to **Predict Page** from sidebar to try it out!")
st.set_page_config(page_title="Delivery Predictor", page_icon="🚚", layout="wide")

# ===== HOME PAGE =====
st.title("🚚 Smart Delivery Time Predictor")

st.markdown("## ⏱ Predict Before You Wait!")

st.markdown("""
Why wait blindly for your delivery?  
Use Machine Learning to estimate your delivery time instantly.

### 💡 What this app does:
- Predicts delivery time based on distance
- Uses Linear Regression
- Gives real-time insights

👉 Go to **Predict Page** from the sidebar to try it out!
""")

# Optional logo (if you add image)
# st.image("logo.png", width=150)

st.markdown("---")
st.markdown("🚀 Built with Streamlit + Machine Learning")