import streamlit as st

st.set_page_config(page_title="Financial Literacy & Cyber Fraud Quiz")

st.title("🧠 Financial Literacy & Cyber Fraud Quiz")
st.write("Test your knowledge with these 10 interactive questions!")

questions = [
    {
        "question": "1. What is the safest way to keep your online banking password secure?",
        "options": [
            "Share it with close friends",
            "Use the same password everywhere",
            "Use a strong unique password",
            "Write it publicly in notes"
        ],
        "answer": "Use a strong unique password"
    },
    {
        "question": "2. What does SIP stand for in mutual funds?",
        "options": [
            "Safe Investment Plan",
            "Systematic Investment Plan",
            "Savings Interest Program",
            "Secure Income Policy"
        ],
        "answer": "Systematic Investment Plan"
    },
    {
        "question": "3. Which of these is a common cyber fraud?",
        "options": [
            "Phishing",
            "Saving money",
            "Budget planning",
            "Opening FD"
        ],
        "answer": "Phishing"
    },
    {
        "question": "4. What should you do if you receive a suspicious OTP request?",
        "options": [
            "Share OTP quickly",
            "Ignore and never share OTP",
            "Post it online",
            "Forward it to strangers"
        ],
        "answer": "Ignore and never share OTP"
    },
    {
        "question": "5. Emergency funds are mainly used for:",
        "options": [
            "Luxury shopping",
            "Unexpected expenses",
            "Gaming",
            "Buying random items"
        ],
        "answer": "Unexpected expenses"
    },
    {
        "question": "6. Which app lock is more secure?",
        "options": [
            "1234",
            "Password",
            "Fingerprint/Face Lock",
            "Date of birth"
        ],
        "answer": "Fingerprint/Face Lock"
    },
    {
        "question": "7. What is budgeting?",
        "options": [
            "Spending without limits",
            "Planning income and expenses",
            "Ignoring savings",
            "Taking loans always"
        ],
        "answer": "Planning income and expenses"
    },
    {
        "question": "8. A fake message asking for bank details is called:",
        "options": [
            "Investment",
            "Phishing scam",
            "Budget alert",
            "EMI reminder"
        ],
        "answer": "Phishing scam"
    },
    {
        "question": "9. Why is saving money important?",
        "options": [
            "For emergencies and future goals",
            "To waste later",
            "To avoid banks",
            "No reason"
        ],
        "answer": "For emergencies and future goals"
    },
    {
        "question": "10. What should you check before clicking a website link?",
        "options": [
            "Website URL and security",
            "Only colors",
            "Random ads",
            "Nothing"
        ],
        "answer": "Website URL and security"
    }
]

score = 0
user_answers = []

for q in questions:
    st.subheader(q["question"])
    ans = st.radio(
        "Choose one:",
        q["options"],
        key=q["question"]
    )
    user_answers.append((ans, q["answer"]))

if st.button("Submit Quiz 🚀"):
    for user, correct in user_answers:
        if user == correct:
            score += 1

    st.success(f"🎉 Your Score: {score}/10")

    if score == 10:
        st.balloons()
        st.write("Excellent! You're financially and digitally smart! 😎")
    elif score >= 7:
        st.write("Great job! Keep learning and staying safe online 👍")
    elif score >= 4:
        st.write("Good attempt! A little more awareness will help 💡")
    else:
        st.write("Keep practicing financial and cyber safety skills 🔐")
