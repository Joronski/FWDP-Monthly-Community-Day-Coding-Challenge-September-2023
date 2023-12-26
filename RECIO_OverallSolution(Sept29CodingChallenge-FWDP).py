def matchingStrings(stringList, queries):
  """
  Counts the number of occurrences of each query string in stringList.

  Args:
    stringList: A list of strings to search.
    queries: A list of strings to search for.

  Returns:
    A list of integers representing the frequency of occurrence of each query string
    in stringList.
  """

  results = []
  for query in queries:
    count = 0
    for string in stringList:
      if query == string:
        count += 1
    results.append(count)
  return results

# Prompt the user to enter the stringList and queries
stringList = input("Enter the stringList: ").split()
queries = input("Enter the queries: ").split()

# Generating the results
results = matchingStrings(stringList, queries)

# Printing the results
for result in results:
  print(result)

"""
  After the Code is executed just input the following stringList and queries

  ex.
  Enter the stringList: aba baba aba xzxb
  Enter the queries: aba xzxb ab

  The Output will be:
  2
  1
  0

  Same goes to the other test cases in Sparse Arrays Challenge
"""