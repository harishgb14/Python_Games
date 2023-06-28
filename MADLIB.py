#MADLIB
#It is word game
#Like string concatenation
#Suppose we want to create that says "subscribe to ____________"

#Youtuber="Harshit Tech"

#some ways to do that
#print("Subscribe to "+Youtuber)
#print("Subscribe to {}".format(Youtuber))
#print(f"Subscribe to {Youtuber}")

name=input("Enter the name :")
Course=input("Course:")
job=input("Job:")
skills=input("Skills:")
madlib= f"Hi this is {name}.I am from {Course}.I am looking forward for a job in {job}.And I am good at {skills}.\
Thank you! "

print(madlib)