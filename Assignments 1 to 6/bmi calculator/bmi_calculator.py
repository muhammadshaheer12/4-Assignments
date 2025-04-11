import streamlit as st

# App title section 
st.title("💪 BMI Calculator 🧮") 
st.write("Quickly calculate your Body Mass Index and check your health category 🧠📊")  

# Input card-style layout
with st.container():
    # Styled input section using HTML/CSS
    st.markdown("""<div style='padding:20px; border-radius:10px; background-color:#f9f9f9;'>""", unsafe_allow_html=True)

    # User inputs
    name = st.text_input("👤 Enter your name:")
    height = st.number_input("📏 Height in meters (e.g., 1.75):", min_value=0.0, step=0.01, format="%.2f")
    weight = st.number_input("⚖️ Weight in kilograms (e.g., 70):", min_value=0.0, step=0.1, format="%.1f")
    age = st.number_input("🎂 Enter your age:", min_value=0, step=1)
    gender = st.radio("🚻 Select your gender:", ["👨 Male", "👩 Female", "⚧️ Other"])

    st.markdown("""</div>""", unsafe_allow_html=True)

# BMI Calculation logic
def calculate_bmi(height, weight):
    # Formula: weight (kg) / height^2 (m^2)
    if height > 0:
        return round(weight / (height ** 2), 2)
    return 0

# Determine BMI Category
def get_bmi_category(bmi):
    if bmi == 0:
        return "Invalid input ❌"
    elif bmi < 18.5:
        return "Underweight 😟🥬"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight 😊💪"
    elif 25 <= bmi < 29.9:
        return "Overweight 😐🍩"
    else:
        return "Obese 😟⚠️"

# Button to trigger BMI calculation
if st.button("🚀 Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)     

        # Display results in styled container
        st.markdown("""
            <div style='text-align:center; padding:20px; background-color:#e8f5e9; border-radius:10px;'>
                <h3>👋 Hello, {}</h3>
                <h4>Your BMI is <span style='color:#4CAF50;'>🧮 {}</span></h4>
                <p><strong>📊 Category:</strong> {}</p>
                <p>🧑‍💼 Age: {} | 🧬 Gender: {}</p>
            </div>
        """.format(name if name else "User", bmi, category, age, gender), unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter valid height and weight. 📏⚖️") 
