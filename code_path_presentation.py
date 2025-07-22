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
        st.subheader(f"Pro {i+1}")
        st.write(pro)
        st.slider("Rate this Pro", 0, 10, 5, key=f"pro_slider_{i}")

    for i, con in enumerate(cons):
        st.subheader(f"Con {i+1}")
        st.write(con)
        st.slider("Rate this Con", 0, 10, 5, key=f"con_slider_{i}")

# Benefits for Architects Page
elif choice == "🚀 Benefits for Architects":
    st.title("🚀 Benefits of Coding for Architects")
    st.markdown("""
        Learning to code can have a significant impact on an architect's career and work efficiency.
        Let's explore how each benefit can be visualized with data to understand its impact better.
        Use the checkboxes to see specific charts related to each benefit.
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
        "Stay ahead of the curve in a tech-driven industry.": "Industry competitiveness:",
        "Develop a unique skill set that sets you apart from peers.": "Skill set comparison:"
    }

    for benefit, description in benefit_interactivity.items():
        if st.checkbox(benefit):
            st.markdown(description)
            if benefit == "Automate repetitive tasks, saving time and effort.":
                st.markdown("**Project Efficiency Before and After Automation**")
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
                st.markdown("**Data Analysis Impact**")
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
                ax.annotate('Significant Growth', xy=(2022, 80), xytext=(2020, 85),
                            arrowprops=dict(facecolor='black', shrink=0.05))
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
            elif benefit == "Improve project efficiency and collaboration with other disciplines.":
                st.markdown("**Collaboration Efficiency**")
                collab_data = pd.DataFrame({
                    "Collaboration Type": ["Traditional", "Tech-Enhanced"],
                    "Efficiency": [65, 88]
                })
                fig, ax = plt.subplots()
                ax.bar(collab_data["Collaboration Type"], collab_data["Efficiency"], color=[arcadis_orange, arcadis_black])
                ax.set_ylabel("Efficiency (%)")
                ax.set_title("Efficiency of Tech-Enhanced Collaboration")
                st.pyplot(fig)
            elif benefit == "Stay ahead of the curve in a tech-driven industry.":
                st.markdown("**Industry Competitiveness**")
                st.markdown("Imagine a graphic here illustrating how tech skills make architects more relevant. For example, a graphic showing an architect upgrading from basic BIM skills to advanced tech skills, showcasing tools like VR/AR, generative design, and data analytics.")
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

    st.markdown("""
        **Next Steps:**
        - **Data Customization:** Adjust the data points and labels in these charts to best fit the specific context of your projects or industry insights.
        - **Interactive Exploration:** Use the checkboxes to dynamically engage and illustrate the benefits to your audience, allowing them to see the potential impact of coding skills in architecture.
        
        These visualizations are a starting point for understanding how coding skills can transform architectural workflows and career paths.
    """)

# New Section: Coding Path Insights
elif choice == "✅ Coding Path Insights":
    st.title("✅ Coding Path Insights")
    st.markdown("""
        This section provides a mixed set of statements about what the Coding Path program covers and what it may not. 
        Use the checkboxes to indicate your agreement or disagreement based on your experience.
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
    for point in insights:
        st.checkbox(point, key=f"insight_{point}")
