"""
  Sometimes, you need to iterate over elements of a list and select some of them based on the specified criteria

  filter() build in python function can help you archive that, See example below
"""


# Given the below scores, return scores that is below 80
scores = [90,10, 89, 30, 200, 4, 32.6]

scores_less_than_80 = filter(lambda score:score <= 80, scores)
print(list(scores_less_than_80))



"""
You can use for loop to archive this as well by creating a new list
"""

