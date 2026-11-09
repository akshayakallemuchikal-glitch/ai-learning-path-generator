import streamlit as st

st.set_page_config(page_title="AI Learning Path Generator", page_icon="🚀")

# Your Logo
st.image("https://res.cloudinary.com/ocfbdfvp/image/upload/v1794119832/1000043551.png", width=180)

st.title("🚀 AI Learning Path Generator")
st.write("Enter any skill and get a complete day-wise learning plan. Built by me.")

# Inputs
skill = st.text_input("What do you want to learn?", placeholder="e.g. Python, UI Design, Digital Marketing")
level = st.selectbox("Your Level", ["Beginner", "Intermediate", "Advanced"])
days = st.selectbox("How many days?", [7, 30, 90])
hours = st.slider("Hours per day", 1, 5, 2)

if st.button("Generate My Learning Path ✨"):
    if not skill:
        st.warning("Please enter a skill first!")
    else:
        st.success(f"Your {days}-Day Plan to Master {skill} ({level})")
        st.write(f"⏰ Plan: {hours} hours/day | Level: {level}")

        if days == 7:
            plan = [
                ("Day 1", f"Basics of {skill} - What it is, why it matters, setup tools"),
                ("Day 2", f"Core Concepts of {skill} - Learn top 5 fundamentals"),
                ("Day 3", f"Hands-on Practice - 3 small exercises in {skill}"),
                ("Day 4", f"Intermediate Topics - Deep dive + watch 2 tutorials"),
                ("Day 5", f"Build Mini Project 1 in {skill}"),
                ("Day 6", f"Build Mini Project 2 + Fix mistakes"),
                ("Day 7", f"Revision + Build Portfolio Project + Share on LinkedIn"),
            ]
        elif days == 30:
            plan = [
                ("Week 1: Foundation", f"Basics, setup, core concepts of {skill}. Daily practice {hours} hrs."),
                ("Week 2: Core Skills", f"Top 10 topics in {skill}. Build 3 small projects."),
                ("Week 3: Advanced", f"Advanced concepts, best practices, real-world use cases."),
                ("Week 4: Portfolio", f"Build 2 big projects, create GitHub repo, post on LinkedIn."),
            ]
        else:
            plan = [
                ("Month 1: Foundation", f"Master basics of {skill} from zero."),
                ("Month 2: Intermediate", f"Projects, problem solving, deep concepts."),
                ("Month 3: Advanced + Job Ready", f"Advanced projects, interview prep, portfolio + LinkedIn."),
            ]

        for title, desc in plan:
            with st.expander(title):
                st.write(desc)
                st.checkbox(f"Mark as done - {title}", key=title)

        st.balloons()
        st.info("Tip: Save this page and tick off each day as you complete it!")

st.markdown("---")
st.write("Made with ❤️ using Streamlit")
