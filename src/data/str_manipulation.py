import re
import sqlparse
import textwrap


def sql_formating(code_input: str) -> str:
    # Detect the language of the code
    sql_keywords_regex = r'^(SELECT|WITH|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER)'
    match = re.search(sql_keywords_regex, code_input.strip(), re.IGNORECASE)

    formatted_code = code_input
    if match:
        formatted_code = sqlparse.format(code_input, reindent=True)
        formatted_code = textwrap.indent(formatted_code, " " * 4)

        if formatted_code[-1] != ';':
            formatted_code += ';'

    return formatted_code
