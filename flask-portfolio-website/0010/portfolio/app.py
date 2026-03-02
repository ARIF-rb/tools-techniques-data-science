import streamlit as st

st.set_page_config("Test", layout = "wide")

st.title("Title Test")

st.sidebar.title("Hamza Rizwan")

tab = st.tabs(["Introduction", "Arif Ch", "Form"])
with tab[0]:
    st.header("Intro Page")
    ques1 = st.selectbox("Question 1", ["Introduction", "Arif Ch", "Form"])

with tab[1]:
    st.subheader("Arif Page")
    col = st.columns(2)
    with col[0]:
        st.subheader("Skills")
        st.markdown("""
                    - python

                    - c++
                    """)
        cols = st.columns([1,2])
        with cols[0]:
            st.progress(70)
            st.progress(15)

        with cols[1]:
            ans = st.slider("Slider", min_value= 0, max_value= 100)

    with col[1]:
        st.subheader("Certifications")
        st.markdown("""
                    - dingy dingy

                    - plop plop
                    """)

with tab[2]:

    form = st.form("Form Fill")
    
    
    with form:
        name = st.text_input("Enter Your name")
        email = st.text_input("Enter your Email")
        message = st.text_area("Write your Message", height= 300)
        submit = st.form_submit_button("Submit")

    if submit:
        st.success("Form submmited")