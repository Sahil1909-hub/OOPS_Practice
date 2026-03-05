class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        print('Welcome to Chatbook! how would you like to continue...')
        user_input = input("""
                1) Press to Signup
                2) Press 2 to Signin
                3) Press 3 to Post
                4) Press 4 to message a friend
                5) Press any other key to exit
            """)
        
        if user_input == "1":
           pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            pass



user = chatbook() 

        
    