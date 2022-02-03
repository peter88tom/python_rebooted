"""
You can use .pop() to get and remove value on key inside a dictionary
You can provide a default value for the case when the key doesn't exist
"""

student = {
  "first_name": "John",
  "last_name": "Doe",
  "education_level": "Permanent Head Damage(Phd)",
  "school_name": "WITS"
}


def remove_value(student):
    """ Remove using key"""
    print(student) # print the original dict
    student.pop("school_name") # remove school_name from dict
    print(student) # print the updated dict


remove_value(student)
