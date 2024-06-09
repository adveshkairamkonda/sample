
"""
# Nested dict means dict has inside dict

person_details = {"name": "John Doe",
                  "address":
                      {"state": "USA",
                       "city":{"local": "XYZ", "central":"NY"}}}

print(f"Line 10 Person name is {person_details["name"]}  Person city is {person_details["address"]["city"]["local"]}")


# Len() - It gives how many items are available
print(f"Total items in the dict is {len(person_details)}")
print(f"Full dict is {person_details}")
print(f"Person name is {person_details["name"]}")
print(f"Address is {person_details["address"]}")
print(f"Address STATE is {person_details["address"]["state"]}")
print(f"Address CITY is {person_details["address"]["city"]}")
print(f"Address CITY LOCAL is {person_details["address"]["city"]["local"]}")
print(f"Address CITY CENTRAL is {person_details["address"]["city"]["central"]}")

"""
nested_dict = {
    'person1': {
        'name': 'Alice',
        'age': 30
    },
    'person2': {
        'name': 'Bob',
        'age': 25
    }
}
nested_dict_with_list = {
    'person1': {
        'name': 'Alice',
        'hobbies': ['reading', 'painting']
    },
    'person2': {
        'name': 'Bob',
        'hobbies': ['swimming', 'cooking']
    }
}
nested_dict_with_list = {
    'person1': {
        'name': 'Alice',
        'hobbies': ['reading', 'painting']
    },
    'person2': {
        'name': 'Bob',
        'hobbies': ['swimming', 'cooking']
    }
}
print(nested_dict['person1']['name'])  # Output: Alice
print(nested_dict_with_list['person2']['hobbies'][0])  # Output: swimming
nested_dict['person1']['age'] = 35
nested_dict_with_list['person1']['hobbies'].append('gardening')

print(nested_dict['person1']['age'])  # Output: 35
print(nested_dict_with_list['person1']['hobbies'])  # Output: ['reading', 'painting', 'gardening']
