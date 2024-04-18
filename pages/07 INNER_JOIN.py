import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("INNER JOIN")
st.markdown("""
When a FROM clause contains two or more tables (or views), that FROM clause is said to join the data values appearing in the two or more tables listed. Up to ten table or view names may be listed in a FROM clause, with each object name separated with a comma. The familiar operation of joining two or more tables can be called an inner join. This distinction is made in order to distinguish inner joins syntactically from left, right, and full (outer) joins. For example, the inner join queries below (on the LEFT_TABLE and RIGHT_TABLE tables) produce the same results:
```sql
SELECT left_table.id, left_val, right_val
FROM left_table, right_table
WHERE left_table.id = right_table.id
```
or
```sql
SELECT left_table.id, left_val, right_val
FROM left_table INNER JOIN right_table
ON left_table.id = right_table.id
```
In both of these queries the LEFT_TABLE and RIGHT_TABLE tables are joined on their commonly named ID columns. Notice that the second query explicitly defines this query as an inner join, not an outer join. You can use the key words INNER JOIN in the from clause instead of the traditional comma (the comma still works for an inner join). To be consistent with this syntax, you should also use an ON clause when you explicitly state a join condition (however, the WHERE clause will work).

The results of these inner joins cannot contain any unmatched rows from either table. For example, the LEFT_TABLE table contained two records with the IDs 2 and 4, this information would not be retrieved in either of the previous queries, since there is no matching record in the RIGHT_TABLE table.

""")

st.image('assets/images/inner_join.png')

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: FROM"):
        st.switch_page("pages/06 FROM.py")
with col2:
    if st.button("Next: LEFT [OUTER] JOIN"):
        st.switch_page("pages/08 LEFT_[OUTER]_JOIN.py")
