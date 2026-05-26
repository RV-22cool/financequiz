import streamlit as st

st.set_page_config(page_title="Financial Literacy & Cyber Safety Quiz")

st.title("💰 Financial Literacy & Cyber Safety Quiz")
st.write("Interactive Quiz with MCQs, Match the Columns & Jumbled Words!")

score = 0

# ---------------- MCQ SECTION ---------------- #

st.header("📘 Multiple Choice Questions")

questions = [
    {
        "question": "1. What should you never share online?",
        "options": ["OTP", "Jokes", "Photos", "Notes"],
        "answer": "OTP"
    },
    {
        "question": "2. SIP stands for:",
        "options": [
            "Safe Internet Plan",
            "Systematic Investment Plan",
            "Secure Income Policy",
            "Savings Interest Plan"
        ],
        "answer": "Systematic Investment Plan"
    },
    {
        "question": "3. Which is a cyber fraud?",
        "options": ["Phishing", "Saving", "Budgeting", "Investing"],
        "answer": "Phishing"
    },
    {
        "question": "4. Why is budgeting important?",
        "options": [
            "To waste money",
            "To plan expenses",
            "To avoid banks",
            "For gaming"
        ],
        "answer": "To plan expenses"
    }
]

user_answers = []

for q in questions:
    st.subheader(q["question"])
    ans = st.radio(
        "Choose one:",
        q["options"],
        key=q["question"]
    )
    user_answers.append((ans, q["answer"]))

# ---------------- MATCH THE COLUMNS ---------------- #

st.header("🔗 Match the Columns")

st.write("Match Column A with the correct option from Column B")

match1 = st.selectbox(
    "Savings Account →",
    ["Select", "Bank", "Fraud", "Investment", "Password"]
)

match2 = st.selectbox(
    "Phishing →",
    ["Select", "Cyber Fraud", "Bank", "Budget", "Savings"]
)

match3 = st.selectbox(
    "SIP →",
    ["Select", "Investment", "Password", "Loan", "Shopping"]
)

match4 = st.selectbox(
    "OTP →",
    ["Select", "Secret Code", "Budget", "Interest", "Tax"]
)

# ---------------- JUMBLED WORDS ---------------- #

st.header("🔀 Unscramble the Financial & Cyber Words")

jumble1 = st.text_input(
    "1. Unscramble: 'GNIVASS'"
)

jumble2 = st.text_input(
    "2. Unscramble: 'GNIHSIHP'"
)

jumble3 = st.text_input(
    "3. Unscramble: 'TEGDUB'"
)

# ---------------- SUBMIT BUTTON ---------------- #

if st.button("Submit Quiz 🚀"):

    # MCQ Score
    for user, correct in user_answers:
        if user == correct:
            score += 1

    # Match the Columns Score
    if match1 == "Bank":
        score += 1

    if match2 == "Cyber Fraud":
        score += 1

    if match3 == "Investment":
        score += 1

    if match4 == "Secret Code":
        score += 1

    # Jumbled Words Score
    if jumble1.strip().upper() == "SAVINGS":
        score += 1

    if jumble2.strip().upper() == "PHISHING":
        score += 1

    if jumble3.strip().upper() == "BUDGET":
        score += 1

    # Final Result
    st.success(f"🎉 Your Total Score: {score}/11")

    if score >= 9:
        st.balloons()
        st.write("Excellent! You are cyber smart and financially aware 😎")

    elif score >= 6:
        st.write("Great work! Keep improving your financial literacy 💡")

    else:
        st.write("Good try! Learn more about cyber safety and smart money habits 🔐")
