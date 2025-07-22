import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Set Page Config
st.set_page_config(
    page_title="Coding Path for Architects",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define Arcadis brand colors
arcadis_orange = "#FF6600"
arcadis_black = "#000000"

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = [
    "🏠 Overview",
    "📚 Modules Breakdown",
    "⚖️ Pros & Cons",
    "🚀 Benefits for Architects",
    "✅ Coding Path Insights"
]
choice = st.sidebar.radio("Go to", pages)

# Overview Page
if choice == "🏠 Overview":
    st.title("Citizen Development Code Path: Upskilling Program")
    st.subheader("Accelerating Innovation Through Collaboration")
    st.markdown("""
        Welcome to the interactive presentation! In this session, we’ll explore the modules, skills, 
        and applications of the Coding Path program, and how architects can leverage these skills 
        to enhance workflows.

        The Coding Path is part of the Citizen Development Upskilling Program at Arcadis. 
        It is designed to teach coding fundamentals, collaborative practices, and tools like GitHub, 
        VSCode, and Streamlit. The focus is on enhancing workflows and driving digital innovation.

        **Let’s dive in!** Use the sidebar to navigate through the chapters.
    """)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Arcadis_Logo.svg/2560px-Arcadis_Logo.svg.png",
        width=400
    )

# Modules Breakdown Page
elif choice == "📚 Modules Breakdown":
    st.header("Modules Breakdown")
    st.write("The program consists of five modules, each focusing on a specific aspect of coding and collaboration:")
    
    with st.expander("Module 1: Coding Fundamentals"):
        st.write("""
            - Set up your coding environment (Python, VSCode, Git, GitHub).
            - Learn the basics of coding and how tools interact.
            - Gain foundational productivity skills for coding success.
        """)

    with st.expander("Module 2: Version Control"):
        st.write("""
            - Learn Git and GitHub to manage and collaborate on code.
            - Understand branching, merging, and pull requests.
            - Enhance teamwork and code tracking.
        """)

    with st.expander("Module 3: Packages and Environments"):
        st.write("""
            - Explore Python packages to simplify workflows.
            - Learn virtual environments for dependency management.
            - Leverage reusable tools like Pandas and Matplotlib.
        """)

    with st.expander("Module 4: Guidelines and Guardrails"):
        st.write("""
            - Write clean, maintainable, and scalable code.
            - Apply best practices for variable naming, formatting, and readability.
            - Collaborate effectively through code reviews.
        """)

    with st.expander("Module 5: Visuals and User Interaction"):
        st.write("""
            - Build interactive web apps using Streamlit.
            - Learn how to create user-friendly interfaces.
            - Empower stakeholders to interact with outputs without coding.
        """)

# Pros & Cons Page
# Pros Section
st.subheader("Advantages")
st.write("Rate the following benefits from 1 (not beneficial) to 5 (very beneficial):")
pro_1 = st.slider("Gain foundational knowledge of Python and coding", 1, 5, 3)
pro_2 = st.slider("Learn how to manipulate and visualize data effectively", 1, 5, 3)
pro_3 = st.slider("Develop skills in collaboration and version control", 1, 5, 3)
pro_4 = st.slider("Understand virtual environments for better coding practices", 1, 5, 3)
pro_5 = st.slider("Open new career opportunities with coding skills", 1, 5, 3)
pro_6 = st.slider("Enhance your problem-solving and logical thinking", 1, 5, 3)
pro_7 = st.slider("Experience an interactive and hands-on learning approach", 1, 5, 3)

st.write("Your benefit ratings:")
st.write({
    "Gain foundational knowledge of Python and coding": pro_1,
    "Learn how to manipulate and visualize data effectively": pro_2,
    "Develop skills in collaboration and version control": pro_3,
    "Understand virtual environments for better coding practices": pro_4,
    "Open new career opportunities with coding skills": pro_5,
    "Enhance your problem-solving and logical thinking": pro_6,
    "Experience an interactive and hands-on learning approach": pro_7,
})

# Cons Section
st.subheader("Disadvantages")
st.write("Rate the following challenges from 1 (not a challenge) to 5 (significant challenge):")
con_1 = st.slider("The learning curve may feel steep for beginners", 1, 5, 3)
con_2 = st.slider("Some topics may not directly apply to daily architectural work", 1, 5, 3)
con_3 = st.slider("Requires consistent practice to retain knowledge", 1, 5, 3)
con_4 = st.slider("Focuses more on collaboration and environments than writing code", 1, 5, 3)
con_5 = st.slider("Limited integration with architectural design tools", 1, 5, 3)
con_6 = st.slider("May require additional effort to apply coding to architecture", 1, 5, 3)
con_7 = st.slider("Not tailored specifically for architects' workflows", 1, 5, 3)

st.write("Your challenge ratings:")
st.write({
    "The learning curve may feel steep for beginners": con_1,
    "Some topics may not directly apply to daily architectural work": con_2,
    "Requires consistent practice to retain knowledge": con_3,
    "Focuses more on collaboration and environments than writing code": con_4,
    "Limited integration with architectural design tools": con_5,
    "May require additional effort to apply coding to architecture": con_6,
    "Not tailored specifically for architects' workflows": con_7,

    # Interactive sliders for each pro and con
    for i, pro in enumerate(pros):
        st.subheader(f"Pro {i + 1}:")
        st.write(pro)
        st.slider(f"Rate this Pro", 0, 10, 5, key=f"pro_slider_{i}")

    for i, con in enumerate(cons):
        st.subheader(f"Con {i + 1}:")
        st.write(con)
        st.slider(f"Rate this Con", 0, 10, 5, key=f"con_slider_{i}")

# Benefits for Architects Page
elif choice == "🚀 Benefits for Architects":
    st.title("🚀 Benefits of Coding for Architects")
    st.markdown("""
        Learning to code can have a significant impact on an architect's career and work efficiency.
        Let's explore how each benefit can be visualized with data to understand its impact better.
        Use the checkboxes to see specific charts or graphics related to each benefit.
    """)

    benefits = [
        "Automate repetitive tasks, saving time and effort.",
        "Analyze and manipulate data to inform design decisions.",
        "Create custom tools for architectural workflows.",
        "Open doors to specialized and well-paying job roles.",
        "Improve project efficiency and collaboration with other disciplines.",
        "Stay ahead of the curve in a tech-driven industry.",
        "Develop a unique skill set that sets you apart from peers."
    ]

    for benefit in benefits:
        if st.checkbox(benefit):
            if benefit == "Automate repetitive tasks, saving time and effort.":
                st.markdown("**Impact of Automation on Efficiency**")
                data = pd.DataFrame({
                    "Scenario": ["Manual Workflow", "Automated Workflow"],
                    "Efficiency": [50, 85]
                })
                fig, ax = plt.subplots()
                ax.bar(data["Scenario"], data["Efficiency"], color=[arcadis_orange, arcadis_black])
                ax.set_ylabel("Efficiency (%)")
                ax.set_title("Impact of Automation on Efficiency")
                st.pyplot(fig)

            elif benefit == "Analyze and manipulate data to inform design decisions.":
                st.markdown("**Accuracy Increase with Data Analysis**")
                labels = ["Traditional Analysis", "Data-Driven Analysis"]
                sizes = [30, 70]
                fig, ax = plt.subplots()
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=[arcadis_black, arcadis_orange])
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                ax.set_title("Accuracy Increase with Data Analysis")
                st.pyplot(fig)

            elif benefit == "Create custom tools for architectural workflows.":
                st.markdown("**Adoption of Custom Tools Over Time**")
                years = np.arange(2018, 2024)
                adoption_rates = [30, 45, 60, 70, 80, 90]
                fig, ax = plt.subplots()
                ax.plot(years, adoption_rates, marker='o', color=arcadis_orange)
                ax.set_xlabel("Year")
                ax.set_ylabel("Adoption Rate (%)")
                ax.set_title("Growth in Custom Tool Adoption in Architectural Projects")
                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
                st.pyplot(fig)

            elif benefit == "Stay ahead of the curve in a tech-driven industry.":
                st.markdown("**Relevance Growth of Architects with Coding Skills**")
                years = np.arange(2020, 2030)
                relevance_coding = [50, 60, 70, 80, 90, 95, 97, 98, 99, 100]
                relevance_bim = [50, 55, 60, 62, 63, 64, 64, 64, 64, 64]
                fig, ax = plt.subplots()
                ax.plot(years, relevance_coding, label="Architects with Coding Skills", color=arcadis_orange, marker='o')
                ax.plot(years, relevance_bim, label="Architects with Basic BIM Skills", color=arcadis_black, marker='x')
                ax.set_xlabel("Year")
                ax.set_ylabel("Relevance in Tech-Driven Industry (%)")
                ax.set_title("Relevance Growth: Coding Skills vs. Basic BIM Skills")
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

            elif benefit == "Open doors to specialized and well-paying job roles.":
                st.markdown("**Salary Comparison**")
                salary_data = pd.DataFrame({
                    "Role": ["Architect (No Coding Skills)", "Architect (With Coding Skills)"],
                    "Average Salary": [55000, 75000]
                })
                fig, ax = plt.subplots()
                ax.bar(salary_data["Role"], salary_data["Average Salary"], color=[arcadis_orange, arcadis_black])
                ax.set_ylabel("Average Salary (USD)")
                ax.set_title("Salary Comparison")
                st.pyplot(fig)

            elif benefit == "Develop a unique skill set that sets you apart from peers.":
                st.markdown("**Skill Set Distinction**")
                skill_data = pd.DataFrame({
                    "Skill Level": ["Standard", "Advanced"],
                    "Distinction Score": [75, 95]
                })
                fig, ax = plt.subplots()
                ax.bar(skill_data["Skill Level"], skill_data["Distinction Score"], color=[arcadis_orange, arcadis_black])
                ax.set_ylabel("Distinction Score")
                ax.set_title("Skill Set Distinction Levels")
                st.pyplot(fig)

# Coding Path Insights Page
elif choice == "✅ Coding Path Insights":
    st.title("✅ Coding Path Insights")
    st.markdown("""
        This section provides insights into the Coding Path program.
        Check the boxes that apply to your experience to evaluate the program's relevance.
    """)

    insights = [
        "Teaches the basics of Python programming.",
        "Covers integration with architectural design tools like Revit or AutoCAD.",
        "Focuses on data cleaning and manipulation with Pandas.",
        "Introduces creating parametric models using coding.",
        "Demonstrates creating visualizations using Matplotlib.",
        "Emphasizes collaboration using Git and GitHub.",
        "Lacks in-depth knowledge of advanced Python libraries (e.g., TensorFlow, PyTorch).",
        "Teaches best practices for coding workflows.",
        "Doesn't fully automate architectural workflows end-to-end.",
        "Offers insights into setting up virtual environments for projects.",
        "May not cover specific applications of coding for architectural analysis."
    ]

    # Checkbox interaction
    checkbox_states = []
    for point in insights:
        checked = st.checkbox(point, key=f"insight_{point}")
        checkbox_states.append(checked)

    # Calculate final score
    total_checked = sum(checkbox_states)
    total_insights = len(insights)
    score = round((total_checked / total_insights) * 100, 2)

    # Provide feedback based on score
    st.markdown(f"### Final Relevance Score: {score}%")
    if score >= 75:
        st.success("The Coding Path program is highly relevant to your needs!")
    elif score >= 50:
        st.warning("The Coding Path program is somewhat relevant, but it has room for improvement.")
    else:
        st.error("The Coding Path program may not meet your needs. Consider additional learning resources.")
