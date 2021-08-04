# Here's the first example of duplication
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


# Here's the second example of duplication
def remove_duplicates1(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result