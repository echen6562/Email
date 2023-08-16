# function:   valid_username
# input:      a username (string)
# processing: determines if the username supplied is valid.  for the purpose
#             of this program a valid username is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) the first character cannot be a number
# output:     boolean (True if valid, False if invalid)

def valid_username(username):
    length = len(username)
    if length < 5:
        return False
    anumeric = str.isalnum(username)
    if anumeric == False:
        return False
    first = username[0]
    if str.isnumeric(first) == True:
        return False
    return True

# function:   valid_password
# input:      a password (string)
# processing: determines if the password supplied is valid.  for the purpose
#             of this program a valid password is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) must contain at least one lowercase letter
#             (4) must contain at least one uppercase letter
#             (5) must contain at least one number
# output:     boolean (True if valid, False if invalid)

def valid_password(password):
    length = len(password)
    if length < 5:
        return False
    anumeric = str.isalnum(password)
    if anumeric == False:
        return False
    if str.isnumeric(password) == True or str.isalpha(password) == True:
        return False
    upper = 0
    for x in password:
        if str.isalpha(x) == True:
            if str.upper(x) == x:
                upper += 1
    if upper == 0:
        return False
    lower = 0
    for x in password:
        if str.isalpha(x) == True:
            if str.lower(x) == x:
                lower += 1
    if lower == 0:
        return False
    for x in password:
        if str.isnumeric(x) == True:
            return True

# function:   username_exists
# input:      a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:     boolean (True if found, False if not found)

def username_exists(username):
    userinfofile = open("user_info.txt", "r")
    userinfo = userinfofile.read()
    splitinfo = userinfo.split("\n")
    for x in splitinfo:
        index = x.find(",")
        if username in x[:index]:
            if username == "":
                return False
            return True
    return False

# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)

def check_password(username,password):
    userinfofile = open("user_info.txt", "r")
    userinfo = userinfofile.read()
    splitinfo = userinfo.split("\n")
    for x in splitinfo:
        index = x.find(",")
        if username in x[:index]:
            if username == "":
                return False
            if password in x[index+1:]:
                return True
    return False

# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given users
#             with the following information:
#
#             sender|date_and_time|message\n
#
#             for example, if you call this function using the following arguments:
#
#             send_message('craig', 'pikachu', 'Hello there! nice to see you!')
#
#             the file 'messages/pikachu.txt' should gain an additional line data
#             that looks like the following:
#
#             craig|11/14/2020 12:30:05|Hello there! nice to see you!\n
#
#             note that you can generate the current time by doing the following:
#
#             import datetime
#             d = datetime.datetime.now()
#             month = d.month
#             day = d.day
#             year = d.year
#             ... etc. for hour, minute and second
#
#             keep in mind that you may need to 'append' to the correct messages file
#             since a user can receive an unlimited number of messages.  you may also
#             need to create a new message file if one does not exist for a user.
# output:     nothing

def send_message(sender,recipient,message):
    import datetime
    d = datetime.datetime.now()
    month = str(d.month)
    day = str(d.day)
    year = str(d.year)
    hour = str(d.hour)
    minute = str(d.minute)
    second = str(d.second)
    inbox = open('messages/' + (recipient) + '.txt', 'a')
    fullmessage = (sender + "|" + month + "/" + day + "/" + year + " " + hour + ":" + minute + ":" + second + "|" + message + "\n")
    inbox.write(fullmessage)
    inbox.close()

# function:   add_user
# input:      a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output:     boolean (True if added successfully, False if not)

def add_user(username,password):
    if username_exists(username) == True:
        return False
    userinfofile = open("user_info.txt", "a")
    user = (username + "," + password)
    userinfofile.write(user)
    userinfofile.write("\n")
    userinfofile.close()
    send_message('admin', username, 'Welcome to your account!')
    return True

# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.  assume you have this file named 'pikachu.txt':
#
#             charmander|11/14/2020 13:37:15|Hey there!
#             charmander|11/14/2020 13:37:15|You too, ttyl
#
#             this function should generate the following output:
#
#             Message #1 received from charmander
#             Time: 11/14/2020 13:37:15
#             Hey there!
#
#             Message #2 received from charmander
#             Time: 11/14/2020 13:37:15
#             You too, ttyl
# output:     no return value (simply prints the messages)

def print_messages(username):
        inbox = open('messages/' + (username) + '.txt', 'r')
        inboxmsg = inbox.read()
        splitmsg = inboxmsg.split('\n')
        msgnum = 0
        for x in splitmsg:
            if x == "":
                continue
            msgnum += 1
            index1 = x.find("|")
            print("Message #", msgnum, " received from ", x[:index1], sep="")
            index2 = x[index1+1:].find("|")
            print("Time:", ((x[index1+1:])[:index2]))
            print((x[index1+1:])[index2+1:], end="\n\n")
        inbox.close()

# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value

def delete_messages(username):
    inbox = open('messages/' + (username) + '.txt', 'w')
    inbox.write("")
    inbox.close()

# I use a while loop that will be broken when the user quits
while True:
# I ask the user for an option input, and I data validate it
    option = input("(l)ogin, (r)egister or (q)uit: ")
    while option != "l" and option != "r" and option != "q":
        print("Invalid option, please try again", end="\n\n")
        option = input("(l)ogin, (r)egister or (q)uit: ")
    print()
# Depending on the option input, the program will either ask for a login, registration,
# or quit the program
    if option == "l":
        print("Log In")
        username = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")
# I make sure that the username exists and that the password input corresponds
# to the username input
        if username_exists(username) == False:
            print("Username is invalid, login cancelled", end="\n\n")
            continue
        if check_password(username,password) == False:
            print("Password is invalid, login cancelled", end="\n\n")
            continue
        if username_exists(username) == True and check_password(username,password) == True:
            print()
            while True:
# If the username exists and the password is valid, the user will be prompted to
# input another option, either read their messages, send a message, delete their
# messages, or logout
                print("You have been logged in successfully as", username)
                loginoption = input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ")
                while loginoption != "r" and option != "s" and option != "d" and option != "l":
                    print("Invalid option, please try again", end="\n\n")
                    loginoption = input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: ")
                if loginoption == "r":
                    print()
                    userinfofile = open('messages/' + username + ".txt", "r")
                    userinfo = userinfofile.read()
                    if userinfo == "":
                        print("No messages in your inbox", end="\n\n")
                    else:
                        print_messages(username)
                if loginoption == "s":
                    recipient = input("Username of recipient: ")
                    if username_exists(recipient) == False:
                        print("Unknown recipient", end ="\n\n")
                        continue
                    message = input("Type your message: ")
                    send_message(username, recipient, message)
                    print("Message sent!", end="\n\n")
                if loginoption == "d":
                    delete_messages(username)
                    print("Your messages have been deleted", end="\n\n")
                if loginoption == "l":
                    print("Logging out as username", username, end="\n\n")
                    break
# If the option chosen is to register, I will ask the user for a username and password
# and if both are valid and original, the account wil be created
    elif option == "r":
        print("Register for an account")
        username = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")
        if username_exists(username) == True:
            print("Duplicate username, registration cancelled", end="\n\n")
            continue
        if valid_username(username) == False:
            print("Username is invalid, registration cancelled", end="\n\n")
            continue
        if valid_password(password) == False:
            print("Password is invalid, registration cancelled", end="\n\n")
            continue
        if username_exists(username) == False and valid_username(username) == True and valid_password(password) == True:
            print("Registration successful", end="\n\n")
            add_user(username,password)
# If the option is to quit, the while loop will break
    elif option == "q":
        print("Goodbye!")
        break


