import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.title("Introduction to SQL", )
st.subheader("What is SQL?")
st.markdown("""
SQL stands for Structured Query Language. It is a powerful programming language specifically designed for managing, manipulating, and querying relational databases. SQL is widely used in database management systems (DBMS) such as MySQL, PostgreSQL, Oracle, SQL Server, SQLite, and others.
""")

st.subheader("Here are some key points about SQL:")
st.markdown("""
1. **Database Interaction**: SQL allows users to interact with databases by defining and manipulating data, as well as performing various operations such as querying, 
   updating, inserting, and deleting data.  
    
2. **Declarative Language**: SQL is a declarative language, meaning that users specify what they want to achieve rather than describing how to achieve it. 
   Users define the desired results, and the database system determines the most efficient way to execute the query.
   
3. **Standardized Language**: SQL is an ANSI/ISO standard language, although different database systems may have their own variations and extensions. 
   However, the basic syntax and functionality of SQL are consistent across most platforms.
   
4. **Structured Querying**: SQL provides a structured way to query databases using a variety of commands and clauses. 
   Common SQL commands include SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, and DROP.
   
5. **Data Definition and Manipulation**: SQL can be used to define the structure of databases, 
   including creating and modifying tables, defining constraints (such as primary keys and foreign keys), and managing indexes.
   
6. **Data Retrieval**: SQL enables users to retrieve data from databases using SELECT statements. 
   Users can specify criteria to filter and sort the data, as well as aggregate functions to perform calculations on groups of data.
   
7. **Data Modification**: SQL allows users to modify existing data in databases using commands such as INSERT, UPDATE, and DELETE. 
   These commands can add new records, update existing records, or remove records from a database.
***
""")


st.subheader("Why is SQL important?")
st.markdown("The importance of SQL (Structured Query Language) stems from its role as the standard language for managing and manipulating relational databases. Here are several key reasons why SQL is important:")
st.markdown("""
1. **Universal Language**: SQL is a standardized language adopted by most relational database management systems (RDBMS), including industry giants like MySQL, 
   PostgreSQL, Oracle, SQL Server, SQLite, and others. Its widespread adoption makes it a universal tool for interacting with databases regardless of the specific 
   platform.
   
2. **Data Management**: SQL provides powerful capabilities for managing data within databases. It allows users to define the structure of databases, create and modify 
   tables, enforce data integrity constraints, and manage indexes for efficient data retrieval.
   
3. **Data Querying**: SQL enables users to retrieve, filter, and manipulate data stored in databases using a variety of commands and functions. With SQL, users can write 
   complex queries to extract specific information from large datasets, perform calculations, aggregate data, and generate reports.
   
4. **Data Manipulation**: In addition to querying data, SQL supports operations for modifying existing data in databases. Users can insert new records, update existing 
   records, and delete records from tables using SQL commands like INSERT, UPDATE, and DELETE.
   
5. **Database Administration**: SQL is essential for database administrators (DBAs) responsible for maintaining and optimizing database performance, ensuring data 
   security, and managing user access privileges. DBAs use SQL to perform tasks such as database backups, schema modifications, and user management.
   
6. **Application Development**: SQL is integral to the development of database-driven applications. Software developers use SQL to interact with databases from their 
   applications, execute database operations, and handle data retrieval and manipulation tasks. Many programming languages provide libraries or frameworks for 
   integrating SQL queries into application code seamlessly.
   
7. **Business Intelligence and Analytics**: SQL plays a crucial role in business intelligence (BI) and data analytics processes. Analysts and data scientists use SQL to 
   query and analyze large volumes of data stored in databases, extract insights, and make data-driven decisions. SQL's ability to perform complex joins, 
   aggregations, and calculations makes it indispensable for data analysis tasks.
   
8. **Data Integration**: SQL facilitates data integration by enabling the exchange of data between different systems and applications. Users can use SQL commands to 
   import data into databases from external sources, export data from databases to other systems, and transform data between different formats.
***
""")

st.subheader("What can SQL do?")
st.markdown("SQL (Structured Query Language) can perform a wide range of operations on a relational database. Some of the main things that SQL can do include:")
st.markdown("""
```sql
SELECT -- Retrieve specific data from one or more tables.

INSERT -- Add new data to a table.

UPDATE -- Modify existing data in a table.

DELETE -- Remove data from a table.

CREATE -- Create new tables, views, stored procedures, and other database objects.

ALTER -- Modify the structure of existing tables, views, and other database objects.

DROP -- Remove tables, views, and other database objects.

INDEX -- Create and manage indexes to improve the performance of queries.

JOIN -- Retrieve data from multiple tables based on a related column.

UNION -- Combine the results of various SELECT statements.

GROUP BY -- Group data by one or more columns and perform aggregate functions.

HAVING -- Filter data based on aggregate functions.

WHERE -- Filter data based on specific conditions.

ORDER BY -- Sort data in ascending or descending order.

LIMIT -- Retrieve a particular number of rows from the result set.

TRUNCATE -- Remove all data from a table, but keep the table structure. 
```
""", unsafe_allow_html=True)
st.markdown("These are just a few examples of the many operations that can be performed using SQL, and the specific set of commands and functionality may vary depending on the specific relational database management system (RDBMS) being used.")

# Navigation Section

st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: Home"):
        st.switch_page("Home.py")
with col2:
    if st.button("Next: SQL Processing Capability"):
        st.switch_page("pages/02 SQL_Processing_Capability.py")
