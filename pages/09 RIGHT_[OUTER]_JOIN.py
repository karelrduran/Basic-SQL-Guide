import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("RIGHT [OUTER] JOIN")
st.markdown("""
Right outer joins (the keyword OUTER is optional) include nonmatching rows only from the table named after the RIGHT [OUTER] JOIN clause. Missing values in a row are filled with nulls. The following sample query creates a right outer join between the LEFT_TABLE and RUGHT_TABLE tables:
```sql
SELECT left_table.id, left_val, right_val
FROM left_table RIGHT OUTER JOIN right_table
ON left_table.id = right_table.id
```
The results of this query contains all matched rows, plus nonmatched rows from the RIGHT_TABLE table (or, the table on the right hand side of the RIGHT OUTER JOIN clause). For example, the RIGHT_TABLE table contained nonmatching records with LEFT_TABLE table on ID, this information would be part of the result. If, however, the LEFT_TABLE table also contained an nonmatched record, this record information would not appear in the result rows. 

Using the RIGHT [OUTER] JOIN syntax includes nonmatched rows from only the joined table on the right of the RIGHT OUTER JOIN clause.

""")
st.image('assets/images/right_join.png')

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: LEFT [OUTER] JOIN"):
        st.switch_page("pages/08 LEFT_[OUTER]_JOIN.py")
with col2:
    if st.button("Next: FULL [OUTER] JOIN"):
        st.switch_page("pages/10 FULL_[OUTER]_JOIN.py")
