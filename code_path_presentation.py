import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Title and Intro
st.title("Citizen Development Coding Path: Upskilling Program")
st.subheader("Accelerating Innovation Through Collaboration")
st.write(
    "Welcome to my interactive presentation! In this session, we’ll explore the modules, "
    "skills, and applications of the Coding Path program, and how architects can leverage these "
    "skills to enhance workflows."
)

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to:",
    ["Overview of the Coding Path", "Modules Breakdown", "Applications for Architects", "Pros & Cons", "Impact Charts", "Interactive Feedback", "Q&A"]
)

# Section 1: Overview
if section == "Overview of the Coding Path":
    st.header("Overview of the Coding Path")
    st.write(
        """
        The Coding Path is part of the Citizen Development Upskilling Program at Arcadis. 
        It is designed to teach coding fundamentals, collaborative practices, and tools like GitHub, 
        VSCode, and Streamlit. The focus is on enhancing workflows and driving digital innovation.
        """
    )

# Section 2: Modules Breakdown
elif section == "Modules Breakdown":
    st.header("Modules Breakdown")
    st.write(
        "The program consists of five modules, each focusing on a specific aspect of coding and collaboration:"
    )
    
    with st.expander("Module 1: Coding Fundamentals"):
        st.write(
            """
            - Set up your coding environment (Python, VSCode, Git, GitHub).
            - Learn the basics of coding and how tools interact.
            - Gain foundational productivity skills for coding success.
            """
        )
        
    with st.expander("Module 2: Version Control"):
        st.write(
            """
            - Learn Git and GitHub to manage and collaborate on code.
            - Understand branching, merging, and pull requests.
            - Enhance teamwork and code tracking.
            """
        )

    with st.expander("Module 3: Packages and Environments"):
        st.write(
            """
            - Explore Python packages to simplify workflows.
            - Learn virtual environments for dependency management.
            - Leverage reusable tools like Pandas and Matplotlib.
            """
        )

    with st.expander("Module 4: Guidelines and Guardrails"):
        st.write(
            """
            - Write clean, maintainable, and scalable code.
            - Apply best practices for variable naming, formatting, and readability.
            - Collaborate effectively through code reviews.
            """
        )

    with st.expander("Module 5: Visuals and User Interaction"):
        st.write(
            """
            - Build interactive web apps using Streamlit.
            - Learn how to create user-friendly interfaces.
            - Empower stakeholders to interact with outputs without coding.
            """
        )

# Section 3: Applications for Architects
elif section == "Applications for Architects":
    st.header("Applications for Architects")
    st.write(
        """
        Here’s how architects can apply the skills learned in the Coding Path program:
        """
    )
    
    st.markdown(
        """
        **1. Automating Repetitive Tasks**  
        Use Python scripts to automate tasks like data extraction, reporting, and parameter updates in BIM workflows.
        
        **2. Enhancing Collaboration**  
        Leverage GitHub for version control and team collaboration to manage and share project scripts.
        
        **3. Building Custom Tools**  
        Develop plugins or scripts for Revit, Dynamo, or other BIM tools to solve project-specific challenges.
        
        **4. Data Analysis and Visualization**  
        Process and analyze large datasets from BIM models to inform design decisions and optimize workflows.
        
        **5. Interactive Dashboards**  
        Use Streamlit to present project data in an interactive format for stakeholders.
        """
    )
    
    st.image("https://via.placeholder.com/800x400", caption="Example of Streamlit Dashboard")  # Replace with actual image

# Section 4: Pros & Cons
elif section == "Pros & Cons":
    st.header("Pros & Cons of Following the Coding Path as an Architect")
    st.write(
        "Explore the advantages and disadvantages of following the program, especially as a beginner in coding."
    )
    
    # Pros Section
    st.subheader("Advantages")
    st.write("Check the benefits that resonate with you:")
    pro_1 = st.checkbox("Enhanced skill set and future-proofing")
    pro_2 = st.checkbox("Increased efficiency through automation")
    pro_3 = st.checkbox("Improved collaboration within multidisciplinary teams")
    pro_4 = st.checkbox("Ability to create custom tools tailored to project needs")
    pro_5 = st.checkbox("Professional growth and alignment with digital transformation initiatives")
    
    st.write("Selected advantages:")
    selected_pros = [pro for pro, checked in zip(
        ["Enhanced skill set and future-proofing", 
         "Increased efficiency through automation", 
         "Improved collaboration within multidisciplinary teams", 
         "Ability to create custom tools tailored to project needs", 
         "Professional growth and alignment with digital transformation initiatives"], 
        [pro_1, pro_2, pro_3, pro_4, pro_5]
    ) if checked]
    st.write(selected_pros)
    
    # Cons Section
    st.subheader("Disadvantages")
    st.write("Rate the following challenges from 1 (not a challenge) to 5 (significant challenge):")
    con_1 = st.slider("Steep learning curve for beginners", 1, 5, 3)
    con_2 = st.slider("Time investment needed to balance learning with work", 1, 5, 3)
    con_3 = st.slider("Complexity of tools like Git and GitHub for novices", 1, 5, 3)
    con_4 = st.slider("Abstract nature of best practices for small-scale tasks", 1, 5, 3)
    con_5 = st.slider("Initial productivity dip during the learning phase", 1, 5, 3)
    
    st.write("Your challenge ratings:")
    st.write({
        "Steep learning curve for beginners": con_1,
        "Time investment needed to balance learning with work": con_2,
        "Complexity of tools like Git and GitHub for novices": con_3,
        "Abstract nature of best practices for small-scale tasks": con_4,
        "Initial productivity dip during the learning phase": con_5,
    })

# Section 5: Impact Charts
elif section == "Impact Charts":
    st.header("Impact of Coding Skills on Architectural Work")
    
    # Chart 1: Efficiency Increase
    st.subheader("Efficiency Increase in BIM Projects with Automation")
    efficiency_data = pd.DataFrame({
        'Project Type': ['Without Automation', 'With Automation'],
        'Efficiency (%)': [70, 90]
    })
    fig1, ax1 = plt.subplots()
    ax1.bar(efficiency_data['Project Type'], efficiency_data['Efficiency (%)'], color=['red', 'green'])
    ax1.set_ylabel('Efficiency (%)')
    ax1.set_title('Efficiency in BIM Projects')
    st.pyplot(fig1)
    
    # Chart 2: Earnings Comparison
    st.subheader("Earnings Comparison: Architects with vs. without Coding Skills")
    earnings_data = pd.DataFrame({
        'Category': ['Without Coding Skills', 'With Coding Skills'],
        'Average Salary (USD)': [60000, 80000]
    })
    fig2, ax2 = plt.subplots()
    ax2.bar(earnings_data['Category'], earnings_data['Average Salary (USD)'], color=['blue', 'orange'])
    ax2.set_ylabel('Average Salary (USD)')
    ax2.set_title('Earnings of Architects')
    st.pyplot(fig2)
    
    # Chart 3: Job Opportunities
    st.subheader("Ease of Finding Specialized Jobs")
    job_data = pd.DataFrame({
        'Skill Level': ['Non-coding Architects', 'Coding Architects'],
        'Job Opportunities': [50, 80]
    })
    fig3, ax3 = plt.subplots()
    ax3.bar(job_data['Skill Level'], job_data['Job Opportunities'], color=['purple', 'cyan'])
    ax3.set_ylabel('Job Opportunities')
    ax3.set_title('Specialized Job Market')
    st.pyplot(fig3)

# Section 6: Interactive Feedback
elif section == "Interactive Feedback":
    st.header("Interactive Feedback Section")
    
    st.write("Please rate your overall experience with this presentation:")
    
    # Create a slider for user feedback
    feedback_score = st.slider("Rate your experience", 0, 10, 5)
    st.write(f"Your feedback score: {feedback_score}")
    
    # Collecting feedback data
    feedback_data = pd.DataFrame({
        'Feedback Score': [feedback_score]
    })
    st.write(feedback_data)

    # Display a thank you message
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")

# Section 7: Q&A
elif section == "Q&A":
    st.header("Q&A")
    st.write("If you have any questions, feel free to ask during the session!")
    st.write("You can also provide feedback or share your thoughts below.")
    
    feedback = st.text_area("Your Feedback or Questions:")
    if st.button("Submit"):
        st.write("Thank you for your feedback!")