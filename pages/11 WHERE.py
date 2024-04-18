import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("WHERE Clause Syntax and Description")
st.markdown("""
Relational databases typically contain many rows of data, with each row constituting a separate record. Most relational database queries retrieve only a portion of the records contained in a table. The WHERE clause qualifies the query command statement to limit the data retrieved to specific rows in the table

The WHERE clause is generally used with a SELECT statement to specify search criteria for retrieving rows of data from a table or group of tables. The WHERE clause can also appear in DELETE and UPDATE command statements.

The optional WHERE clause sets conditions that each record must meet before that record is retrieved by a query. If the SELECT command statement does not include a WHERE clause, every row in the table or tables queried appears in the result.

A predicate states selection criteria that is applied to each row of data values in the table being queried by the SELECT statement. If the data in a particular record matches the selection criteria, then that record is retrieved by the query, otherwise the record is passed over. See Predicates for more information.

WHERE clause selection criteria may include nested subqueries or may connect two or more tables together in a join condition.

The WHERE clause format appears below:
```sql
WHERE search-condition
```
Parameters:
```sql
search-condition -- Specifies a predicate (or one or more predicates connected with the AND, OR, or NOT operators).
``` 

""")

# Navigation Section
st.subheader("", divider='rainbow')
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: FULL [OUTER] JOIN"):
        st.switch_page("pages/10 FULL_[OUTER]_JOIN.py")
with col2:
    if st.button("Next: GROUP BY"):
        st.switch_page("pages/12 GROUP_BY.py")
