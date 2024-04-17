import streamlit as st


def page_configuration():
    st.set_page_config(
        page_title="📔 A basic SQL guide for Data Engineers",
        page_icon="📔",
        layout="wide",
        initial_sidebar_state='expanded'
    )

    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

