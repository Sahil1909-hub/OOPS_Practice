class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        print('Welcome to Chatbook! how would you like to continue...')
        user_input = input("""
                1) Press 1 to Signup
                2) Press 2 to Signin
                3) Press 3 to Post
                4) Press 4 to message a friend
                5) Press any other key to exit
            """)
        
        if user_input == "1":
           self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.mssge_friend()
        else:
            exit()


    def signup(self):
        email = input('Enter your email: ')
        pwd = input('Enter your password: ')
        self.username = email
        self.password = pwd
        print('You have signedup successfully..')
        print('\n')
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print('Please signup first by pressing 1 in the menu')
            self.menu()
        else:
            uname = input('Enter your username/email here: ')
            pas = input('Enter your password here: ')
            print(f'You have signedin successfully with {uname} username')
            self.loggedin = True
            print('\n')
            self.menu()

    def my_post(self):
        if self.loggedin == True:
            post_mssge = input('Enter your post message here: ')
            print(f'Following content has been posted -->', post_mssge)
            print('Would you like to message your friend..?')
            print('\n')
            self.menu()
        else:
            print('Signin first to post a message')
            print('\n')
            self.menu()

    def mssge_friend(self):
        if self.loggedin == True:
            frnd_name = input('Enter your friends name whom you want to message: ')
            frnd_mssge = input(f'Enter your message you want to send to {frnd_name}: ')
            print(f'Your message to {frnd_name} has been send successfully')
        else:
            print('Please Signin first to continue..')
            print('\n')
            self.menu()
    

user1 = chatbook() 

        
    