import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("INNER JOIN")
st.markdown("""
When a FROM clause contains two or more tables (or views), that FROM clause is said to join the data values appearing in the two or more tables listed. Up to ten table or view names may be listed in a FROM clause, with each object name separated with a comma. The familiar operation of joining two or more tables can be called an inner join. This distinction is made in order to distinguish inner joins syntactically from left, right, and full (outer) joins. For example, the inner join queries below (on the PART and PARTSUPP tables) produce the same results:
```sql
SELECT part.pno, pname, qty
FROM part, partsupp
WHERE part.pno = partsupp.pno
```
or
```sql
SELECT part.pno, pname, qty
FROM part INNER JOIN partsupp
ON part.pno = partsupp.pno
```
In both of these queries the PART and PARTSUPP tables are joined on their commonly named PNO columns. Notice that the second query explicitly defines this query as an inner join, not an outer join. You can use the key words INNER JOIN in the from clause instead of the traditional comma (the comma still works for an inner join). To be consistent with this syntax, you should also use an ON clause when you explicitly state a join condition (however, the WHERE clause will work).

The results of these inner joins cannot contain any unmatched rows from either table. For example, if the PART table contained a record for a RIVET with a PNO column value of P8, this RIVET information would not be retrieved in either of the previous queries, since there is no matching record in the partsupp table with a PNO column value of P8.

""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: FROM"):
        st.switch_page("pages/06 FROM.py")
with col2:
    if st.button("Next: FULL [OUTER] JOIN"):
        st.switch_page("pages/08 FULL_[OUTER]_JOIN.py")
