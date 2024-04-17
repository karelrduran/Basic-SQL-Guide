import streamlit as st


from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader('SQL Syntax')
st.markdown("""
SQL syntax refers to the rules and guidelines defining how to correctly write SQL statements. It includes the use of keywords, clauses, operators, and functions that are used to query and manipulate data in a relational database.

The basic syntax of an SQL statement consists of a command followed by a clause and conditions. The most common SQL commands are SELECT, INSERT, UPDATE, DELETE, and CREATE. Each command has its specific syntax and performs a particular task.
""")

st.subheader("SQL Syntax Rules")
st.markdown("""
SQL syntax has a **set of rules** that must be followed for a SQL statement to be valid. Here are some of the most important rules to keep in mind when writing SQL statements:

   * SQL statements always start with the keywords.
   * SQL keywords must be written in uppercase for a better understanding. For example, SELECT, FROM, WHERE, etc.
   * SQL statements must end with a semicolon (;).
   * Table and column names must be written in lowercase; if multiple words are used, they should be separated by an underscore (_) or camelCase.
   * String values must be enclosed in single quotes (' ').
   * Date values must be enclosed in single quotes (' ') and should be in the format 'YYYY-MM-DD'.
   * Numeric values should not be enclosed in quotes.
   * Each clause in a SQL statement should be written on a separate line for better readability.
   * The SELECT clause must come first in a SELECT statement, followed by the FROM clause and other clauses such as WHERE, JOIN, GROUP BY, and ORDER BY.
   * When using the WHERE clause to filter results, the comparison operator must be placed between the column name and the value being compared.
   * When joining tables, the ON clause should specify the relationship between the columns of the two tables.
   * SQL is not case-sensitive, which means the update keyword is the same as the UPDATE
""")

st.subheader("CRUD (Create, Read, Update, Delete)")
st.markdown("""
 SQL supports four fundamental operations, collectively known as CRUD (Create, Read, Update, Delete). They are:
```sql
SELECT  -- Read the data
INSERT  -- Insert new data
UPDATE  -- Update existing data
DELETE  -- Remove data
```
CRUD is an important concept because it gives users total control over their data. It allows them to retrieve, add, update, and remove any data item.
""")

st.subheader('SQL Clause')
st.markdown("""
In SQL (Structured Query Language), a clause is a component of a SQL statement that performs a specific function. For example, the SELECT clause specifies the columns to be retrieved, the WHERE clause specifies a condition to filter rows, and the ORDER BY clause sorts the result set.

On the other hand, an SQL statement is composed of several clauses, each with a specific purpose and syntax. It is a complete command that is executed against a database. An SQL statement can contain one or more clauses, depending on the task performed. For example, a SELECT statement typically includes a SELECT clause, a FROM clause, and possibly others such as WHERE, GROUP BY, HAVING, and ORDER BY.
""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: SQL Data Types"):
        st.switch_page("pages/03 SQL_Data_Types.py")
with col2:
    if st.button("Next: SELECT"):
        st.switch_page("pages/05 SELECT.py")
