import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("FROM Clause Syntax and Description")
st.markdown("""
The FROM clause (like the SELECT clause) must appear in every SQL query statement. See SELECT Clausefor more information. While the SELECT clause specifies from which columns data values are retrieved during query execution, the FROM clause specifies the table(s) in which these data columns are located.

The FROM clause names one or more tables (or views) from which data values are retrieved by the query. Data retrieval is limited to the tables (or views) specified. The XDB Server also allows you to explicitly specify right, left, and full outer joins, and use subselects or nested table expressions. The FROM clause either names a single table or view or produces an intermediate result table that is the result of a subselect or an inner or outer join operation.

The FROM clause is required in a SELECT statement to identify the tables and/or views that are being queried. When more than one table or view is specified in the FROM clause, each of these object names can also be assigned a correlation name. In XDB mode, the FROM clause is extended to allow explicit expression of inner and outer join operations and a subselect or nested table expression. 

The FROM clause format appears below: 
```sql
FROM table-ref [,...]
```
table-ref: 
```sql
{
  [{table-name | view-name} [[AS] correlation-name]
  | [(subselect) [AS] correlation-name]
  | [joined-table]}
}
```
joined-table: 
```sql
table-ref [INNER] | [{LEFT | RIGHT | FULL} [OUTER]]
  JOIN table-ref join-condition
| [(joined-table)]
```
join-condition:
```sql
ON join-expression { = | <> | > | < | >= | <= }
  join-expression AND [...]
```
join-expression:
```sql
column-name [{VALUE | COALESCE} (column-name [,...])]
```
""")
st.markdown("""
Parameters:
```sql
table-name or view-name -- A list of one or more table or view names (separated by commas), from which data values are to be retrieved. 
                        -- Must identify a table or view described in the system catalog of the database subsystem identified by the implicitly 
                        -- or explicitly specified location name.
                        
correlation-name        --Can be specified for a table reference, either immediately following the table reference or after the AS keyword which follows 
                        -- the table reference. A correlation name must be specified for a nested table expression that is enclosed in parentheses.
                        
joined-table            -- Specifies an intermediate result table that is the result of either an inner equi-join or an outer join. The table is derived 
                        -- by applying one of the join-operators; INNER, RIGHT OUTER, LEFT OUTER, or FULL OUTER, to its operands. If a join-operator 
                        -- is not specified, INNER is implicit. The order in which a LEFT OUTER or RIGHT OUTER JOIN is performed can affect the result. 
                        -- A joined-table can be used in any context in which any form of the SELECT statement is used. Both a view and a cursor is read-only 
                        -- if its SELECT statement includes a joined-table.
                        
joined-condition        -- Defines a search condition in which predicates can be combined only with the keyword AND, and each predicate has the form 
                        -- 'expression operator expression'. The '=' operator is the only operator allowed for a FULL OUTER JOIN or a FULL JOIN.
                        
join-expression         -- Must include a column name. Only columns and the VALUE and COALESCE functions are allowed in the expression. 
                        -- VALUE and COALESCE are allowed only when the join operator is FULL JOIN or FULL OUTER JOIN. 
                        -- One expression of the predicate must reference only columns of one of the operand tables of the associated join operator, 
                        -- and the other expression of the predicate must reference only columns of the other operand table. Before this rule is applied, 
                        -- column references are resolved using the rules for resolution of column name qualifiers. 
```
""")

st.subheader("Correlation Names")
st.markdown("""
Correlation names are used in place of the actual table or view name when qualifying columns within a query statement. The correlation name appears immediately after the corresponding table or view name in the FROM clause (separated by a single space). Correlation names must satisfy the same naming conventions as table names, and must be unique among all table, view and other correlation names within a query. The correlation name qualifies columns that appear in either SELECT or WHERE clauses. See WHERE Clause for more information.

The following query shows a correlation name of "p" being assigned to the PART table, and a correlation name of "ps" being assigned to the PARTSUPP table.
```sql
SELECT pname, qty
FROM part p, partsupp ps
WHERE p.pno = ps.pno
```
""")
st.subheader("Using AS")
st.markdown("""
 The AS keyword is available before correlation names, and after the following:

    - Nested table expressions
    - Table names
    - View names
    - Aliases
    - Synonyms
""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: SELECT"):
        st.switch_page("pages/05 SELECT.py")
with col2:
    if st.button("Next: INNER JOIN"):
        st.switch_page("pages/07 INNER_JOIN.py")
