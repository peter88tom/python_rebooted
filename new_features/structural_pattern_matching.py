"""
Structural pattern matching lets you match value against a set of different possible values.
"""
def http_errors(status):
  match status:
    case 400:
      return "Bad request"
    case 401 | 403:
      return "Not allowed"
    case 404:
      return "Not found"
    case _:
      return "Something wrong with the internet"

newf = http_errors(404)
print(newf)
