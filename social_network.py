from  social_network_classes import SocialNetwork, Person
import social_network_ui

#Create instance of main social network object
ai_social_network = SocialNetwork()

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
        elif choice == "2":
            # loggin in
            user_name = input("Username: ")
            user_password = input("Password: ")
            # if successfully logged in
            if ai_social_network.log_in(user_name, user_password):
                current_user = ai_social_network.current_user(user_name)
                while True:
                    # user menu
                    user_choice = social_network_ui.userMenu()
                    if user_choice == "1":
                        send_to = input("Send message to: ")
                        current_user.send_message(send_to, ai_social_network)
                    elif user_choice == "2":
                        inner_menu_choice = social_network_ui.manageAccountMenu()
                        # inner menu
                        while True:
                            if inner_menu_choice == "1":
                                current_user.edit_details()
                            if inner_menu_choice == "2":
                                new_friend = input("Friend name: ")
                                if ai_social_network.current_user(new_friend) not in ai_social_network.list_of_people:
                                    print("Your friend has not registered for an account")
                                else:
                                    current_user.add_friend(new_friend)
                            if inner_menu_choice == "3":
                                block_friend_name = input("Friend name: ")
                                if block_friend_name in current_user.friendlist:
                                    current_user.block_friend(block_friend_name) 
                                else: 
                                    print(block_friend_name, "does not exist in your friend list")
                            if inner_menu_choice == "4":
                                current_user.view_all_friend()
                            if inner_menu_choice == "5":
                                current_user.view_all_message()    
                            if inner_menu_choice == "6":
                                break
                            else:
                                break
                    elif user_choice == "3":
                        break
                    else: 
                        break
            # if not successfully logged in
            else:
                print("")
                print("********************************************************")
                print("Username or password is incorrect")
                print("Please retry")   
        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Your input is invalid. Try Again!")
        #restart menu
        choice = social_network_ui.mainMenu()
        
