def matchingStrings(stringList, queries):
    """
    Counts the number of occurrences of each query string in stringList.

    Args:
        stringList: A list of strings to search.
        queries: A list of strings to search for.

    Returns:
        A list of integers representing the frequency of occurrence of each query string in stringList.
    """

    results = []
    for query in queries:
        count = 0
        for string in stringList:
            if query == string:
                count += 1
        results.append(count)
    return results

# Example Usage:

# Sample 1 Input
stringList = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]

results = matchingStrings(stringList, queries)

for result in results:
    print(result)