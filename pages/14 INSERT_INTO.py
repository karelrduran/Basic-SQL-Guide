import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("SQL INSERT INTO Statement")
st.markdown("""
The SQL INSERT INTO statement is a fundamental command that allows you to add one or more records to an existing table within a relational database. This command is essential for populating and maintaining your database with relevant data. 
Here's a breakdown of the basic syntax:
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```
Let's break down each component of the above syntax:
```sql
INSERT INTO -- Keyword signifying insertion of a new record.
table_name -- Name of the table where the new record will be inserted.
(column1, column2, column3, ...) -- Optional list of specific columns to insert data into.
VALUES (value1, value2, value3, ...) -- List of data values corresponding to the respective columns.
``` 
""")
st.subheader("Using shorter syntax")
st.markdown("""
You can also use a shorter syntax to insert data into all the table's columns. In this case, you do not need to specify the column names, but you need to ensure that the order and number of the values match the order and number of the columns in the table.
```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```
""")
st.subheader("SQL INSERT INTO Statement examples:")
st.markdown("""
Consider a "Customers" table with columns like CustomerID, CustomerName, ContactName, Address, City, PostalCode, and Country.
#### Inserting a single record
```sql
INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (4, 'Global Spices', 'Neil Sharma', '123 Liberty St.', 'New York', '10005', 'USA');
```
#### Inserting multiple records
```sql
INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (5, 'Sunrise Electronics', 'Maya Patel', '45 Silicon Ave.', 'San Jose', '95113', 'USA'),
       (6, 'Green Valley Textiles', 'Raj Gupta', '78 Market St.', 'Houston', '77002', 'USA'),
       (7, 'Oceanic Imports', 'Anita Singh', '32 Harbor Way', 'Seattle', '98104', 'USA');

```
""")


# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: ORDER BY"):
        st.switch_page("pages/13 ORDER_BY.py")
with col2:
    if st.button("Next: UPDATE"):
        st.switch_page("pages/15 UPDATE.py")
