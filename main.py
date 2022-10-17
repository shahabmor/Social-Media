from user import User
from saving_engine import save, load

logo = '''

   __  ___       ____         _      __  _  __    __                  __  
  /  |/  /_ __  / __/__  ____(_)__ _/ / / |/ /__ / /__    _____  ____/ /__
 / /|_/ / // / _\ \/ _ \/ __/ / _ `/ / /    / -_) __/ |/|/ / _ \/ __/  '_/
/_/  /_/\_, / /___/\___/\__/_/\_,_/_/ /_/|_/\__/\__/|__,__/\___/_/ /_/\_\ 
       /___/                                                              
                                                                  
''' + "\n"*5


# basic information ----------------------------------------------------------------------------------------------------
# file actions ---------------------------------------------------------------------------------------------------------
data = load()

list_of_users = []

try:
    for id_account in data:
        new_user = User(id_account)
        new_user.name = data[id_account]['name']
        new_user.email = data[id_account]['email']
        new_user.password = data[id_account]['password']
        new_user.posts = data[id_account]['post']
        new_user.following = data[id_account]["followings"]
        new_user.followers = data[id_account]["followers"]
        list_of_users.append(new_user)

except:
    # due to this action nobody can use owner ID

    OWNER = User('Owner')
    OWNER.name = "Shahab Moradi"
    save(OWNER)
    list_of_users.append(OWNER)


# general functions-----------------------------------------------------------------------------------------------------
def clear():
    print("\n" * 50)


# basic functions ------------------------------------------------------------------------------------------------------
def add_new_user(users):
    """this function create a new account and append it to list of users"""
    valid = False
    while not valid:

        new_id = input("\n\nID Account: ")
        valid = True

        for old_user in users:
            if new_id == old_user.id:
                print("Sorry this ID has already taken, please enter a new ID")
                valid = False

        if valid:
            new_user = User(new_id)
            new_user.get_name()
            new_user.get_email()
            new_user.get_password()
            list_of_users.append(new_user)
            save(new_user)
            print("A new account has been created\n\n")


def login(users):
    """this function gets id and password from user and turn the direction to related page"""
    valid = False
    while not valid:

        user_id = input("\n\nID Account: ")
        password = input("Password:")

        for user in users:
            if user_id == user.id and password == user.secret_password:
                valid = True
                clear()
                user_page(user)

        print("Password does not match ID Account! Try again.")

# -----------------------------------------search related functions-----------------------------------------------------
# search
def search():
    """this function takes an ID and shows basic information about that ID account"""
    done = False
    while not done:

        clear()

        for index in range(len(list_of_users)):
            print(f"{index+1}#  {list_of_users[index].id}")

        search_direction = input("\ntype 'Back' to back to your page\n"
                                 "See posts(Enter ID): ")

        if search_direction.lower() == "back":
            done = True

        for user in list_of_users:
            if user.id.lower() == search_direction.lower():
                target_id(user)
                done = True


# target id
def target_id(user):

    clear()

    done = False
    while not done:

        header(user)
        target_id_direction = input("\n\n1: See posts\n"
                                    "2: Back\n\n"
                                    "Enter: ")

        if target_id_direction.lower() == "see posts":
            clear()
            posts(user)
            print("\n\n")

        elif target_id_direction.lower() == "back":
            done = True


# user functions--------------------------------------------------------------------------------------------------------
# ----------------------------------------- posts related function------------------------------------------------------
def my_posts(user):
    in_posts = True
    while in_posts:

        clear()
        posts(user)

        posts_related_direction = input("\n\n1# New post\n"
                                        "2# Delete post\n"
                                        "3# Back\n\n"
                                        "Enter: "
                                        )

        if posts_related_direction.lower() == "new post":
            new_post(user)

        elif posts_related_direction.lower() == "delete post":
            delete_post(user)

        elif posts_related_direction.lower() == "back":
            in_posts = False


# posts
def posts(user):
    """this function shows the related user posts"""
    print("############posts#############\n\n")
    if len(user.posts) == 0:
        print("There is no post here!")

    else:
        for i in range(len(user.posts)):
            print(f"{i + 1}#  {user.posts[i]}")


# New post
def new_post(user):
    """this function takes a new string from user and append it as a new post"""
    post = input("Enter new post: ")
    user.posts.append(post)
    save(user)


# delete post
def delete_post(user):
    index = int(input("\nPost's Index: "))
    user.posts.pop(index-1)
    save(user)

# ----------------------------------------- follow related functions ---------------------------------------------------
# Follow new account
def follow_new_account(user):
    """this function takes an id from user and append that to following list, if it has not followed by user"""
    valid = False
    while not valid:

        follow = True

        target_id = input("\ntype 'Back' to back to your page\n"
                          "Enter ID: ")

        if target_id.lower() == "back":
            valid = True
            follow = False

        for following in user.following:
            if following == target_id:
                print("You have already follow this account!\n")
                follow = False

        if follow:
            done = False
            for account in list_of_users:
                if account.id == target_id:
                    user.following.append(target_id)
                    account.followers.append(user.id)
                    save(user)
                    save(account)
                    done = True
                    print(f"You follow {target_id} successfully!\n")

            if not done:
                print("There is no account with this ID\n")


# Show followers
def show_followers(user):

    """this function shows who follow the user"""
    if len(user.followers) == 0:
        print("Nobody follows you!")

    else:
        for index in range(len(user.followers)):
            print(f"{index + 1}# {user.followers[index]}")

        done = False
        while not done:
            user_choice = input("\ntype 'Back' to back to your page\n"
                                "See posts(Enter ID): ")

            if user_choice.lower() == "back":
                done = True

            for follower in list_of_users:
                if follower.id == user_choice:
                    posts(follower)


# Show followings
def show_followings(user):
    """this function shows following accounts and their post(if you want)"""
    if len(user.following) == 0:
        print("You follow nobody!")

    else:
        for index in range(len(user.following)):
            print(f"{index + 1}# {user.following[index]}")

        done = False
        while not done:
            user_choice = input("\ntype 'Back' to back to your page\n"
                                "See posts(Enter ID): ")

            if user_choice.lower() == "back":
                done = True

            for following_user in list_of_users:
                if following_user.id == user_choice:
                    posts(following_user)


# -------------------------------------------edit related functions ----------------------------------------------------
# edit function
def edit(user):
    done = False
    while not done:

        clear()
        header(user)

        edit_related_direction = input("\n\nEdit\n"
                                       "1# Name\n"
                                       "2# Email\n"
                                       "3# Password\n"
                                       "4# Back\n\n"
                                       "Enter: ")

        if edit_related_direction.lower() == "name":
            user.get_name()

        elif edit_related_direction.lower() == "email":
            user.get_email()

        elif edit_related_direction.lower() == "password":
            user.get_password()

        elif edit_related_direction.lower() == "back":
            save(user)
            done = True


# user page-------------------------------------------------------------------------------------------------------------
def header(user):
    print(f"{user.name}'s Page!\n")
    print(f"Username: {user.id}")
    print(f"Email: {user.email}")
    print(f"Posts: {len(user.posts)}")
    print(f"Followers: {len(user.followers)}")
    print(f"Followings: {len(user.following)}")

def user_page(user):

    in_page = True

    while in_page:
        clear()
        header(user)

        user_direction = input("\n\n\n1: My posts\n"
                               "2. Follow new account\n"
                               "3: Followers\n"
                               "4: Followings\n"
                               "5: Edit\n"
                               "6: Back\n\n"
                               "Enter: "
                               )

        if user_direction.lower() == "my posts":
            my_posts(user)

        elif user_direction.lower() == "follow new account":
            follow_new_account(user)

        elif user_direction.lower() == "followers":
            show_followers(user)

        elif user_direction.lower() == "followings":
            show_followings(user)

        elif user_direction.lower() == "edit":
            edit(user)

        elif user_direction.lower() == "back":
            in_page = False


# main -----------------------------------------------------------------------------------------------------------------
app_is_on = True
while app_is_on:

    clear()
    print(logo)

    direction = input("1: Add new user\n"
                      "2: Login\n"
                      "3: Search\n"
                      "4: Exit\n\n"
                      "Enter: "
                      )

    if direction.lower() == "add new user":
        add_new_user(list_of_users)

    elif direction.lower() == "login":
        login(list_of_users)

    elif direction.lower() == "search":
        search()

    elif direction.lower() == "exit":
        for user in list_of_users:
            save(user)
        app_is_on = False
