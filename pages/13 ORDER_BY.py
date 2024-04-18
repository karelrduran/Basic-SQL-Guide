import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("SQL ORDER BY Clause")
st.markdown("""
SQL ORDER BY clause is crucial for sorting query results in ascending or descending order using one or more columns. It is essential in data analysis and reporting, allowing users to organize data in a meaningful sequence. This tutorial will guide you through the syntax, usage, and practical examples of the ORDER BY clause, helping you to enhance your data retrieval processes.
The SQL ORDER BY clause sorts a query's results in a specific order. It arranges the result set in ascending or descending order using one or more columns. The sorting can be performed on one or multiple columns, which provides flexibility in presenting the results. The ORDER BY clause is usually used with the SELECT statement to retrieve and sort specific data from a database table.
The syntax of the ORDER BY clause is as follows:
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 ASC|DESC, column2 ASC|DESC, ...;
```
Here's a breakdown of the components in the syntax:
```sql
SELECT column1, column2, ... -- Specifies the columns you want to retrieve.
FROM table_name -- Specifies the table from which you want to retrieve data.
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ... -- Orders the results by the specified columns. You can use ASC for ascending order (default) or DESC for descending order. 
```
""")

st.subheader("SQL ORDER BY Clause examples:")
st.markdown("""
Suppose you have a table named Users, and you want to sort the results by the LastName column in ascending order:
#### Sorting results in ascending order
```sql
SELECT FirstName, LastName
FROM Users
ORDER BY LastName ASC;
```
This above query selects all users' first and last names, sorting the results by last name in ascending order.
#### Sorting results in descending order
To sort the same Users table by the RegDate column in descending order:
```sql
SELECT FirstName, LastName, RegDate
FROM Users
ORDER BY RegDate DESC;
```
In the above SQL, Users will be listed in descending order based on their registration date, starting with the most recent.
#### Sorting by multiple columns
You can also sort using multiple columns. For example, to sort the Users table first by LastName in ascending order and then by FirstName in ascending order:
```sql
SELECT FirstName, LastName
FROM Users
ORDER BY LastName ASC, FirstName ASC;
```
The above SQL sorts users by their last names; if multiple users have the same last name, their first names are used as a secondary sorting criterion.
""")

st.subheader("Best practices and considerations")
st.markdown("""
**Multiple Columns**: When sorting using various columns, the columns listed first are given precedence. Plan your query accordingly.

**Use Column Aliases**: If you use functions or expressions in your SELECT statement, it's a good idea to sort by these aliases in the ORDER BY clause.

**Performance Impacts**: Sorting can be resource-intensive, especially for large datasets. To improve performance, always make sure your database is properly indexed.

**Sorting Null Values**: By default, SQL places NULL values at the end of the result set for an ascending order sort and at the beginning for a descending order. You can use IS NULL or IS NOT NULL in a WHERE clause to filter these values if needed. 
""")

# Navigation Section
st.subheader("", divider='rainbow')
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: GROUP BY"):
        st.switch_page("pages/12 GROUP_BY.py")
with col2:
    if st.button("Next: INSERT INTO"):
        st.switch_page("pages/14 INSERT_INTO.py")
