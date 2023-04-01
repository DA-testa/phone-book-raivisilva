# Raivis Ilva 221rdb403
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
            raise ValueError("Invalid format")
    return queries


def process_queries(queries):
    result = []
    phoneBook = {}
    for query in queries:
        if query.type == 'add':
            phoneBook[query.number] = query.name
        elif query.type == 'del':
            if query.number in phoneBook:
                del phoneBook[query.number]
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


# python3

# class Query:
#     def __init__(self, query):
#         self.type = query[0]
#         self.number = int(query[1])
#         if self.type == 'add':
#             self.name = query[2]

# def read_queries():
#     n = int(input())
#     return [Query(input().split()) for i in range(n)]

# def write_responses(result):
#     print('\n'.join(result))

# def process_queries(queries):
#     result = []
#     # Keep list of all existing (i.e. not deleted yet) contacts.
#     contacts = []
#     for cur_query in queries:
#         if cur_query.type == 'add':
#             # if we already have contact with such number,
#             # we should rewrite contact's name
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     contact.name = cur_query.name
#                     break
#             else: # otherwise, just add it
#                 contacts.append(cur_query)
#         elif cur_query.type == 'del':
#             for j in range(len(contacts)):
#                 if contacts[j].number == cur_query.number:
#                     contacts.pop(j)
#                     break
#         else:
#             response = 'not found'
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     response = contact.name
#                     break
#             result.append(response)
#     return result

# if __name__ == '__main__':
#     write_responses(process_queries(read_queries()))