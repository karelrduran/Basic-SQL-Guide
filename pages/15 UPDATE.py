import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("SQL UPDATE Statement")
st.markdown("""
The SQL UPDATE statement updates existing data in a table. Unlike the INSERT statement, which inserts new records into a table, and the DELETE statement, which deletes records, the UPDATE statement modifies existing records without adding or removing rows.
The basic syntax for the SQL UPDATE statement is as follows:
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
Here's a breakdown of the components in the syntax:
```sql
UPDATE -- This command instructs the database to update records.
table_name -- Specifies the target table from which records will be updated.
SET -- Use the "SET" clause to update columns and their new values.
WHERE -- An optional clause that specifies conditions under which records will be updated. If omitted, all records in the table will be updated.
``` 
""")
st.subheader("SQL UPDATE Statement examples:")
st.markdown("""
#### Updating a single record
To update a specific record, combine the UPDATE statement with a WHERE clause that uniquely identifies the record. For example, changing a user's email based on their user ID:
```sql
UPDATE users
SET Email = 'newemail@example.com'
WHERE UserID = 5
LIMIT 1;
```
#### Updating multiple records
The UPDATE statement can modify multiple records simultaneously if they meet a specified condition. For example, to increase the price of products in a particular category by 10%:
```sql
UPDATE Products
SET Price = Price * 1.1
WHERE CategoryID = 3;
```
#### Updating multiple columns:
To update more than one column at a time, separate column/value pairs with commas. For example, to update both the address and phone number of a specific user:
```sql
UPDATE users
SET Address = '123 New Street', Phone = '1234567890'
WHERE UserID = 1
LIMIT 1;
```
""")

st.subheader("Best practices for using SQL UPDATE Statement")
st.markdown("""
    **Always Use a WHERE Clause**: Except in rare cases where you intentionally want to update every record, always include a WHERE clause to limit the scope of your update.
    
    **Incorporate a LIMIT Clause**: It is essential when updating a specific number of records to enhance the precision and safety of your operation.
    
    **Backup Before Bulk Updates**: Before executing an update that affects multiple rows, make sure you have a recent backup or can roll back the changes if necessary.
    
    **Pre-Test with SELECT**: Before performing an update, use a SELECT statement with the same conditions to review which records will be affected. 
""")


# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: INSERT INTO"):
        st.switch_page("pages/14 INSERT_INTO.py")
with col2:
    if st.button("Next: DELETE"):
        st.switch_page("pages/16 DELETE.py")
