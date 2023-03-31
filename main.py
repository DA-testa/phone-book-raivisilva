# Raivis Ilva 221RDB403 
# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        self.name = None
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().strip().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result).strip())

def process_queries(queries):
    contacts = {}
    result = []
    # Keep a dictionary of all existing (i.e. not deleted yet) contacts.

    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts.pop(cur_query.number, None)
        else:
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
