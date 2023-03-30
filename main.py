print("One-Million-To-One")
print("Guess a number between 1 to 1 million")

i = 0

while True:
  i += 1
  guess = int(input("What is your guess?: "))
  if guess == 50000:
    print("Correct!")
    print("It took you", i, "guess to get it correct!")
    break
  elif guess < 50000 and guess > 0:
    print("Too low")
    continue
  elif guess > 50000:
    print("Too high")
    continue
  elif guess < 0:
    print("REALLY??")
    exit()
  else:
    print("Err.. I think you put the wrong input")
    continue