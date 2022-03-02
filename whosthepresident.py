
def election2():


    # a quiz with 2 questions and answers based on on such.

    x = input("Who's the President? ")

    #A questioning of the user's answer'
    print (f'{x}, huh?')
    #if the answer is anthing other than Joe Biden or Biden, it's wrong.. WIll replace
    # time/date string with actual time/date in the near future with countdown until Jan 20, 2025.

    #If has to be typed with repeated x== conditions
    if x == "Joe Biden" or x =="Biden":
        print (f"{x}? That's right.")
    elif x == "Donald Trump" or x == "Trump" or x =="DT" or x == 'God Emperor Trump':
        print("Nah, this insurrectionist is not the President.")
    else:
        print("Nah, the President is Joe Biden, until at least Jan 20, 2025.")
    # y = second question. If the answer isn't no, it's wrong.
    y = input("Was there massive evidence of voter fraud? ")
    if y == "no" or y == 'nope' or y =='nah' or y =="negative":
        print("That's right, that was bull.") 
    else: 
        print("No there wasn't.")

    exit()



election2()


'''
def election():


    # a quiz with 2 questions, with 1 right and wrog answer, and answers based on on such.

    x = input("Who's the President? ")

    #A questioning of the user's answer'
    print (x + "?")
    if x == "Joe Biden":
        print ("Good job")
    elif x == "Donald Trump" or "Trump" or "DT":
        print("You've been lied to, unfortunately")
    y = input("Was there massive evidence of voter fraud? ")
    if y == "yes":
        print("No there wasn't")
    elif y == "no":
        print("That's right, that was bull.")

    exit()

election()
'''






