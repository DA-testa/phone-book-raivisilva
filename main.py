# Raivis Ilva 221RDB403 
# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().strip().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result).strip())

def process_queries(queries):
    result = []
    # Keep a dictionary of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contact[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
