import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("SELECT Clause Syntax and Description")
st.markdown("""
Each SQL query statement must contain both a SELECT and a FROM clause. The combination of these two clauses determine the table columns that are searched by the query. The WHERE clause and other advanced clauses further limit data retrieval to specific table rows. The sample queries presented throughout this reference utilize the training tables contained in the TUTORIAL location. See FROM Clause, WHERE Clause, Other Clauses, and XDB Server Tutorial Location for more information.

The SELECT clause specifies the columns from which data values are to be retrieved by the query. Data retrieval is limited to the columns specified. When selecting from two or more tables having duplicate column names, it may be necessary to qualify column names with table or view names. Prefixing column names with a table or view name ensures that the query retrieves the correct column (in the correct table).

The SELECT clause format appears below:
```sql
SELECT [ALL | DISTINCT] {* | projection-list[,...]}
``` 
projection-list: 
```sql
{ 
    expression [[AS] name] | (CASE-statement) AS name | 
    {table-name | view-name | correlation-name}.* 
}
```
CASE-statement: 
```sql
(CASE WHEN condition THEN expression [WHEN condition THEN expression] [...]
    ELSE expression END) AS name
```
""")
st.markdown("""
Parameters:
```sql
ALL         -- Option (default) which selects all rows that satisfy the WHERE condition. Duplicates are not eliminated.

DISTINCT    -- Option that eliminates duplicate rows from the result.

*           -- Represents a list of names that identify the columns of the final result table. The first name in the list identifies the first column, the second name 
            -- identifies the second column, and so on. To retrieve all columns in a table or view, enter a single asterisk in place of projection-list.
            
expression  -- A list of one to 750 column names (separated by commas) and possibly including constants, functions, host-variables, special registers, 
            -- labeled durations and various operators. If duplicate column names from different tables must appear in the list, prefix the column name in 
            -- the SELECT clause with that column's table name to resolve any ambiguity. To force the use of an index on a particular column during a query, 
            -- append an asterisk enclosed in parentheses (*) to the name of the indexed column. 
            
AS          -- Can be used to name result columns in a SELECT clause. This is particularly useful for a column derived from an expression or from a function applied 
            -- to a column value. You can use the name in a GROUP BY clause.

            /* The name of a result column of a subselect is determined as follows:

                * If the AS clause is specified, the name of the result column is the name specified on the AS clause.
                * If the AS clause is not specified and the result column is derived from a column name, the result column name is the unqualified name of that column.
                * All other result columns are unnamed.
            */
            
CASE-statement -- XDB Mode only. Allows an item to be conditionally specified in the projection list. For example the CASE statement,

            SELECT (CASE
              WHEN A=2
                THEN FIRST_NAME
              ELSE
                LAST_NAME
              END)

            inserts the column name FIRST_NAME or LAST_NAME into the projection list, depending on the value of the variable A.
            
condition   -- An expression that evaluates to TRUE or FALSE,
expression  -- (In the CASE statement.) An expression specifying a projection list item. (See expression description above). 
            -- When condition is TRUE, expression is resolved,

name        -- A name you assign to the column produced by the CASE statement. (When you include the CASE statement, you must include the AS clause.)

name.*      -- When selecting columns from one or more tables or views, you can select all columns from a particular table by qualifying the special asterisk 
            -- character with the table name. name.* represents a list of names that identify the columns of name. name can be a table-name, view-name, 
            -- or correlation-name, and must designate a table or view named in the FROM clause. The first name in the list identifies the first column of 
            -- the table or view, the second name in the list identifies the second column of the table or view, and so on.
``` 
""")

st.subheader("Select Clause Examples")
st.markdown("""
In the sample query statement below, the prefix "part" in front of the CITY column (separated with a period) tells the system to use the CITY column from the PART table, rather than from the SUPPLIER table.
```sql
    SELECT pno, part.city, qty, sname
    FROM partsupp, supplier, part
    WHERE part.pno = partsupp.pno
      AND partsupp.sno = supplier.sno
``` 
If columns are not prefixed with the name of the owner table, the Server queries the first column with that name that the system encounters.

The next sample query adds a five percent surcharge on all outstanding customer balances in the state of Maryland, and then lists the new adjusted balance for each affected company. 
```sql
SELECT company,  balance + balance * .05 AS New_Balance
FROM customer
WHERE state = MD
```
The AS clause expression calculates the adjusted balance, which it displays under the heading New_Balance.
""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: SQL Syntax"):
        st.switch_page("pages/04 SQL_Syntax.py")
with col2:
    if st.button("Next: FROM"):
        st.switch_page("pages/06 FROM.py")
