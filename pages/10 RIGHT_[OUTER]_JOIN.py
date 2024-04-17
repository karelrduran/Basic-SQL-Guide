import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("RIGHT [OUTER] JOIN")
st.markdown("""
Right outer joins (the keyword OUTER is optional) include nonmatching rows only from the table named after the RIGHT [OUTER] JOIN clause. Missing values in a row are filled with nulls. The following sample query creates a right outer join between the PART and PARTSUPP tables:
```sql
SELECT part.pno, pname, qty
FROM part RIGHT OUTER JOIN partsupp
ON part.pno = partsupp.pno
```
The results of this query contains all matched rows, plus nonmatched rows from the PARTSUPP table (or, the table on the right hand side of the RIGHT OUTER JOIN clause). For example, if the PARTSUPP table contained a nonmatching record for a PNO column value of P9, this information would be part of the result. If, however, the PART table also contained an nonmatched record, this record information would not appear in the result rows. Using the RIGHT [OUTER] JOIN syntax includes nonmatched rows from only the joined table on the right of the RIGHT OUTER JOIN clause.

""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: LEFT [OUTER] JOIN"):
        st.switch_page("pages/09 LEFT_[OUTER]_JOIN.py")
with col2:
    if st.button("Next: WHERE"):
        st.switch_page("pages/11 WHERE.py")
