

def insert_to_vecdb(client, chunks):
    return client.upsert(chunks)


def retrieve(client, query):
    results = client.search(query)
    context = []
    for result in results:
        context.append(result[0])
    return "\n".join(context)

