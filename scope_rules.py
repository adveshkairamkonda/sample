global_var = "I am global"

def outer_function():
    # Enclosing scope
    enclosing_var = "I am enclosing"

    def inner_function():
        # Local scope
        local_var = "I am local"
        print("Inside inner_function:")
        print("Local variable:", local_var)
        print("Enclosing variable:", enclosing_var)
        print("Global variable:", global_var)

    inner_function()

print("Outside all functions:")
print("Global variable:", global_var)

outer_function()

"""
global_var is a global variable accessible throughout the script.
outer_function defines enclosing_var in its enclosing scope.
inner_function defines local_var in its local scope.
All variables are accessible from their respective scopes.
The output demonstrates how variables are accessed from different scopes.
"""