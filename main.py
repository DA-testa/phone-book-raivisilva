# Raivis Ilva 221RDB403 
# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        self.name = None
        if self.type == 'add':
            self.name = query[2]
        assert 0 <= self.number <= 9999999

def read_queries():
    n = int(input())
    assert 1 <= n <= 10**5
    return [Query(input().strip().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result).strip())

def process_queries(queries):
    contacts = {}
    result = []
    # Keep a dictionary of all existing (i.e. not deleted yet) contacts.

    for cur_query in queries:
        if cur_query.type == 'add':
            assert 1 <= cur_query.number <= 10**7 and len(cur_query.name) <= 15
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            assert 1 <= cur_query.number <= 10**7
            contacts.pop(cur_query.number, None)
        else:
            assert 1 <= cur_query.number <= 10**7
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
