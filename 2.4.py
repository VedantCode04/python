#Demonstrate Function Scoping.

global_var = "I'm a global variable"

def outer_function():
    outer_var = "I'm an outer variable"
    
    def inner_function():
        local_var = "I'm a local variable"
        print("Inside inner_function:")
        print(local_var)  
        print(outer_var)  
        print(global_var) 

    print("Inside outer_function:")
    print(outer_var)  
    print(global_var) 

    inner_function()
    print("Back inside outer_function:")

print("In the global scope:")
print(global_var) 

outer_function()
