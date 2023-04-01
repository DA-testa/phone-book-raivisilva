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
    assert 1 <= n <= 10**5, "Invalid number of queries"
    queries = []
    for i in range(n):
        query = input().strip().split()
        assert len(query) in [2, 3], "Invalid query format"
        if query[0] == 'add':
            assert len(query[1]) <= 7 and query[1].isdigit(), "Invalid phone number"
            assert len(query[2]) <= 15 and query[2].isalpha(), "Invalid name"
        elif query[0] == 'del':
            assert len(query[1]) <= 7 and query[1].isdigit(), "Invalid phone number"
        else:
            assert len(query[1]) <= 7 and query[1].isdigit(), "Invalid phone number"
            queries.append(Query(query))
    return queries
    #return [Query(input().strip().split()) for i in range(n)]

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
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            if cur_query.number in contacts:
                result.append(contacts[cur_query.number])
            else:
                result.append('not found')
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
