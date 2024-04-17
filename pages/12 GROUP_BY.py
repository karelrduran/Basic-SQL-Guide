import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("GROUP BY Clause")
st.markdown("""
When a query statement includes a GROUP BY clause, the SELECT clause for that query may list (in addition to ordinary column names) one or more aggregate functions (SUM, COUNT, AVG, etc.) operating on groups of data values in other columns.

The GROUP BY clause contains a column-list argument that must include all simple column names that appear in the SELECT clause. Columns can also be named using the AS Clause (see SELECT Clause). Simple column names are called grouping columns, since they group together records with identical data in that column. This record grouping allows mathematical operations to be performed on the other columns specified as arguments in the aggregate functions. Records can also be grouped by any valid expression appearing in the SELECT clause argument. In these cases, the expression must also be referenced in the GROUP BY clause by a whole number representing its relative column position in the SELECT clause (or output result).

The GROUP BY clause format appears below:
``sql
GROUP BY column-list
``
Parameters:
column-list -- Consists of an ordered list of column names or numbers, separated by commas.
""")

st.subheader("GROUP BY Example")
st.markdown("""
The following query uses functions to produce three output columns in the query results. The query calculates the number of parts made in each city, and the maximum and minimum weight of those parts (in each city):
```sql
SELECT city, COUNT(*), MIN(weight), MAX(weight)
FROM part
GROUP BY city
```

The query results are as follows:
|city 	|count(*) 	|min(weight) 	|max(weight)|
|-------|-----------|---------------|-----------|
|LONDON |3         	|12      	    |19         |
|PARIS 	|3 	        |12         	|17         |

The next example (not available in DB2 mode) finds the number of orders placed each month, grouping the results by the first output column:
```sql
SELECT XMONTH(o_date), COUNT(*)
FROM orders
GROUP BY 1
```

The query results are as follows:
|column1|count(*)|
|-------|--------|
|9   	|1       |
|10 	|4       |
""")

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: WHERE"):
        st.switch_page("pages/11 WHERE.py")
with col2:
    if st.button("Next: ORDER BY"):
        st.switch_page("pages/13 ORDER_BY.py")
