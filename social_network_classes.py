# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:

    # store all accounts that have been created
    def __init__(self):
        self.list_of_people = []

    ## For more challenge try this
    # def save_social_media(self, user):
        # json = json.dumps(user.__dict__)
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        # socialMedia = json.dump(user)
        # print(socialMedia)

    ## For more challenge try this
    # def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        # pass

    def log_in(self, user_name, user_password):
        for x in self.list_of_people:
            if user_name == x.username and user_password == x.password:
                    print("Hi. Welcome, ", user_name)
                    return True
        return False
    
    def current_user(self, user_name):
        for x in self.list_of_people:
            if user_name == x.username:
                    return x
            
    def  create_account(self):
        print("Creating ...")
        name = input("Name: ")
        age = input("Age: ")
        username = input("Username: ")
        password = input("Password: ")
        user = Person(name, age, username, password)
        self.list_of_people.append(user)
        # to check if a new account is added to list_of_people
        # for x in range(len(self.list_of_people)):
            # print(self.list_of_people[x].name)
    
class Person:
    def __init__(self, name, age, username, password):
        self.name = name
        self.year = age
        self.username = username
        self.password = password
        self.friendlist = []
        self.inbox = []

    def edit_details(self):
        new_age = input("Enter new age: ")
        self.year = new_age
        new_name = input("Enter new name: ")
        self.name = new_name
        new_username = input("enter new username: ")
        self.username - new_username
        new_password = input("Reset password: ")
        self.password = new_password

    def add_friend(self, friend_name):
        self.friendlist.append(friend_name)

    def view_all_friend(self):
        print("Friend list: ")
        for friend in range(len(self.friendlist)):
            print(self.friendlist[friend])

    def block_friend(self, block_friend_name):
        self.friendlist.remove(block_friend_name)
        
    def send_message(self, friend_name, ai_social_network):
        message = input("Message: ")
        if friend_name not in self.friendlist:
            print(friend_name, "does not exist in your friend list")
        else:
            print("To ", friend_name, ": ", message)
            receiver = ai_social_network.get_person_object(friend_name)
            sender_info = "From " + str(self.name) + ": "
            receiver.inbox.append(sender_info)
            receiver.inbox.append(message)
            
    def view_all_message(self):
        print("My messages: ")
        for message in range(len(self.inbox)):
            print(self.inbox[message])
