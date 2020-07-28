from os import system, name

# import only system from os 

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#Thank you https://www.geeksforgeeks.org/clear-screen-python/