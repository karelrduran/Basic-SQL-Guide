import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("FULL [OUTER] JOIN")
st.markdown("""
In contrast to inner joins, outer joins can contain some or all nonmatching rows from both joined tables. Missing values in a row of the result table are filled with nulls. The following sample query creates a full outer join between the LEFT_TABLE and RIGHT_TABLE tables:
```sql
SELECT left_table.id, left_val, right_val
FROM left_table FULL OUTER JOIN right_table
ON left_table.id = right_table.id
```
The results of this full outer join (the keyword OUTER is optional) contain all matched as well as unmatched rows from either table. For example, the LEFT_TABLE table contained nonmatching records with RIGHT_TABLE, this information would be part of the result, even though there is no matching record in the RIGHT_TABLE table. Likewise, the RIGHT_TABLE table contained nonmatching recordS with LEFT_TABLE, this record information would also appear in the result even though there is no matching value in the LEFT_TABLE table.

Using the FULL [OUTER] JOIN syntax includes nonmatched rows from both joined tables. Full outer joins can only use the equal (=) comparison operator in the join condition (left and right outer joins can use all the comparison operators).
""")
st.image('assets/images/full_join1.png')
st.image('assets/images/full_join2.png')

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: RIGHT [OUTER] JOIN"):
        st.switch_page("pages/09 RIGHT_[OUTER]_JOIN.py")
with col2:
    if st.button("Next: WHERE"):
        st.switch_page("pages/11 WHERE.py")
