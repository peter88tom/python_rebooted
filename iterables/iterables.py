"""
Iterable is an object that includes zero, one and many elements. An iterable has the ability to return one element
at a time.

Because of this feature you can use for loop to iterate over it.

In fact range(), list, tuple are iterable because you can loop over them

What is an iterator?
  - It is an agent that performs the iteration
  - To get an iterator from an iterable object, you can use iter() function
  - Once you have iterator you use next() function to get next element.
  - Every time you call next() function, it returns the next element in the iterable.
  - If there will be no more elements and you call next() function, you will get an exception

  See example below
"""

languages = ['Python', 'Ruby', 'Java', 'Go']

languages_iter  = iter(languages)

language = next(languages_iter)
print(language)

next_language = next(languages_iter)
print(next_language)


