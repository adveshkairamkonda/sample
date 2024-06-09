import json
# Python Data Types
num = 10
list_data = [10,20,30]
tuple_data = (45,90,80)
str_data = "Hello everyone welcome to India"
dict_data = {"name": "John Done", "state":"Karnataka","city":"Bangalore"}
bool_true_data = True
bool_false_data = False
none_data = None

# Convert Python to Json data type
num_json = json.dumps(num) # '10'
list_data_json = json.dumps(list_data) # '[10,20,30]'
tuple_data_json = json.dumps(tuple_data) # '(45,90,80)'
str_json_data = json.dumps(str_data) # '"Hello everyone welcome to India"'
dict_data_json = json.dumps(dict_data) # '{"name": "John Done", "state":"Karnataka","city":"Bangalore"}'
bool_true_data_json = json.dumps(bool_true_data)
bool_false_data_json = json.dumps(bool_false_data)
non_data_json = json.dumps(none_data)

print(f"JSON num is {num_json} Type is {type(num_json)}")
print(f"JSON list is {list_data_json}  Type is {type(list_data_json)}")
print(f"JSON tuple is {tuple_data_json}  Type is {type(tuple_data_json)}")
print(f"JSON dict is {dict_data_json}  Type is {type(dict_data_json)}")
print(f"JSON bool True is {bool_true_data_json} Type is {type(bool_true_data_json)}")
print(f"JSON bool False is {bool_false_data_json} Type is {type(bool_false_data_json)}")
print(f"JSON None is {non_data_json} Type is {type(non_data_json)}")
