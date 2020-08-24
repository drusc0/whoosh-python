import sys

from whoosh import scoring
from whoosh.index import open_dir
from whoosh.qparser import QueryParser


def query_index(string, n, indexdir="indexdir"):
    ix = open_dir(indexdir)

    with ix.searcher(weighting=scoring.Frequency) as searcher:
        query = QueryParser("content", ix.schema).parse(string)
        results = searcher.search(query, limit=n)
        for i in range(n):
            print(results[i]['title'], float(results[i].score), results[i]['textdata'])


if __name__ == "__main__":
    query_str, top_n = sys.argv[1], int(sys.argv[2])
    query_index(query_str, top_n)
