from users import User
import getpass

while True:
    print("""-------------<<main menu>>-------------------
             * Termination of the program -->0
             * Registration -->1
             * Login -->2
          """)

    option = input("select your option:")

    match option:
        case "0":
            break
        case "1":
            username = input("Please enter your username:")
            password = input("Please enter your password:")
            phone = input("Please enter your phone number:")

            User.signup(username, password, phone)

        case "2":
            username = input("Please enter your username:")
            password = input("Please enter your password:")
            User.login(username, password)
            if User.login(username,password):
                while True:
                    print("""-------------<<Menu>>-----------------
                            * User information -->1
                            * Edit user information -->2
                            * Changing the password -->3
                            * Back to main menu -->4""")
                    option2 = input("select your option:")

                    match option2:
                        case "1":
                            user = User.datauser.get(username)
                            if user:
                                print(f"Username: {user.username}")
                                print(f"Phone number: {user.phone_number}")
                            else:
                                print("User not found")

                        case "2":
                            new_username = input("Please enter your new username (press enter to skip):")
                            new_phone = input("I apologize for the incomplete response earlier. Here's the complete corrected code:")

                        case "3":
                            username = input("please enter your username")
                            new_password = getpass.getpass("Please enter your password:")
                            new_password1 = getpass.getpass("please enter your password agin:")
                            if new_password == new_password1:
                                User.edit_password(new_password, username)

                        case "4":
                            break
            else:
                break



