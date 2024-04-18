import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("Nested Table Expressions")
st.markdown("""
An operand of a join can be more complex than the name of a single table or view. A subselect can be used as a complex operand in the FROM clause. Such an operand is called a nested table expression. Suppose we wanted to join the result of the last sample query with the SUBPART table, which includes a column named SUBPART (containing data similar to the commonly named PNO columns in the PART and PARTSUPP tables). The SUBPART table contains several rows with part numbers (SUBPART column) values that do not appear in either the PART or PARTSUPP tables.

The following sample query joins the SUBPART table with the result of the outer join of the PART and PARTSUPP table (three way join), displaying the nonmatching part number values from SUBPART in the result:
```sql
SELECT product, VALUE(subpart.subpart, partnum) AS partnum, pname, subpart.qty
FROM subpart LEFT JOIN
(SELECT VALUE(part.pno, partsupp.pno) AS
partnum,pname, subpart.qty
FROM part FULL OUTER JOIN partsupp
ON part.pno = partsupp.pno) AS temp
ON subpart.subpart = partnum
```
In this example, the correlation name is temp. The optional keyword AS is useful as an eye catcher for the correlation name that follows.

The following restrictions on nested table expressions apply:

    - Must be enclosed in parentheses
    - Must have a correlation name. In our example, the correlation name is temp.
""")

# Navigation Section
st.subheader("", divider='rainbow')
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: DELETE"):
        st.switch_page("pages/16 DELETE.py")
with col2:
    if st.button("Next: Querying Views"):
        st.switch_page("pages/18 Querying_Views.py")
