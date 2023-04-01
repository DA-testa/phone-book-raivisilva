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
    n = int(input().strip())
    if not 1 <= n <= 10**5:
        raise ValueError("Invalid value of N")
    queries = []
    for i in range(n):
        query = input().strip()
        if not re.match(r"(add|del|find) \d{1,7} [a-zA-Z]{1,15}", query):
            raise ValueError("Invalid query format")
        queries.append(Query(query.split()))
    return queries

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    contacts = {}
    result = []
    # Keep a dictionary of all existing (i.e. not deleted yet) contacts.

    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            if cur_query.number in contacts:
                result.append(contacts[cur_query.number])
            else:
                result.append('not found')
    return result


if __name__ == '__main__':
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)

