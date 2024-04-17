import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("SQL Processing Capabilities")
st.markdown("""
SQL has been established as a language that can be used by casual users and skilled programmers. It offers a wide range of processing capabilities, simpler ones that beginners may use and more composite by the expert class of users.
""")
st.markdown("""
The various processing capabilities of SQL are:
<table class="table">
<tbody>
<tr>
<th style="width: 200px;">Type
</th><th>Description

</th></tr><tr>
<td>Data Definition Language (DDL)
</td><td>The SQL DDL offers commands for defining relation schemas, deleting relations, creating indexes, and modifying relation schemas.

</td></tr><tr>
<td>Interactive Data Manipulation Language
</td><td>DML includes query languages based on both relational algebra and tuple relational calculus.

</td></tr><tr>
<td>Embedded Data Manipulation Language
</td><td>The embedded form of SQL is designed for use within general-purpose programs such as PL/1, COBOL, Fortran, Pascal, or C.

</td></tr><tr>
<td>View Definition
</td><td>The SQL DDL also includes commands for defining views.

</td></tr><tr>
<td>Authorization
</td><td>The SQL DDL includes commands for specifying access rights to relations and views.

</td></tr><tr>
<td>Integrity
</td><td>SQL provides some limited forms of integrity checking. Future products and standards of SQL will likely comprise enhanced features for integrity checking.

</td></tr><tr>
<td>Transaction Control
</td><td>SQL also includes commands for specifying the beginning and end of transactions and commands for controlling transaction processing.

</td></tr></tbody>
</table>
""", unsafe_allow_html=True)

st.subheader("Data Definition Language (DDL)")
st.markdown("""
The database schema is specified by a set of definitions expressed by a particular language called data definition language. Changes to the structure of a database are handled by a different set of SQL statements, collectively termed as SQL Data Definition Language, or DDL.

Using DDL statements, you can do the following:

    - Define and create a new table.
    - Remove a table that is no longer needed.
    - Alter the definition of an existing table.
    - Classify a virtual table (view) of data.
    - Establish security controls for a database.
    - Index creation to make table search faster.
    - Control the physical storage of data by the DBMS. 

DDL is also used to define the length of data items. It may also specify the encoding the program uses in the data items (binary, character, bits, string, etc.).

Although the DDL and DML are two distinct parts of the SQL language, in most SQL-based DBMS products, the split is a conceptual one only. Usually, the DDL and DML statements are submitted to the DBMS in the same way, and they can be freely intermixed in both interactive SQL sessions and programmatic SQL applications. If a program or user needs a table to store its temporary results, it can create the table, populate it, manipulate the data, and then delete it. Again, this is a significant advantage over earlier data models, in which the database structure was fixed when the database was created.
""")

st.subheader("Data Manipulation Language (DML)")
st.markdown("""
After the database schema has been specified and the database has been created, the data can be manipulated using a set of procedures that are expressed by a particular language called a data manipulation language.

By data manipulation, language means:

    - Retrieval of information stored in the database.
    - Insertion of new information into the database.
    - Deletion of information from the database.
    - Modification of data in the database. 
""")
# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: Introduction to SQL"):
        st.switch_page("pages/01 Introduction_to_SQL.py")
with col2:
    if st.button("Next: SQL Data Types"):
        st.switch_page("pages/03 SQL_Data_Types.py")
