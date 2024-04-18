import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.markdown("""
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        h1 {
            text-align: center;
        }
    </style>
</head>
</html>
""", unsafe_allow_html=True)
st.title("Welcom to the Basic SQL Guide")
st.markdown("""
Welcome to the SQL Basics Guide. In this guide, we will explore the fundamentals of Structured Query Language (SQL), a powerful tool for working with relational databases. Whether you are interested in application development, data analysis or database administration, understanding SQL is a fundamental skill that will help you work with data efficiently and effectively.
""")

st.subheader("Objectives of this Guide")
st.markdown("""
In this guide, we will focus on providing you with a solid understanding of fundamental SQL concepts. We will explore topics such as SQL processing power, SQL data types, SQL syntax, and the different types of SQL statements, including SELECT, FROM, JOIN, and WHERE statements. Throughout the guide, you will find clear explanations and practical examples to reinforce your understanding.
""")

st.subheader("Guide Structure")
st.markdown("""
The guide is structured in several sections, each dedicated to a specific SQL topic. We will start with a general introduction to SQL and its processing power. Then, we will explore the different SQL data types and the syntax used to write SQL statements. As we progress, we will dive into more advanced details, such as WHERE, GROUP BY and ORDER BY clauses, as well as the different types of JOIN. 

Finally, we will conclude with a practical section 'Do Yourself' where you will be able to put your knowledge into practice by creating your own code by polling the Vivino database, which was acquired by scraping the vivino.com website, also several sample queries are provided which you can run or modify.
""")

st.subheader("How to use this guide?")
st.markdown("""
This guide is designed for beginners with no previous SQL experience. If you are a student, IT professional, developer or data analyst looking to acquire SQL skills, this guide is for you. Each section is presented in a clear and concise manner, with examples to help you understand the concepts presented. We recommend that you follow each section in order and put the knowledge learned into practice.
""")

st.subheader("We're excited to join you on your SQL learning journey!")

st.markdown("""
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        h1 {
            text-align: center;
        }
    </style>
</head>
</html>
""", unsafe_allow_html=True)

st.title("🎈 GET YOUR BALLOONS! 🎈")

# Navigation Section

st.subheader("", divider='rainbow')
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    st.button("Previous:", disabled=True)
with col2:
    if st.button("Next: Introduction to SQL"):
        st.switch_page("pages/01 Introduction_to_SQL.py")
