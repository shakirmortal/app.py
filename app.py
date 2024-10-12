%%writefile app.py
import streamlit as st

# Example Streamlit app
st.title("🎓 Personalized Study Plan Generator")

# Get user input for subject
subject = st.text_input("Enter the subject:", "Physics")

# Create a user profile dictionary (replace with dynamic inputs if needed)
learning_style = st.selectbox("Select your learning style", ['visual', 'auditory', 'kinesthetic'])
study_hours = st.slider("How many hours can you study per day?", 1, 8, 2)

user_profile = {
    'learning_style': learning_style,
    'time_available': study_hours,
    'current_level': 'beginner'
}

# Generate the study plan
if st.button("Generate Study Plan"):
    st.write(f"Generating a study plan for {subject} with a learning style of {learning_style} for {study_hours} hours.")
