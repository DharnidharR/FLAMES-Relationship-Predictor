def flames_calculator(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    
    for letter in name1:
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)    
    total_letters = len(name1) + len(name2)
    
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    temp = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    result = 0
    while(len(temp)!=1):
        result = (result + total_letters -1 )% len(temp)
        temp.pop(result)
    
    return temp[0]

botName = "Bot"
print(f"{botName}: Haii !! I am FLAMES Chatbot... \n{botName} : I am excited to know your name")
userName = input("USER: Enter Your Name : ")
user_email_id = input(f"{userName}: Enter Mail id : ")
print(f"Bot: Hi {userName} , Let's get to know each other! \n{botName}: I'm a chatbot created by BYD , and my superpower is predicting relationships between two names. \n{botName}: It might sound a little silly, but hey, it's the silly things that make life fun, don't you think?")


uName = input(f"{botName}: Enter name that i can call : ")
print(f"{botName}: Nice to meet you, {uName}! What would you like to call me? ")
botName = input(f"{userName}: ")
print(f"{botName}: Awesome! From now on, you can call me {botName}. Let's get started, {uName}! 🔥")
print(f"{botName}: Alright, {uName}, let's dive into the FLAMES game! I'll predict the relationship between two names.")

while(True):
    print(f"{botName}: First things first, what's the first Person's name? ")
    name1 = input(f"{userName}: ")
    print(f"{botName}: Got it! {name1} is in the house! 🎤")
    print(f"{botName}: And what's the second Person's name? ")
    name2 = input(f"{userName}: ")
    print(f"{botName}: Alright, {name2} is here too! Let's see what the future holds for {name1} and {name2}. 🔮\n{botName}: Any Guess..?? ")
    sel = input(f"{userName}: (Yes/No) : ").lower()
    if(sel == 'no'):
        print(f"{botName}: Oh come on, {uName}! Don't be shy. Take a wild guess! 😜")
    if(sel == 'yes'):
        print(f"{botName}: Thats nice.. Tell me your guess, Let's see whether you guessed it Right...")
    guess = input(f"{userName}: (Friends/Lovers/Affection/Marriage/Enemies/Siblings) : ")
    print(f"{botName}: Hmmm, {guess} ? 🤔.. Interesting. Let's see if you are Right.\n{botName}: Enter 'Start'")
    start = input(f"{userName}: ")
    result = flames_calculator(name1, name2)

    if result == "Friends":
        print(f"{botName}: {name1} and {name2} are Friends! Besties forever! 🤝")
        print(f"{botName}: Friendship is the only cement that will ever hold the world together.")
    elif result == "Lovers":
        print(f"{botName}: {name1} and {name2} are Lovers! Ooo la la! 💖")
        print(f"{botName}: Someone's got a crush! Time to confess your feelings! 😉")
    elif result == "Affection":
        print(f"{botName}: {name1} and {name2} have Affection! Someone's blushing! 😊")
        print(f"{botName}: This could be the start of something beautiful!")
    elif result == "Marriage":
        print(f"{botName}: {name1} and {name2} are destined for Marriage! Ring the bells! 💍")
        print(f"{botName}: Start planning the wedding! I'll bring the cake! 🎂 ")
    elif result == "Enemies":
        print(f"{botName}: {name1} and {name2} are Enemies! Uh-oh, better stay away! 😠")
        print(f"{botName}: We can detroy our enemies when we make them our friends... Chill with them")
    elif result == "Siblings":
        print(f"{botName}: {name1} and {name2} are Siblings! Family goals! 👨‍👩‍👧‍👦")
        print(f"{botName}: No fighting over the remote control, okay? 😂")


    # To Store the names that was used to calculate FLAMES in TXT file
    file_path = r"Flames_Result.txt"
    with open(file_path, 'a') as file:
        file.write(f"{name1} : {name2} = {result}\n")


    print(f"{botName}: That was fun, {uName}! Want to try again with different names? ")
    play_again = input(f"{userName}: (Yes/No) ").lower()
    if play_again != "yes":
        print(f"{botName}: Thanks for playing, {uName}! See you next time!")
        break
    else:
        print(f"{botName}: Awesome! Let's do this again! 🔥💫")
        print(f"{botName}: Waittt!!! 🤔'\n'{botName}: What if you have many names in your list to check for FLAMES ?? ")
        print(f"{botName}: If there is 1 name Enter (1)'\n'{botName}: If there is more than 1 names Enter (2)")
        ttt = input(f"{userName}: Enter 1 or 2 : ")
        if(ttt == 1):
            continue
        else:
            name1 = input(f"{userName}: Enter your name : ")
            print(f"{botName}: wonderfull..... Enter all names seperated by comma")
            nameList = input(f"{userName}: Enter Names : ")
            nameList = nameList.replace(" ","")
            nameList = list(map(str , nameList.split(",")))
            nameCount = len(nameList)
            for i in range (nameCount):
                name2 = nameList[i]
                result = flames_calculator(name1, name2)
                print(f"FLAMES relation between {name1} & {name2} is {result}")
            print(f"{botName}: Thanks for playing, {uName}! See you next time!")
            break