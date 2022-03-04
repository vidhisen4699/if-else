# Que). write a code Login_Page using (multiple choise) if....else   

print ("Hello and welcome to Billing Pro, please enter your username and password to access the database.")

username = input ("Enter username:")

if username == "cking" or "doneal" or "mcook":
  print ("Valid username.")
else:
  print ("Invalid username. Please try again.") 


password = input ("Enter password:")

if password == "rammstein1" or "theory1" or "tupac1":
  print ("Valid password. User has been verified.")
else:
  print ("Invalid password. Access denied.")