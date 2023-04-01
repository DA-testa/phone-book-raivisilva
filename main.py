# Raivis Ilva 221rdb403 13.GRUPA
import re
import sys


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = None
        self.name = None
        if self.type == 'add':
            self.number = int(query[1])
            self.name = query[2]
        else:
            self.number = int(query[1])


def read_queries():
    n = int(sys.stdin.readline())
    queries = []
    for i in range(n):
        query = input().strip().split()
        if len(query) == 2 and query[0] == "find":
            queries.append(Query(query))
        elif len(query) == 3 and query[0] == "add" and query[1].isdigit() and query[2].isalpha() and len(query[1]) <= 7 and len(query[2]) <= 15:
            queries.append(Query(query))
        elif len(query) == 2 and query[0] == "del" and query[1].isdigit() and len(query[1]) <= 7:
            queries.append(Query(query))
        else:
            raise ValueError("Invalid format")
    return queries


def process_queries(queries):
    result = []
    phoneBook = {}
    for query in queries:
        if query.type == 'add':
            phoneBook[query.number] = query.name
        elif query.type == 'del':
            phoneBook.pop(query.number, None)
        else:
            name = phoneBook.get(query.number, "not found")
            result.append(name)
    return result


def write_responses(result):
    print('\n'.join(result))


if __name__ == '__main__':
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)
