# UniBuddy Project - bot for University students 
# Data Science project
# New update

print('''
      Hello! Wecome to the University! \n
      Please enter your details to get started :
      ''')


while True:
    try:
        user_name = input("Please enter your student name :").capitalize()
        user_age = int(input("Please enter your age : "))
        fav_colour = input ("Please enter your favourite colour - Red, Blue, or Yellow :").capitalize()

        if not user_name.isalpha():
            print("You have entered a wrong name. Please try again.")
        elif not fav_colour.isalpha():
            print("You have entered a wrong colour. Please try again")
        else: 
            print(f"Hi {user_name}! Welcome to the University")
            break
    except ValueError as e:
            print(e)
            print("You have not entered a number")


print(f"""
     Welcome {user_name}! I see that your favourite colour is {fav_colour}.
     I have a few suggestions based on your choice!
      
      """)

if fav_colour == 'Red':

    print("If you like the colour RED, I have the following suggetions for you! Check out :")

    print("""
    1. Our red colour themed rugby club.
    2. Our red themed design club.
    3. Our strawberry farming club.
    4. Our Chinese Opera club.
    5. Our political debate club.
          
          """)
elif fav_colour == 'Blue':

    print("If you like the colour BLUE, I have a few recommendations for you: ")

    print ("""
    1. Our Blue squid swimming club.
    2. Our Bow and Arrow club.
    3. Our Blue themed Taekwondo club.     
    4. Our deep sea exploration society.
    5. Our blue bird evironmental sociery.  
                
           """)
elif fav_colour == 'Yellow':
    print("If you like the colour YELLOW, please find below our recommendations for you :")
    print("""
    1. Our yellow planet exploration club.
    2. Our Sand and Velo club.
    3. Our Sun lowers club.
    4. Our countryside challenge club.
    5. Our Smiling design club.        

          """)

else: 
    print("I'm not sure if that is the colour you entered.")

if user_age <=22 :

    print("Here are some freshment specific events : ")
    print("""
    1. Meet your friends on Thursday.
    2. Cycle together meet-up.
    3. Library exploration meeting.
    4. Modern dance evening.
          
          """)


#question = input("""Welcome to our FAQ (frequently asked questions) section!
#      Please ask your question :
      
#      """)
    
def question_match(faq_list: list, index: int) -> None:
    if index ==0:
        print(f"You have chosen: {faq_list[index]}")
        print("It's on the right of the main building, down the road.")
    elif index ==1:
        print(f"You have chosen: {faq_list[index]}")
        print("The cafeteria is on the main street on the left, 50 meters from the main building.")
    elif index==2:
        print(f"You have chosen: {faq_list[index]}")
        print("The Gym is on the side street on the right, 100 meters from the main building.")
    elif index==3:
        print(f"You have chosen: {faq_list[index]}")
        print("Classes start at 9 am.")
    elif index==4:
        print(f"You have chosen: {faq_list[index]}")
        print("The cafeteria is open from 8 am until 8 pm.")
    elif index==5:
        print(f"You have chosen: {faq_list[index]}")
        print("The details of wifi access are on the Student desk in the Main building.")
    elif index==6:
        print(f"You have chosen: {faq_list[index]}")
        print("The nearest coffee shop is 100 meters from the East gate.")
    elif index==7:
        print(f"You have chosen: {faq_list[index]}")
        print("The admissions office is in the Main building on the left from the entrance.")
    else:
        print("You have entered a wrong number. Please try again.")
    return None



def questionnaire_answers() -> None:
    # Load faq_list
    faq_file = open("input.txt", "r")
    faq_list = []#this is a list
    for lines in faq_file:
        temp = lines.strip('\n')
        temp = temp.split()
        joined = " ".join(temp)
        faq_list.append(joined)
    #Enumerated questions
    print("This is a list of our most frequently asked questions.")
    for count, quest in enumerate(faq_list, start = 1):
        print(f"{count}.{quest}")
    answer_more = True
    while answer_more:
        choice = int(input("Please enter the number question you want to ask :"))
        index = choice - 1
        question_match(faq_list=faq_list, index=index)
        answer_more = int(input("Would you like to anwer another question? [1-yes, 0-no]"))
    print("Good luck!")
    return None


if __name__=="__main__":
    questionnaire_answers()