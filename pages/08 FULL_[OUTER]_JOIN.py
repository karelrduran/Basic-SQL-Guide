import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("FULL [OUTER] JOIN")
st.markdown("""
In contrast to inner joins, outer joins can contain some or all nonmatching rows from both joined tables. Missing values in a row of the result table are filled with nulls. The following sample query creates a full outer join between the PART and PARTSUPP tables:
```sql
SELECT part.pno, pname, qty
FROM part FULL OUTER JOIN partsupp
ON part.pno = partsupp.pno
```
The results of this full outer join (the keyword OUTER is optional) contain all matched as well as unmatched rows from either table. For example, if the PART table contained a nonmatching record for a RIVET with a PNO column value of P8, this RIVET information would be part of the result, even though there is no matching record in the PARTSUPP table (with a PNO column value of P8). Likewise, if the PARTSUPP table contained a nonmatching record with a PNO column value of P7, this record information would also appear in the result even though there is no matching P7 PNO column value in the PART table.

Using the FULL [OUTER] JOIN syntax includes nonmatched rows from both joined tables. Full outer joins can only use the equal (=) comparison operator in the join condition (left and right outer joins can use all the comparison operators).
""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: INNER JOIN"):
        st.switch_page("pages/07 INNER_JOIN.py")
with col2:
    if st.button("Next: LEFT [OUTER] JOIN"):
        st.switch_page("pages/09 LEFT_[OUTER]_JOIN.py")
