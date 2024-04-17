import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("SQL DELETE Statement")
st.markdown("""
The DELETE statement deletes existing records from the database table. This statement is essential for database maintenance, as it allows you to clean out old, unnecessary, or incorrect data while maintaining the integrity and relevance of your database.
The basic structure for the SQL DELETE statement is as follows:
```sql
DELETE FROM table_name WHERE condition;
```
Here's a breakdown of the components in the syntax:
```sql
DELETE -- This command instructs the database to remove records.
table_name -- Specifies the target table from which records will be deleted.
WHERE -- An optional clause that specifies conditions for deleting records. If omitted, all records in the table will be deleted. 
```
""")

st.subheader("SQL DELETE Statement examples:")
st.markdown("""
#### Deleting specific records
To delete records based on a condition, use DELETE with WHERE. For example, deleting a user from the Users table using a unique ID:
```sql
DELETE FROM Users WHERE UserID = 101 LIMIT 1;
```
#### Deleting multiple records
```sql
DELETE FROM Products WHERE Status = "Discontinued";
```
The above statement deletes all records from the Products table with a Status column value of "Discontinued", indicating that the product is no longer available.

### Best practices for using the DELETE statement

- Always Use a WHERE Clause: Be specific about which records to delete to avoid accidental data loss.
- Incorporate a LIMIT Clause: It is essential when deleting a specific number of records to enhance the precision and safety of your operation.
- Backup Before Bulk Deletions: Ensure you have a recent database backup before executing a DELETE operation that affects multiple rows. This precaution allows you to restore data if necessary.
- Use Transactions: If your database supports transactions, use them when performing DELETE operations. This way, you can roll back the transaction if something goes wrong, ensuring data integrity.
- Pre-Test with SELECT: Before executing a DELETE statement, use a SELECT statement with the same conditions to review which records will be affected. This step helps to prevent unintended deletions
""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: UPDATE"):
        st.switch_page("pages/15 UPDATE.py")
with col2:
    if st.button("Next: Nested Table Expressions"):
        st.switch_page("pages/17 Nested_Table_Expressions.py")
