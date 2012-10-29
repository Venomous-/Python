start = raw_input ("V1 or V2: ").capitalize()
if start == "V1":
    question = raw_input ("What is your name: ")
    print "Oh, hello, " + question.capitalize() + "."
elif start == "V2":
    question = raw_input ("What is your name: ").capitalize()
    print "Oh, hello, {0}!".format(question)