import random

num_of_tries = 0

randNum = random.randint(1, 10)

while True:
  try:
    user_input = int(input("Guess the number from 1 to 10: "))
  except:
    print("Please enter a valid number from 1 to 10!")
    continue
  
  num_of_tries += 1

  if user_input < randNum:
    print("Higher!")
  elif user_input > randNum:
    print("Lower!")
  else:
    msg = ""
    if num_of_tries > 1:
      msg = "tries"
    else:
      msg = "try"
    print(f"Correct! The secret number is {randNum}! It took you {num_of_tries} {msg}.\nThank you for playing!")
    break