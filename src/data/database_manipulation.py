import sqlite3
import pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy_schemadisplay import create_schema_graph


def get_data(query: str) -> pd.DataFrame | str:
    conn = sqlite3.connect('./db/vivino.db')
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        return f'<p> <span style="color: red;"> {e} </span>.</p>'
    finally:
        conn.close()
    return df


def generate_der() -> None:
    engine = create_engine('sqlite:///db/vivino.db')
    metadata = MetaData()
    metadata.reflect(bind=engine)
    graph = create_schema_graph(metadata=metadata, engine=engine, show_datatypes=False, show_indexes=False)
    graph.write_png('db/dbschema.png')
