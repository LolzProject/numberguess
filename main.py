# BTW, I am copy and pasting the code in, so all packages are already installed to the base software.

number = random.randint(0, 10)
correct = false
print("Guess a number from 0 to 10!")
while correct == False:
  option = input("GTN>>> ")
  if int(option) == number:
    correct = True
    print("Correct! :D")
  elif int(option) != number:
    print("Incorrect.")
  elif option == "quit":
    print("Okay!")
    correct = True
    print("Closed GuessTheNumber.")
  else:
    print("Invalid input, either string or nothing.")
    print("Try again.")
