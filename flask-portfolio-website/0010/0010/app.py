
import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Muhammad Arif Rubbani Portfolio", layout="wide", initial_sidebar_state="collapsed")



# Initialize session state for navigation and details
if "selected_service" not in st.session_state:
    st.session_state.selected_service = None
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None

# Navigate back to the main Services section
def back_to_services():
    st.session_state.selected_service = None

# Navigate back to the main Projects section
def back_to_projects():
    st.session_state.selected_project = None

# Home Section
def home_section():
    st.markdown("<h1 class='header-title'>HI! I am Muhammad Arif Rubbani</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='header-subtitle'>Python Programmer & Data Analyst</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/imgs/man.png", width=200)
    with col2:
        st.markdown("""
            <div class="image-description">
                Welcome to my digital portfolio! Here’s a bit more about me:
                <ul>
                    <li><strong>Data Analyst</strong> with experience in statistical analysis and visualization.</li>
                    <li><strong>Python Programmer</strong> specializing in data science and machine learning projects.</li>
                    <li>Skilled in transforming data into actionable insights using Python and SQL.</li>
                    <li>Strong passion for solving real-world problems using data-driven solutions.</li>
                </ul>
                Explore my work, and let’s connect to build something amazing together!
            </div>
        """, unsafe_allow_html=True)


# Services Section
def services_section():
    if st.session_state.selected_service is None:
        st.markdown('<h2 class="section-title">What I Do</h2>', unsafe_allow_html=True)
        services = [
            {
                "icon": "📊",
                "title": "Data Analysis and Visualization",
                "description": "Perform data cleaning, preprocessing, and analysis to uncover actionable insights.",
                "details": "\n- Data Cleaning and Preprocessing\n- Advanced Statistical Analysis\n- Interactive Dashboards with Matplotlib and Seaborn\n- Tailored Insights for Business Decisions"
            },
            {
                "icon": "🤖",
                "title": "Machine Learning Model Development",
                "description": "Build predictive and classification models using Scikit-learn and TensorFlow.",
                "details": "\n- Supervised and Unsupervised Learning\n- Model Optimization and Evaluation\n- Expertise in NLP and Deep Learning\n- Scalable Solutions for Real-World Problems"
            },
            {
                "icon": "🔗",
                "title": "ETL and Data Pipeline Development",
                "description": "Design and implement robust ETL pipelines using PySpark and KNIME.",
                "details": "\n- Efficient Data Extraction and Transformation\n- Seamless Integration with APIs\n- Automated Data Workflows\n- Data Consistency and Quality Assurance"
            },
            {
                "icon": "🌐",
                "title": "Web Development and Automation",
                "description": "Create responsive web applications and automate repetitive tasks.",
                "details": "\n- Full-Stack Web Development\n- Automation Scripts for Efficiency\n- Integration with APIs\n- User-Friendly Interfaces"
            },
            {
                "icon": "☁️",
                "title": "Cloud Computing and Deployment",
                "description": "Deploy scalable applications on cloud platforms like AWS and Azure.",
                "details": "\n- Cloud Resource Management\n- CI/CD Pipeline Setup\n- Scalable Deployment Solutions\n- Cost Optimization Techniques"
            },
            {
                "icon": "🔒",
                "title": "Cybersecurity and Data Protection",
                "description": "Ensure the security and integrity of systems and data.",
                "details": "\n- Vulnerability Assessments\n- Encryption and Secure Data Storage\n- Incident Response Plans\n- Compliance with Security Standards"
            },
        ]

        col1, col2, col3 = st.columns(3, gap="large")
        for i, service in enumerate(services):
            with [col1, col2, col3][i % 3]:
                st.markdown(f"<h3>{service['icon']} {service['title']}</h3>", unsafe_allow_html=True)
                st.write(service["description"])
                if st.button(f"View Details ", key=f"service_{i}"):
                    st.session_state.selected_service = service
                    st.rerun()
                st.markdown("<br>", unsafe_allow_html=True)  # Add spacing between services
    else:
        service = st.session_state.selected_service
        st.markdown(f"<h2 class='section-title'>{service['icon']} {service['title']}</h2>", unsafe_allow_html=True)
        st.markdown(service['details'])
        if st.button("Back to Services"):
            back_to_services()
            st.rerun()
            
# Projects Section
def projects_section():
    if st.session_state.selected_project is None:
        st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
        projects = [
            {
                "title": "Diet Plan Recommendation Engine",
                "description": "A recommendation engine for personalized diet plans.",
                "technologies": "Python, Machine Learning",
                "outcome": "Provided users with tailored diet plans based on preferences.",
                "image": "assets/diet_plan.png",
                "details": "This project uses machine learning algorithms to analyze user preferences and recommend customized diet plans for better health and fitness.",
                "download_link": "https://example.com/diet_plan_download",
            },
            {
                "title": "Movie Advisor",
                "description": "A recommendation system based on user's likes and dislikes.",
                "technologies": "Python, Recommendation Systems",
                "outcome": "Enhanced user experience by suggesting movies tailored to preferences.",
                "image": "assets/movie_advisor.jpg",
                "details": "This project analyzes user preferences and viewing history to suggest movies, utilizing collaborative filtering techniques.",
                "download_link": "https://example.com/movie_advisor_download",
            },
            {
                "title": "Sales Performance Dashboard",
                "description": "A dashboard to track sales performance.",
                "technologies": "Tableau, Excel",
                "outcome": "Improved sales insights and operational efficiency.",
                "image": "assets/sales_dashboard.png",
                "details": "This dashboard provides real-time insights into sales trends, revenue streams, and performance metrics, enabling better decision-making.",
                "download_link": "https://example.com/sales_dashboard_download",
            },
            {
                "title": "Image Classification Model",
                "description": "A model for classifying images using deep learning.",
                "technologies": "Python, TensorFlow, Keras",
                "outcome": "Accurately classified images into predefined categories.",
                "image": "assets/image_classification.png",
                "details": "This project leverages deep learning techniques to classify images into various categories with high accuracy, using convolutional neural networks (CNNs).",
                "download_link": "https://example.com/image_classification_download",
            },
        ]


        for i in range(0, len(projects), 2):
            col1, col2 = st.columns(2)
            for j, col in enumerate([col1, col2]):
                if i + j < len(projects):
                    project = projects[i + j]
                    with col:
                        st.image(project["image"],width=200)
                        st.subheader(project["title"])
                        st.write(project["description"])
                        if st.button("View Details", key=f"project_{i+j}"):
                            st.session_state.selected_project = project
                            st.rerun()
    else:
        project = st.session_state.selected_project
        st.markdown(f"<h2 class='section-title'>{project['title']}</h2>", unsafe_allow_html=True)
        st.image(project["image"], width=200)
        st.write(f"**Technologies Used:** {project['technologies']}")
        st.write(f"**Outcome:** {project['outcome']}")
        st.write(project['details'])
        if "download_link" in project:
            st.markdown(f"[Download Project Files]({project['download_link']})", unsafe_allow_html=True)
        if "live_demo" in project:
            st.markdown(project['live_demo'], unsafe_allow_html=True)
        if st.button("Back to Projects"):
            back_to_projects()
            st.rerun()

# About Section
def about_section():
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

    # Create a layout with 2 columns: One for Education and One for Experience
    col1, col2 = st.columns(2)
    
    # Left Column: Education Section
    with col1:
        st.markdown("<h3 class='section-subtitle'>Education</h3>", unsafe_allow_html=True)
        st.markdown("""
            - **Bachelor's in Data Science** • University of Central Punjab, Lahore *(2022 – Present)*  
            - **Intermediate (ICS with Physics)** • PGC, Lahore *(2020 – 2022)*
        """)
    
    # Right Column: Experience Section
    with col2:
        st.markdown("<h3 class='section-subtitle'>Experience</h3>", unsafe_allow_html=True)
        st.markdown("""
            - **Data Analyst** • Freelancing • Lahore *(July 2023 – Present)*  
            - **Data Analyst** • SCBS *(April 2024 – December 2024)*  
            - **Data Scientist** • Prodigy Tech *(October 2024 – Present)*  
            - **Python Tutor** • Freelancing • Lahore *(August 2021 – Present)*  
            - **Python Online Tutor** • NOON Islamic Centre • Peshawar *(November 2021 – February 2023)*  
            - **Python & Scratch Tutor** • Home Tuition • Lahore *(January 2022 – October 2022)*  
        """)

# Skills Section
def skills_section():
    st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

    # In-demand skills with progress bars
    st.markdown("<h3 class='section-subtitle'>In-Demand Skills</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Python**")
        st.progress(0.9)
        st.write("Proficient in Python programming for data analysis, machine learning, and automation.")

        st.write("**Data Science**")
        st.progress(0.85)
        st.write("Experienced in statistical analysis, data visualization, and predictive modeling.")
    with col2:
        st.write("**Machine Learning**")
        st.progress(0.8)
        st.write("Skilled in using machine learning algorithms for data prediction and analysis.")
        
        st.write("**MySQL**")
        st.progress(0.8)
        st.write("Skilled in using MYsql queries to fetch data more swiftly.")
        
        

    st.markdown("<h3 class='section-subtitle'>Other Skills</h3>", unsafe_allow_html=True)
    st.markdown("""
        - **Programming Languages:** Python, C++, Scratch, Java
        - **Tools & Libraries:** Matplotlib, Seaborn, Django, Pandas, Numpy, Scikit-learn, Keras, TensorFlow
        - **Software Development:** Strong OOP concepts, knowledge of design patterns, software development principles
        - **Other Skills:** Microsoft Office, strong analytical and problem-solving skills, good communication skills (written and oral)
    """)



# Pricing Section
def pricing_section():
    st.subheader("Pricing Plans")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Free Plan")
        st.markdown("$0.00/month")
        st.markdown("- 1 Project")
        st.markdown("- 5GB Storage")
        st.markdown("- Basic Support")
        st.button("Sign Up", key="free_plan")

    with col2:
        st.markdown("### Standard Plan")
        st.markdown("$9.99/month")
        st.markdown("- 10 Projects")
        st.markdown("- 50GB Storage")
        st.markdown("- Premium Support")
        st.button("Sign Up", key="standard_plan")

    with col3:
        st.markdown("### Premium Plan")
        st.markdown("$49.99/month")
        st.markdown("- Unlimited Projects")
        st.markdown("- 200GB Storage")
        st.markdown("- 24/7 Support")
        st.button("Sign Up", key="premium_plan")

# Contact Section
def contact_section():
    st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)
    st.write("Feel free to get in touch with me! Fill out the form below and I will get back to you as soon as possible.")

    # Creating a form with Streamlit's native form widget
    with st.form(key="contact_form"):
        # Input fields
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        # Submit button for the form
        submit_button = st.form_submit_button(label="Send Message")

        # Handle the form submission
        if submit_button:
            if name and email and message:
                st.success("Thank you for reaching out! Your message has been sent.")
            else:
                st.error("Please fill in all fields before submitting.")

def footer_section():
    st.markdown("""
    <footer style="text-align: center; margin-top: 50px;">
        <p>Follow me on:</p>
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 10px;">
            <a href="https://www.linkedin.com/in/arifrubbani" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width: 30px; height: 30px;">
            </a>
            <a href="https://github.com/arifrubbani" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" style="width: 30px; height: 30px;">
            </a>
            <a href="https://twitter.com/arifrubbani" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter" style="width: 30px; height: 30px;">
            </a>
        </div>
    </footer>
    """, unsafe_allow_html=True)


# Tab-like Navigation
tabs = st.tabs(["Home", "About", "Projects", "Skills", "Services", "Pricing", "Contact"])
with tabs[0]:
    home_section()
with tabs[1]:
    about_section()
with tabs[2]:
    projects_section()
with tabs[3]:
    skills_section()
with tabs[4]:
    services_section()
with tabs[5]:
    pricing_section()
with tabs[6]:
    contact_section()

footer_section()
