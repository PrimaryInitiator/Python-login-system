import time

loginDB = [
    ["Owner" , "owner" , "Admin"],
    ["Admin" , "password" , "Admin"],
    ["User" , "qwerty" , "Default"],
    ]

commentsDB = [
    ["Welcome to the Forum! Please be Kind and Civil", "- The Owner"]

]


def login():
    global LoggedIn
    LoggedIn = False

    global AdminPermissions
    AdminPermissions = False
    LoginCounter = 0

    while LoggedIn == False:
        username = input("Enter your username:")
        password = input("Enter your password:")

        for i in range (len(loginDB)):
            if username == loginDB[i][0] and password == loginDB [i][1]:
                LoggedIn = True
                print("Welcome back",loginDB[i][0],"!")
                global CurrentUser
                CurrentUser = loginDB[i][0]
                if loginDB[i][2] == "Admin":
                    AdminPermissions = True

        if LoggedIn == False :
            print("Login Incorrect. Please try again.")
            LoginCounter +=  1
            if LoginCounter-3 == 0 :
                print ("You have been locked out. Please wait for one minute to try again.")
                time.sleep(60)
            


def addUser():
    newUserName : str = input("Enter the new users username: ")
    newPassword : str = input("Enter the new users password:")
    newUserPerm : bool = input("Enter the Permission Level (Default , Admin):")

    loginDB.append ([newUserName , newPassword , newUserPerm]) 

def delUser():
    userToRemove = input("Enter a username to remove:")
    for i in range (len(loginDB)):
        if loginDB[i][0] == userToRemove:
            loginDB.pop(i)
            print("User Removed")
            return 
        
    print("User not found.")

def viewDataBase():
    print(*loginDB)
    

def AdminPermissionsCheck():
    if AdminPermissions == True :
        print("Access Granted")
        return True
    else :
        print("Insufficent Permissions")
        return False
            
def viewComments():    
    formatted_comments = [f'"{comment[0]}" by {comment[1]}' for comment in commentsDB]
    print(", ".join(formatted_comments))



def action():
    global LoggedIn 
    userAction = input("Would you like to: Access the Admin Section (Administration), View the comment wall (View) Leave a comment (Comment) or Logout (Logout) ...") 
    
    if userAction == "Administration" and AdminPermissionsCheck() == True:
        AdminAction = input("Would you like to: Add a new user (Add), Delete an existing user (Delete) or View database (Database)")
        
        if AdminAction == "Add":
            addUser()
        elif AdminAction == "Database":
            viewDataBase()
        elif AdminAction == "Delete":
            delUser()
        
#     elif userAction == "Change password":
    elif userAction == "Comment":
        userComment = input("What would you like to comment?")
        commentsDB.append([userComment , "-", CurrentUser,]) 


    elif userAction == "Logout":
        LoggedIn = False
        login()

    elif userAction == "View":
        viewComments()

login()
while LoggedIn == True:
    action()    




