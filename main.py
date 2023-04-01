import re

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
    n = int(input())
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
            raise ValueError("Invalid query format")
    return queries

def process_queries(queries):
    result = []
    phone_book = {}
    for query in queries:
        if query.type == 'add':
            phone_book[query.number] = query.name
        elif query.type == 'del':
            if query.number in phone_book:
                del phone_book[query.number]
        else:
            name = phone_book.get(query.number, "not found")
            result.append(name)
    return result

def write_responses(result):
    print('\n'.join(result))

if __name__ == '__main__':
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)

