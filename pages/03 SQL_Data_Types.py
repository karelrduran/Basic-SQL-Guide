import streamlit as st

from page_parts.page_configuration import page_configuration

# Page Configuration

page_configuration()

# Body Section

st.subheader("SQL Data Types")
st.markdown("""
SQL data types specify the type of data that a column or variable can hold in a SQL database. These data types include numeric, character and string, date and time, binary, boolean, enumerated, array, and JSON types. Each data type has a specific range of values and uses. Choosing the appropriate data type for a column or variable is essential for accurate and efficient data storage and retrieval.
""")
st.markdown("""
<table class="table">
<tbody>
<tr>
<th>Data Type
</th><th>Description

</th></tr><tr>
<td><code>INT</code>
</td><td>The <code>INT</code> data type stores integer values. It can hold whole numbers, such as items in stock or orders placed.&nbsp;<code>INT</code> values can range from -2147483648 to 2147483647.

</td></tr><tr>
<td><code>BIGINT</code>
</td><td>The <code>BIGINT</code> data type stores large integers. It can be used to hold whole numbers larger than the range of values that can be stored in the&nbsp;<code>INT</code> data type. <code>BIGINT</code> values can range from -9223372036854775808 to 9223372036854775807.

</td></tr><tr>
<td><code>SMALLINT</code>
</td><td>The <code>SMALLINT</code> data type stores smaller integers. It can be used to hold whole numbers smaller than the range of values that can be stored in the&nbsp;<code>INT</code> data type. <code>SMALLINT</code> values can range from -32768 to 32767.

</td></tr><tr>
<td><code>TINYINT</code>
</td><td>The <code>TINYINT</code> data type stores very small integers. It can be used to hold whole numbers smaller than the range of values that can be stored in the <code>SMALLINT</code> data type. <code>TINYINT</code> values can range from 0 to 255.

</td></tr><tr>
<td><code>NUMERIC</code>
</td><td>The <code>NUMERIC</code> data type stores exact numeric values with a fixed precision and scale. The precision is the total number of digits in a number, and the scale is the number of digits to the right of the decimal point. For example, 124.56 has a precision of 5 and a scale of 2.

</td></tr><tr>
<td><code>DECIMAL</code>
</td><td>The <code>DECIMAL</code> data type is similar to the <code>NUMERIC</code> data type that stores exact numeric values with a fixed precision and scale. It's important to note that&nbsp;<code>NUMERIC</code> and <code>DECIMAL</code> are synonyms in SQL, and it's up to the developer to choose which one to use.

</td></tr><tr>
<td><code>FLOAT</code>
</td><td>The <code>FLOAT</code> data type stores approximate numeric values with a floating-point representation. It can store very large or tiny numbers with many digits before and after the decimal point.

</td></tr><tr>
<td><code>REAL</code>
</td><td>The <code>REAL</code> data type stores approximate numeric values with a floating-point representation. It is similar to the <code>FLOAT</code> data type but uses fewer bits to represent the value, meaning it has a smaller range and less precision.

</td></tr><tr>
<td><code>DOUBLE PRECISION</code>
</td><td>The <code>DOUBLE PRECISION</code> data type stores approximate numeric values with a floating-point representation, similar to the <code>FLOAT</code> and <code>REAL</code> data types. <code>DOUBLE PRECISION</code> is often used to store floating-point numbers with higher precision than the <code>FLOAT</code> data type.

</td></tr><tr>
<td><code>CHAR</code>
</td><td>The <code>CHAR</code> data type stores fixed-length character strings. It can hold a fixed number of characters, specified by the field's length. For example, a <code>CHAR(10)</code> field can store a string of up to 10 characters. If the inserted string is shorter than the specified length, the remaining characters will be filled with spaces.

</td></tr><tr>
<td><code>VARCHAR</code>
</td><td>The <code>VARCHAR</code> data type stores variable-length character strings. It can hold a variable number of characters, specified by the field's length. For example, a <code>VARCHAR(10)</code> field can store a string of up to 10 characters. If the string inserted is shorter than the specified length, it will only use the necessary amount of storage.

</td></tr><tr>
<td><code>TEXT</code>
</td><td>The TEXT data type stores variable-length character strings, similar to the <code>VARCHAR</code> data type. It can store a large amount of character data, and the maximum length of a <code>TEXT</code> field is typically much larger than that of a <code>VARCHAR</code> field. The exact maximum length of a <code>TEXT</code> field can vary depending on the specific SQL implementation being used.

</td></tr><tr>
<td><code>DATE</code>
</td><td>The <code>DATE</code> data type stores date values. It can be used to hold a date, which includes the day, month, and year. It's defined as&nbsp;<code>DATE</code> and used to store date information such as birthdate, hiring date, order date, etc. The format of a <code>DATE</code> value can vary depending on the specific SQL implementation being used, but it typically follows the format of "YYYY-MM-DD" where YYYY represents the year, MM represents the month, and DD represents the day.

</td></tr><tr>
<td><code>TIME</code>
</td><td>The <code>TIME</code> data type stores time values. It can keep time, which includes hours, minutes, and seconds. It can store information such as opening, closing, arrival, departure, etc. The format of a&nbsp;<code>TIME</code> value can vary depending on the specific SQL implementation being used, but it typically follows the format of "HH:MM:SS" where HH represents the hour, MM represents the minutes, and SS represents the seconds.

</td></tr><tr>
<td><code>DATETIME</code>
</td><td>The <code>DATETIME</code> data type stores both date and time values. It can be used to hold a date and time, which includes the day, month, year, and time, which consists of the hours, minutes, and seconds. It's defined as&nbsp;<code>DATETIME</code>, and it's used to store date and time information such as start time, end time, and timestamp. The format of a <code>DATETIME</code> value can vary depending on the specific SQL implementation, but it typically follows the format of "YYYY-MM-DD HH:MM:SS".

</td></tr><tr>
<td><code>TIMESTAMP</code>
</td><td>In SQL, the <code>TIMESTAMP</code> data type stores both date and time values, similar to the <code>DATETIME</code> data type. It can be used to store a date, which includes the day, month, year, and time, which consists of the hours, minutes, and seconds. It's defined as <code>TIMESTAMP</code>, which stores date and time information such as start time, end time, and timestamp. The format of a <code>TIMESTAMP</code> value can vary depending on the specific SQL implementation being used. Some implementations provide automatic initialization and updating for <code>TIMESTAMP</code> columns.

</td></tr><tr>
<td><code>YEAR</code>
</td><td>The <code>YEAR</code> data type stores year values. It can be used to hold a year, which includes four digits representing the year. It's defined as&nbsp;<code>YEAR</code> and used to store year information such as birth year, hire year, etc.

</td></tr><tr>
<td><code>BINARY</code>
</td><td>The <code>BINARY</code> data type stores fixed-length binary data. It is comparable&nbsp;to the CHAR data type but holds binary values instead of character strings. The&nbsp;<code>BINARY</code> data type requires a fixed length to be specified and can be used to store any binary data, such as images, audio, or other binary files.

</td></tr><tr>
<td><code>VARBINARY</code>
</td><td>The <code>VARBINARY</code> data type stores variable-length binary data. It is similar to the <code>VARCHAR</code> data type but holds binary values instead of character strings. The <code>VARBINARY</code> data type requires a maximum length to be specified and can be used to hold any binary data, such as images, audio, or other binary files.

</td></tr><tr>
<td><code>BLOB</code>
</td><td>The <code>BLOB</code> (Binary Large OBject) data type stores extensive binary data such as images, audio, or other binary files. It can hold a large amount of binary data, and the maximum size of a <code>BLOB</code> field can vary depending on the specific SQL implementation being used. <code>BLOB</code> is typically used to store data that is not character or string data.

</td></tr><tr>
<td><code>BOOLEAN</code>
</td><td>The <code>BOOLEAN</code> data type stores true/false or yes/no values. It can hold only two possible values: <code>TRUE</code>, <code>FALSE</code>, <code>YES</code>, or <code>NO</code>. It's defined as <code>BOOLEAN</code> and used to store logical values. The exact representation of a <code>BOOLEAN</code> value can vary depending on the specific SQL implementation being used, but it typically follows the format of "<code>TRUE</code>" or "<code>FALSE</code>" or "<code>1</code>" or "<code>0</code>" or "<code>YES</code>" or "<code>NO</code>".

</td></tr><tr>
<td><code>ENUM</code>
</td><td>The <code>ENUM</code> data type stores a predefined set of values. It is a string object with a value chosen from a list of permitted values specified when the table is created. It is similar to a string object but is more restrictive in that it only allows values included in the list of permitted values.

</td></tr><tr>
<td><code>ARRAY</code>
</td><td>The <code>ARRAY</code> data type stores an ordered collection of elements. It is a variable-size multidimensional array and can hold a list of values with the same data type. The elements of an array can be any data type, such as integers, strings, or other complex data types. The size of an array is not fixed and can be changed dynamically.

</td></tr><tr>
<td><code>JSON</code>
</td><td>The <code>JSON</code> data type stores JSON (JavaScript Object Notation) data. It is a lightweight data-interchange format that is simple for humans to read and write and for machines to parse and generate.

</td></tr><tr>
<td><code>JSONB</code>
</td><td>The <code>JSONB</code> data type stores binary representation of JSON (JavaScript Object Notation) data. <code>JSONB</code> (binary JSON) is an optimized binary format of JSON data. It is similar to the <code>JSON</code> data type but stores the data in a binary format, making it more efficient in terms of storage and retrieval. <code>JSONB</code> also provides additional functionality, such as indexing and searching capabilities on the JSON data.

</td></tr><tr>
<td><code>UUID</code>
</td><td>The <code>UUID</code> (Universally Unique Identifier) data type stores unique identifier values. It is a 128-bit value represented as a hexadecimal string, usually in the format of "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX". It is designed to have a very low probability of the same value being generated twice, hence the term "universally unique".

</td></tr><tr>
<td><code>IP ADDRESS</code>
</td><td>The <code>IP ADDRESS</code> data type stores Internet Protocol (IP) address values. It is a string representation of an IP address, usually in the format of "xxx.xxx.xxx.xxx" for IPv4 addresses and "xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx" for IPv6 addresses.

</td></tr><tr>
<td><code>CIDR</code>
</td><td>The <code>CIDR</code> (Classless Inter-Domain Routing) data type stores IP network addresses in a compact representation. It is a string representation of an IP network address, usually in the format of "xxx.xxx.xxx.xxx/yy" for IPv4 addresses and "xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/yy" for IPv6 addresses. The "yy" represents the number of bits of the IP address used to identify the network, also called the prefix length.

</td></tr></tbody>
</table>
""", unsafe_allow_html=True)

st.markdown("""
***
<div style="background-color:green; padding:10px;">
It's worth noting that SQL data types can have additional constraints and options, such as UNSIGNED for numeric types and CHARACTER SET for character and string types; also, different SQL implementations may have different data types or variations of data types.
</div>

***    
""", unsafe_allow_html=True)

st.subheader('SQL Data Types Example')

st.code(
    body="""
    CREATE TABLE customers (
        customer_id INT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(255) UNIQUE,
        date_of_birth DATE,
        is_active BOOLEAN NOT NULL DEFAULT TRUE,
        last_login TIMESTAMP
    );
""",
    language='sql')

st.markdown("""
<ul class="list">
<li>In the example above, the "<code>customer_id</code>" column has an <code>INT</code> data type and is set as the <code>primary key</code>, meaning it must contain a unique value for each row in the table.
</li><li>The "<code>first_name</code>" and "<code>last_name</code>" columns have <code>VARCHAR</code> data types with a maximum length of <code>50</code> characters and are both set as "<code>NOT NULL</code>", meaning they must contain a value.
</li><li>The "<code>email</code>" column has a <code>VARCHAR</code> data type with a maximum length of <code>255</code> characters and is set as "<code>UNIQUE</code>", meaning it must contain a unique value across the entire table.
</li><li>The "<code>date_of_birth</code>" column has a <code>DATE</code> data type.
</li><li>The "<code>is_active</code>" column has a <code>BOOLEAN</code> data type and is set as "<code>NOT NULL</code>" and "<code>DEFAULT TRUE</code>".
</li><li>The "<code>last_login</code>" column has a <code>TIMESTAMP</code> data type.
</li></ul> 
""", unsafe_allow_html=True)

# Navigation Section
st.markdown("***")
col1, col2 = st.columns(spec=2, gap='large')

with col1:
    if st.button("Previous: SQL Processing Capability"):
        st.switch_page("pages/02 SQL_Processing_Capability.py")
with col2:
    if st.button("Next: SQL Syntax"):
        st.switch_page("pages/04 SQL_Syntax.py")
