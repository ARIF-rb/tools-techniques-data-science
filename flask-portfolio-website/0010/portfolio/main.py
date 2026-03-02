import streamlit as st
import base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read()).decode("utf-8")
    return base64_string

# Encode the image
image_base64 = get_base64_image("assets/profile.png")

st.set_page_config(page_title="Hamza Rizwan • Portfolio", page_icon="🤵‍♂️", layout="wide")
st.sidebar.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="data:image/png;base64,{image_base64}" style="width: 200px; border-radius: 50%;">
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("""
# &nbsp;&nbsp;&nbsp;&nbsp; Hamza Rizwan :red[Portfolio]
""", unsafe_allow_html=True)


tab = st.tabs(["Home", "Projects", "Skills", "Certificates", "About Me", "Contact"])


# Home Tab
with tab[0]:
    
    col1,colmid,col2 = st.columns([3,0.2,6])
    
    with col1:
        st.image("assets/profile.png")

    with col2:
        st.markdown("""#""")
        st.header(":red[Hamza Rizwan]")
        st.markdown("""##### _Data Scientist | Data Analyst | Business Intelligence | Machine Learning | Artificial Intelligence_""")
        st.markdown(
            """
            A versatile Data Science student with expertise in data analysis, engineering, business intelligence, AI, and machine learning.
            Proficient in Python, C++, C#, SQL, and various tools like Visual Studio, Anaconda, and KNIME. Experienced in ETL processes, web scraping,
            database management (MySQL, MongoDB), and leveraging Python libraries such as NumPy, Pandas, and Matplotlib. With a strong foundation in
            data-driven decision-making and a passion for innovation, Hamza seeks opportunities in Data Analysis or IT to contribute to organizational
            success. Currently pursuing a Bachelor’s in Data Science at the University of Central Punjab, expected to graduate in 2026.
            """
        )

# Projects Tab
with tab[1]:

    if "selected_project" not in st.session_state:
        st.session_state["selected_project"] = None

    if st.session_state["selected_project"] is None:
        
        st.header(":red[Projects]")
        st.markdown("<hr style='margin-top: 5px; margin-bottom: 5px;'>", unsafe_allow_html=True)

        projects = [
            {
                "title": "Sales Performance Dashboard for Retail Business",
                "description": "Real-time dashboard optimizing sales and operational performance.",
                "technologies": "Databases, KNIME",
                "outcome": "Enabled business interaction with a real-time dashboard.",
                "image": "assets/sales_dashboard.png",
                "details": "A dashboard integrating sales, product, and customer data for real-time insights. It helps businesses track revenue, identify performance trends, and make data-driven decisions.",
                "download_link": "https://drive.google.com/file/d/1mkzH99CCp_4cjjRPAc2Vxb3teIai_KZz/view?usp=drive_link",
            },
            {
                "title": "Online Mart Database Management System",
                "description": "A system to manage and organize data for an online mart.",
                "technologies": "MySQL, Apache, MongoDB, PHP, Perl, ERDplus",
                "outcome": "Efficient management of an online mart database system.",
                "image": "assets/online_mart.png",
                "details": "The system tracks customer orders, payments, shipping details, products, and reviews, enhancing customer experience and inventory management.",
                "download_link": "https://drive.google.com/file/d/17HRvN0BRwgU_GAFj80P6GEMYH7LBFDIO/view?usp=drive_link",
            },
            {
                "title": "Interactive Interface of MentorBot using Figma",
                "description": "A user-friendly and intuitive interface for MentorBot.",
                "technologies": "Figma for UI/UX design",
                "outcome": "A well-designed and interactive frontend that enhances user engagement.",
                "image": "assets/mentorbot_ui.png",
                "details": "A responsive and intuitive interface for MentorBot that provides seamless user experience across multiple devices.",
                "live_demo": """<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450"
                    src="https://embed.figma.com/proto/fG03GosIX41zOJzpue9keX/MentorBot-App-by-Hamza-Rizwan?node-id=0-527&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&embed-host=share"
                    allowfullscreen></iframe>""",
            },
        ]

        cols = st.columns(3)
        for idx, project in enumerate(projects):
            with cols[idx % 3]:
                st.image(project["image"], width=300)
                st.subheader(project["title"])
                st.caption(project["description"])
                if st.button(f"View Details", key=f"btn_{idx}"):
                    st.session_state["selected_project"] = project
                    st.rerun()
                    

    else:
        project = st.session_state["selected_project"]
        st.header(f":red[{project['title']}]")
        st.image(project["image"], width=300)
        st.subheader("Details:")
        st.write(project["details"])
        st.subheader("Technologies Used:")
        st.write(project["technologies"])
        st.subheader("Outcome:")
        st.write(project["outcome"])

        if "download_link" in project:
            st.subheader("Download:")
            st.markdown(
                f"[Download Project Files]({project['download_link']})",
                unsafe_allow_html=True
            )
        elif "live_demo" in project:
            st.subheader("Live Demo:")
            st.markdown(project["live_demo"], unsafe_allow_html=True)

        st.markdown("---")
        if st.button("Back to Projects"):
            st.session_state["selected_project"] = None 
            st.rerun()



#Skills
with tab[2]:
    st.header(":red[Skills]")
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 5px;'>", unsafe_allow_html=True)
    cola1,colmid, cola2 = st.columns([2,1,2])
    with cola1:
        st.subheader(":red[Technical Skills:]")
        st.markdown("""
                    - **Programming:** Visual Studio, Anaconda, C, C++,
                    C#, Python, MySQL, MongoDB, Pentaho,
                    KNIME, ETL, Data Warehousing, Web Scraping

                    - **Python Libraries:** Numpy, Pandas, Matplotlib,
                    BeautifulSoup, Scrapy, Streamlit

                    - **Media:** Adobe Photoshop, Adobe Premiere Pro,
                    Adobe Lightroom, Adobe After Effects, Canva, Figma

                    - **Technical:** Excel, Microsoft Office, Data
                    Analysis, Data Engineering, Database
                    Management, Dropshipping, SEO, Social Media
                    Management, Content Creation, Audience
                    Engagement, Growth Strategy
                    """)
        st.subheader(":red[Skill Set]")

        col1, col2 = st.columns([4, 6])  
        with col1:
            st.write("Programming")
        with col2:
            st.progress(90)


        col1, col2 = st.columns([4, 6])  
        with col1:
            st.write("Media")
        with col2:
            st.progress(70)


        col1, col2 = st.columns([4, 6])  
        with col1:
            st.write("Technical")
        with col2:
            st.progress(95)


        col1, col2 = st.columns([4, 6]) 
        with col1:
            st.write("Soft Skills")
        with col2:
            st.progress(75)


    with cola2:
        st.subheader(":red[Soft Skills:]")
        st.markdown("""
                    - **Communication:** Strong verbal and written skills

                    - **Adaptability:** Flexible in changing environments

                    - **Problem-solving:** Creative and effective solutions

                    - **Quick Learner:** Fast at mastering new concepts

                    - **Teamwork:** Collaborative and supportive

                    - **Time Management:** Efficient and organized

                    - **Emotional Intelligence:** Understanding and
                    managing emotions

                    - **Critical Thinking:** Analyzing and making
                    informed decisions

                    - **Attention to Detail:** Ensuring accuracy and
                    quality

                    - **Professionalism:** The ability to be professional
                    """)


#Certificates
with tab[3]:
    st.header(":red[Certifications, Courses and Training]")
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 5px;'>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader(":red[Programming & Data Science:]")
        st.markdown("""
                    * Microsoft Learn (C# and SQL, 44 Badges with 7 Trophies)
                    * Data Analysis Certificate (Freecodecamp)
                    * Microsoft Foundational C# Certificate
                    * Legacy Python
                    * Fundamentals of Data Science
                    * Tools and Techniques for Data Science
                    * Design and Analysis of Algorithms
                    * Data Structure and Algorithms
                    * Software Engineering
                    * Object-Oriented Programming
                    * Programming Fundamentals
                    """)
    with col2:
        st.subheader(":red[Mathematics & Analytical:]")
        st.markdown("""
                    * Calculus
                    * Linear Algebra
                    * Discrete Structure
                    * Statistics and Probability
                    * Applied Statistics
                    * Logic Thinking
                    """)
    with col3:
        st.subheader(":red[Complementary:]")
        st.markdown("""
                    * **Entrepreneurship:** Knowledge in business strategies, innovation, and managing startups.
                    * **Technical English:** Proficient in technical writing, ensuring clear and effective communication in techfocused environments.
                    * **Psychology:** Understanding human behavior and cognitive processes, enhancing communication and
                    teamwork.
                    """)

#About Me
with tab[4]:
    st.header(":red[About Me]")
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 5px;'>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns([5,3,2])
    with col1:
        st.subheader(":red[Professional Summary]")
        st.write(
            """
            I am a versatile Data Science student skilled in data analysis, data engineering, 
            business intelligence, AI, and Machine Learning. Proficient in Python, C++, C#, SQL, 
            and tools like Visual Studio, Anaconda, and KNIME, I specialize in using Python libraries 
            like Numpy, Pandas, and Matplotlib. With hands-on experience in ETL, data warehousing, 
            web scraping, database management (MySQL, MongoDB), dropshipping, product hunting, and SEO, 
            I combine technical expertise with creativity to deliver actionable insights and drive business growth. 
            
            I seek opportunities in Data Analysis or IT to apply my skills and contribute to organizational success.
            #####
            """
        )

        st.subheader(":red[Hobbies and Interests]")
        st.write(
            """
            * **Hobbies:** Researching about Tech and Dropshipping, PCs, Components, Video Games, Video Editing,
            Boxing.
            * **Interests:** Tech, IT, Dropshipping, Shopify, Product Hunting, Product Marketing, Esports, Football, Boxing,
            MMA.

            """
        )
    with col2:
        st.subheader(":red[Education]")
        st.markdown(
            """
            #### **Bachelor of Data Science** _(2022-2026)_

            _University of Central Punjab, Lahore_ 

                
            #### **Higher Secondary School (HSSC)** _(2020-2022)_

            _Pakistan School and College Mangaf, Kuwait_


            #### **Matriculation (Matric)** _(2018-2020)_

            _Pakistan School and College Mangaf, Kuwait_

                
            #### **Lower Eduction (LKG - 8th Class)** _(2008-2018)_

            _Pakistan School and College Mangaf, Kuwait_
            """
        )
    with col3:
        st.subheader(":red[Languages]")
        st.markdown(
            """
            * English

            * Urdu
                
            * Hindi
              
            * Punjabi
               
            * Arabic
            """
        )


#Contact
with tab[5]:
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Contact Me</h1>", unsafe_allow_html=True)

    
    fm = st.form("Contact Me")
    with fm:
        col1,col2 = st.columns(2)
        with col1:
                name = st.text_input("Your Name",placeholder="   Enter your name")
        with col2:
                email = st.text_input("Your Email", placeholder="   Enter your email")

        message = st.text_area("Your Message",placeholder= "Write your message here",height= 300)

        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            if name and email and message:
                st.success("Thank you for your message! I'll get back to you shortly.")
            else:
                st.error("Please fill in all the fields.")

    st.markdown("""
    <style>
        .stButton>button {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    """, unsafe_allow_html=True)

#Footer
st.markdown("<hr style='margin-top: 5px; margin-bottom: 5px;'>", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Socials</h1>", unsafe_allow_html=True)

col1, colmid, col2 = st.columns(3)

with colmid:
    co1, co2, co3, co4 = st.columns(4)

    # Facebook Button
    with co1:
        st.markdown("""
            <a href="https://www.facebook.com" target="_blank">
                <button style="background-color: #3b5998; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer;">
                    Facebook
                </button>
            </a>
        """, unsafe_allow_html=True)

    # LinkedIn Button
    with co2:
        st.markdown("""
            <a href="https://www.linkedin.com" target="_blank">
                <button style="background-color: #0077b5; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer;">
                    LinkedIn
                </button>
            </a>
        """, unsafe_allow_html=True)

    # Instagram Button
    with co3:
        st.markdown("""
            <a href="https://www.instagram.com" target="_blank">
                <button style="background-color: #e4405f; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer;">
                    Instagram
                </button>
            </a>
        """, unsafe_allow_html=True)

    # Twitter Button
    with co4:
        st.markdown("""
            <a href="https://www.twitter.com" target="_blank">
                <button style="background-color: #1da1f2; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer;">
                    Twitter
                </button>
            </a>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; font-size: 14px; color: gray;">
         Thank you for visiting my portfolio. Feel free to reach out for any opportunities or collaborations!
    </div>
""", unsafe_allow_html=True)
