import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section


st.subheader("LEFT [OUTER] JOIN")
st.markdown("""
Left outer joins (the keyword OUTER is again optional) include nonmatching rows only from the table named before the LEFT [OUTER] JOIN clause. Missing values in a row are filled with nulls. The following sample query creates a left outer join between the LEFT_TABLE and RIGHT_TABLE tables:
```sql
SELECT left_table.id, left_val, right_val
FROM left_table LEFT OUTER JOIN right_table
ON left_table.id = right_table.id
```
The results of this query contains all matched rows, plus unmatched rows from the LEFT_TABLE table (or, the table on the left hand side of the LEFT OUTER JOIN clause). For example, the LEFT_TABLE table containes nonmatching records with RIGHT_TABLE TABLE on ID, this information would be part of the result, even though there is no matching record in the RIGHT_TABLE table. If, however, the RIGHT_TABLE table also contained an unmatched record, this record information would not appear in the result rows. 

Using the LEFT [OUTER] JOIN syntax includes nonmatched rows from only the joined table on the left of the LEFT OUTER JOIN clause.
""")
st.image('assets/images/left_join.png')

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: INNER JOIN"):
        st.switch_page("pages/07 INNER_JOIN.py")
with col2:
    if st.button("Next: RIGHT [OUTER] JOIN"):
        st.switch_page("pages/09 RIGHT_[OUTER]_JOIN.py")
