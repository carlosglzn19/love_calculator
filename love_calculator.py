print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") # What is your name?
name2 = input("What is their name?\n") # What is their name?

#Combine both names in lower case to have only one string
combined_names = name1.lower() + name2.lower()

#counting true letters in both names
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

#counting love letter in both names
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e

#Getting the score
score = str(first_digit) + str(second_digit)

#Interpretation of the score
if int(score) < 10 or int(score) > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")