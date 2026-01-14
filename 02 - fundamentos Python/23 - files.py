
try: 
        
    with open('test.txt', mode="w") as my_file:
        text = my_file.write(" :) ")
        
    with open('test.txt', mode="r") as my_file:
        print(my_file.readline())
        
    with open('test.txt', mode="r+") as my_file:
        print(my_file.readline())
        text = my_file.write(" :( ")
     
    with open('test.txt', mode="a") as my_file:
        text = my_file.write(" 123 ")
        print(text)
              
except FileNotFoundError as err:
    print("No existe el archivo")
except Exception as err:
    print(f"Ocurrió u error: {err}")