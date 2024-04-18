import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("Querying Views")
st.markdown("""
You may query a view just like a table, provided you have SELECT authority on the view. For example, assume that the redparts view was originally defined as follows:
```sql
CREATE VIEW redparts
AS SELECT *
FROM part
WHERE color = 'RED'
```
The following query retrieves a subset of column values from this view (the view itself being a subset of the original PART table):
```sql
SELECT pno, city
FROM redparts
```
The query result appears below:

|pno 	|city  |
|-------|------|
|P1 	|LONDON|
|P4 	|LONDON|
|P6 	|LONDON|

The next example also queries the redparts view:
```sql
SELECT *
FROM redparts
WHERE weight < 15
```
The query results appear below:
|pno 	|pname 	|color 	|weight |city|
|-------|-------|-------|-------|------|
|P1 	|NUT 	|RED 	|12 	|LONDON|
|P4 	|SCREW 	|RED 	|14 	|LONDON|

""")

# Navigation Section
st.subheader("", divider='rainbow')
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: Nested Table Expressions"):
        st.switch_page("pages/17 Nested_Table_Expressions.py")
with col2:
    if st.button("Next: Do Yourself"):
        st.switch_page("pages/19 Do_Yourself.py")
