import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

# Navigation Section

st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    st.button("Previous:", disabled=True)
with col2:
    if st.button("Next: Introduction to SQL"):
        st.switch_page("pages/01 Introduction_to_SQL.py")
