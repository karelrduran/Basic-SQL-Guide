import streamlit as st

from page_parts.page_configuration import page_configuration
from src.data.data_connection import get_data
from src.data.query_manipulation import QueryManipulation
from src.data.str_manipulation import sql_formating

# Page Configuration

page_configuration()


def reformat_text_area():
    code_input = st.session_state.query_str
    st.session_state.query_str = sql_formating(code_input)


def fill_text_area(code_input: str):
    # code_input = st.session_state.sql_code_example
    st.session_state.query_str = sql_formating(code_input)


# Body Section
with st.expander("Entity Relationship Diagram", expanded=False):
    st.image('assets/images/DER.png', use_column_width=True)

# Query examples
query_manipulation = QueryManipulation()
with st.expander(label="Query examples"):
    col1, col2 = st.columns(2)
    with col1:
        selected_query = st.selectbox("Select query", query_manipulation.queries_description())
    with col2:
        st.code(sql_formating(query_manipulation.get_query(selected_query)), language='sql')
        if st.button("Use"):
            fill_text_area(query_manipulation.get_query(selected_query))

# Try your code
query = st.text_area(key='query_str', label="Try your code:")
if st.button("Execute", on_click=reformat_text_area):
    output_table = get_data(query=query)
    if isinstance(output_table, str):
        st.write(output_table, unsafe_allow_html=True)
    else:
        st.write(output_table)
        st.balloons()

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: Querying Views"):
        st.switch_page("pages/18 Querying_Views.py")
with col2:
    st.button("Next: To be Continue...", disabled=True)
