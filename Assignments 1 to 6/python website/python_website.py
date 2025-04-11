import streamlit as st

# Set the title of the web app 
st.title("🐍✨ Welcome to the Python Website! 🖥️🌐")

# Description text 
st.write("""
👋 Hello there, Pythonista! 🐍

This is a fun and simple website built with **Streamlit** and Python. 💡🔧  
Click the button below to get your fun surprise! 🎉🎁
""")

# Display a success or warning message based on button click
if st.button("Click me for a fun surprise! 🎊🚀"):
    st.success("🎉 Surprise! You're awesome! 🌈💻 Keep coding and keep having fun with Python! 🐍✨")
else:
    st.warning("👆 Don't be shy! Click the magic button above to unlock your surprise! 🧙‍♂️✨")

# Additional Fun Section: Python Facts 🧠🐍
st.markdown("---")
st.subheader("📚 Did You Know? Fun Python Facts")
python_facts = [
    "🐍 Python was named after *Monty Python*, not the snake!",
    "🔢 Python uses indentation instead of brackets—clean and easy to read!",
    "🌍 Python is used by companies like Google, Netflix, and NASA!",
    "📊 Python is great for data science, web development, automation, and more!",
    "💬 Python has a huge, friendly community with tons of libraries!"
]
for fact in python_facts:
    st.write(fact)

# User Interaction: Favorite Python Feature Input 💬
st.markdown("---")
st.subheader("💬 What's your favorite Python feature?")
user_input = st.text_input("Type your favorite thing about Python (e.g., simplicity, libraries, etc.) ✍️")
if user_input:
    st.write(f"🙌 That's awesome! You love Python for: **{user_input}** 🐍💙")

# End of page warning
st.warning("⚠️ You’ve reached the end of the page! Thanks for visiting! 🌟")
