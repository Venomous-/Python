#Ask for first and last name, House address, Zip Code/Pin Code, and City.
#Also ask for country\


#Import time (quite obvious)
import time

#Ask for the country, if united states ask for the zip code, if not ask for postal code
country = raw_input("Which country do you live in? (Full country name please):").lower()
if country == "united states":
    zipCode = raw_input("What is your zip code?:")
else:
    zipCode = raw_input("What is your postal code?:")
    
#Ask for the city and state
state = raw_input("What state/province do you live in?:")
city = raw_input("What city do you live in?:")
#Ask for the first and last name
firstName = raw_input("What is your first name?:")
lastName = raw_input("what is your last name?:")

#Ask for the house address
houseAddress = raw_input("What is your house address?:")

#Final statement
print "Hello, {0} {1}! It's nice to know that you are from {2}! Your zip/postal code is {3}!".format(firstName, lastName, country, zipCode)
time.sleep(5)
print "Wow, thanks for waiting! You are from the city of {0}, and the state/province of {1}!".format(city, state)
time.sleep(5)
print "Your house address is {0}!".format(houseAddress)