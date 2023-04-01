class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        self.name = None
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    if n < 1 or n > 10**5:
        raise ValueError("Invalid number of queries.")
    queries = []
    for i in range(n):
        query = input().strip().split()
        if query[0] == 'add':
            if len(query) != 3:
                raise ValueError("Invalid query format.")
            if not query[1].isdigit() or len(query[1]) > 7 or query[1][0] == '0':
                raise ValueError("Invalid phone number.")
            if not query[2].isalpha() or len(query[2]) > 15:
                raise ValueError("Invalid name.")
        elif query[0] == 'find':
            if len(query) != 2:
                raise ValueError("Invalid query format.")
            if not query[1].isdigit() or len(query[1]) > 7 or query[1][0] == '0':
                raise ValueError("Invalid phone number.")
        elif query[0] == 'del':
            if len(query) != 2:
                raise ValueError("Invalid query format.")
            if not query[1].isdigit() or len(query[1]) > 7 or query[1][0] == '0':
                raise ValueError("Invalid phone number.")
        else:
            raise ValueError("Invalid query type.")
        queries.append(Query(query))
    return queries

def write_responses(result):
    print('\n'.join(result).strip())

def process_queries(queries):
    contacts = {}
    result = []
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
    try:
        queries = read_queries()
        write_responses(process_queries(queries))
    except ValueError as e:
        print("Error:", e)


