import json


class QueryManipulation:
    def __init__(self):
        self.queries = self.read_json()

    def read_json(self) -> list:
        queries = 'src/sql_scripts/queries.json'
        with open(queries) as f:
            queries = json.load(f)

        return queries

    def write_json(self, query: str, description: str):
        pass

    def queries_description(self) -> list:
        descriptions = [query['description'] for query in self.queries]
        return descriptions

    def get_query(self, description: str) -> str:
        for query in self.queries:
            if description in query['description']:
                return query['query']
