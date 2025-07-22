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

# Define Arcadis colors
arcadis_orange = "#FF6600"
arcadis_black = "#000000"

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = [
    "🏠 Intro",
    "📚 Modules Overview",
    "⚖️ Pros & Cons",
    "🚀 Benefits for Architects",
    "✅ Coding Path Insights"
]
choice = st.sidebar.radio("Go to", pages)

# Intro Page
if choice == "🏠 Intro":
    st.title("Coding Path for Architects")
    st.subheader("Empowering Architects with Coding Skills")
    st.markdown("""
        Welcome to this interactive presentation! This app showcases the **Coding Path** from the Arcadis Upskilling Program.

        In this presentation, you'll learn:
        - The structure and content of the program.
        - Pros and cons of taking the course.
        - Benefits of coding for architects.
        - Insights into what the program covers and what it doesn’t.

        **Let’s dive in!** Use the sidebar to navigate through the chapters.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Arcadis_Logo.svg/2560px-Arcadis_Logo.svg.png", width=400)

# Modules Overview Page
elif choice == "📚 Modules Overview":
    st.title("📚 Modules Overview")
    st.markdown("Here’s a breakdown of the modules covered in the Coding Path program:")

    modules = {
        "Module 1: Introduction to Programming": [
            "Learn the basics of Python.",
            "Understand variables, loops, and functions.",
            "Introduction to coding platforms like VS Code."
        ],
        "Module 2: Data Handling": [
            "Work with data structures like lists, dictionaries, and dataframes.",
            "Introduction to libraries like Pandas and Numpy.",
            "Learn how to clean and manipulate data."
        ],
        "Module 3: Visualization": [
            "Create charts and graphs using Matplotlib.",
            "Understand how to present data visually.",
            "Learn the principles of effective data storytelling."
        ],
        "Module 4: Collaboration & Environments": [
            "Work with Git and GitHub for version control.",
            "Understand virtual environments and package management.",
            "Collaborate effectively on coding projects."
        ]
    }

    for module, points in modules.items():
        with st.expander(module):
            st.markdown("- " + "\n- ".join(points))

# Pros & Cons Page
elif choice == "⚖️ Pros & Cons":
    st.title("⚖️ Pros & Cons")
    st.markdown("Below are the pros and cons of the Coding Path program:")

    pros = [
        "Gain foundational knowledge of Python and coding.",
        "Learn how to manipulate and visualize data effectively.",
        "Develop skills in collaboration and version control.",
        "Understand virtual environments for better coding practices.",
        "Open new career opportunities with coding skills.",
        "Enhance your problem-solving and logical thinking.",
        "Experience an interactive and hands-on learning approach."
    ]

    cons = [
        "The learning curve may feel steep for beginners.",
        "Some topics may not directly apply to daily architectural work.",
        "Requires consistent practice to retain knowledge.",
        "Focuses more on collaboration and environments than writing code.",
        "Limited integration with architectural design tools.",
        "May require additional effort to apply coding to architecture.",
        "Not tailored specifically for architects' workflows."
    ]

    for i, pro in enumerate(pros):
        st.subheader(f"Pro {i + 1}:")
        st.write(pro)
        st.slider(f"Rate this Pro", 0, 10, 5, key=f"pro_slider_{i}")

    for i, con in enumerate(cons):
        st.subheader(f"Con {i + 1}:")
        st.write(con)
        st.slider(f"Rate this Con", 0, 10, 5, key=f"con_slider_{i}")

# Benefits for Architects Page
elif choice == "�� Benefits for Architects":
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

    benefit_interactivity = {
        "Automate repetitive tasks, saving time and effort.": "See how automation impacts efficiency:",
        "Analyze and manipulate data to inform design decisions.": "Explore data insights:",
        "Create custom tools for architectural workflows.": "Tool customization potential:",
        "Open doors to specialized and well-paying job roles.": "Career potential graph:",
        "Improve project efficiency and collaboration with other disciplines.": "Collaboration benefits:",
        "Stay ahead of the curve in a tech-driven industry.": "Tech-savvy architects are leaders in the future:",
        "Develop a unique skill set that sets you apart from peers.": "Skill set comparison:"
    }

    for benefit, description in benefit_interactivity.items():
        if st.checkbox(benefit):
            st.markdown(description)
            if benefit == "Stay ahead of the curve in a tech-driven industry.":
                st.markdown("""
                    **Graphic: Architects with Coding Skills vs. Architects with Basic BIM Skills**
                    - Architects with **coding skills** 🌟 are equipped to:
                        - Automate workflows.
                        - Use generative design tools.
                        - Analyze and manipulate data.
                    - Architects with **basic BIM skills** 🏗️ rely on predefined tools and workflows.
                    
                    _This graphic shows that coding-skilled architects are more adaptable and versatile in tech-driven environments._
                """)

# Coding Path Insights Page
elif choice == "✅ Coding Path Insights":
    st.title("✅ Coding Path Insights")
    st.markdown("""
        This section provides insights into the Coding Path program. Check the boxes that apply to your experience to evaluate the program's relevance.
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
