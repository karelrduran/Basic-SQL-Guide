import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section


st.subheader("LEFT [OUTER] JOIN")
st.markdown("""
Left outer joins (the keyword OUTER is again optional) include nonmatching rows only from the table named before the LEFT [OUTER] JOIN clause. Missing values in a row are filled with nulls. The following sample query creates a left outer join between the PART and PARTSUPP tables:
```sql
SELECT part.pno, pname, qty
FROM part LEFT OUTER JOIN partsupp
ON part.pno = partsupp.pno
```
The results of this query contains all matched rows, plus unmatched rows from the PART table (or, the table on the left hand side of the LEFT OUTER JOIN clause). For example, if the PART table contained a nonmatching record for a WASHER with a PNO column value of P9, this WASHER information would be part of the result, even though there is no matching record in the PARTSUPP table with a PNO column value of P9. If, however, the PARTSUPP table also contained an unmatched record, this record information would not appear in the result rows. Using the LEFT [OUTER] JOIN syntax includes nonmatched rows from only the joined table on the left of the LEFT OUTER JOIN clause.

""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: FULL [OUTER] JOIN"):
        st.switch_page("pages/08 FULL_[OUTER]_JOIN.py")
with col2:
    if st.button("Next: RIGHT [OUTER] JOIN"):
        st.switch_page("pages/10 RIGHT_[OUTER]_JOIN.py")
