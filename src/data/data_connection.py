import sqlite3
import pandas as pd


def get_data(query: str) -> pd.DataFrame | str:
    conn = sqlite3.connect('./db/vivino.db')
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        return f'<p> <span style="color: red;"> {e} </span>.</p>'
    finally:
        conn.close()
    return df
