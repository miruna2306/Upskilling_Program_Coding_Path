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
elif choice == "⚖️ Pros & Cons":
    st.header("Pros & Cons")
    
    # Pros Section
    st.subheader("Advantages")
    st.write("Rate the following benefits from 1 (not beneficial) to 5 (very beneficial):")
    pros = [
        "Gain foundational knowledge of Python and coding.",
        "Learn how to manipulate and visualize data effectively.",
        "Develop skills in collaboration and version control.",
        "Understand virtual environments for better coding practices.",
        "Open new career opportunities with coding skills.",
        "Enhance your problem-solving and logical thinking.",
        "Experience an interactive and hands-on learning approach."
    ]
    pro_ratings = {}
    for i, pro in enumerate(pros):
        pro_ratings[pro] = st.slider(pro, 1, 5, 3)

    st.write("Your benefit ratings:")
    st.write(pro_ratings)
    
    # Cons Section
    st.subheader("Disadvantages")
    st.write("Rate the following challenges from 1 (not a challenge) to 5 (significant challenge):")
    cons = [
        "The learning curve may feel steep for beginners.",
        "Some topics may not directly apply to daily architectural work.",
        "Requires consistent practice to retain knowledge.",
        "Focuses more on collaboration and environments than writing code.",
        "Limited integration with architectural design tools.",
        "May require additional effort to apply coding to architecture.",
        "Not tailored specifically for architects' workflows."
    ]
    con_ratings = {}
    for i, con in enumerate(cons):
        con_ratings[con] = st.slider(con, 1, 5, 3)

    st.write("Your challenge ratings:")
    st.write(con_ratings)

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
            st.markdown(f"**Visualizing the impact of: {benefit}**")
            # Example data visualization can be added here for each benefit
            st.write("Example visualization placeholder...")

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

    checkbox_states = {}
    for insight in insights:
        checkbox_states[insight] = st.checkbox(insight)

    total_checked = sum(checkbox_states.values())
    total_insights = len(insights)
    score = round((total_checked / total_insights) * 100, 2)

    st.markdown(f"### Final Relevance Score: {score}%")
    if score >= 75:
        st.success("The Coding Path program is highly relevant to your needs!")
    elif score >= 50:
        st.warning("The Coding Path program is somewhat relevant, but it has room for improvement.")
    else:
        st.error("The Coding Path program may not meet your needs. Consider additional learning resources.")
