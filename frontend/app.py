import streamlit as st
import requests

st.set_page_config(
    page_title="AI Exam Anxiety Detector",
    page_icon="🧠",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:bold;
    text-align:center;
}
.result-box {
    padding:15px;
    border-radius:10px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🎓 AI-Based Exam Anxiety Detector</div>', unsafe_allow_html=True)

st.write("Analyze your exam-related thoughts using AI.")

user_input = st.text_area("✍️ Enter your feelings about exams:")

if st.button("🔍 Analyze Anxiety"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"text": user_input}
            )

            result = response.json()
            anxiety_level = result["predicted_anxiety_level"]

            if anxiety_level == "Low Anxiety":
                st.success(f"😊 {anxiety_level}")
                st.info("You seem calm and prepared. Keep it up!")
            elif anxiety_level == "Moderate Anxiety":
                st.warning(f"😐 {anxiety_level}")
                st.write("Try breathing exercises and proper planning.")
            else:
                st.error(f"😟 {anxiety_level}")
                st.write("Consider speaking with a mentor or counselor.")

        except:
            st.error("⚠ Backend server is not running.")
