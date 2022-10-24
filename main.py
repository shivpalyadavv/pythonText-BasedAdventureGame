name = str(input("Enter Your Name: "))
print(f"{name} you are coding this program")
print(" You felt you are thirsty and you saw a bottle nearby but it's empty, Now you have two options")
print("1.Walk and drink water. 2.Ask Mom to fill up the bottle and pass to you")
user = int(input("Choose 1 or 2: "))
if user == 1:
    print("You did it")
elif user == 2:
    print("You are lazy af bro")
else:
    print("Please Check your input")