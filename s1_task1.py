Dictionary={
    "Ahmed": 1394,
    "Ali":   6074,
    "Amr":   9345,
}
name=input("Please enter the name:")
password=int(input("please enter password:"))

if name in Dictionary.keys() and Dictionary[name]==password:
    print("Login successful")
else:
    print("Invalid username or password")
 



