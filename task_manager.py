'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
from datetime import date
from datetime import datetime

#====Login Section====
with open('user.txt','r+') as user_file:
    username_list = []
    password_list = []
    inner_bool = True
    outer_bool = True
    for line in user_file:
        username, password = map(str,line.split())
        username = username.strip(',')
        username_list.append(username)
        password_list.append(password)
    while outer_bool == True:
        while inner_bool == True:
            input_username = input('Please enter a valid username: ')
            if input_username in username_list:
                inner_bool = False
            else:
                print('Incorrect username, please try again:\n')
        while inner_bool == False:
            input_password = input('Please enter a valid password: ')
            if (input_password in password_list
                and password_list.index(input_password) == username_list.index(input_username)):
                inner_bool = None
                outer_bool = False
            elif input_password == '1':
                inner_bool = True
            else:
                print('Incorrect password, please try again, or press 1 to return to username entry:\n')

#=====Menu operating blocks===========
while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if input_username != 'admin':
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

# Below menu is for Compulsory Task Part 2 for admin login
    else:
        menu = input('''\nSelect one of the following Options below:  
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
s - Statistics
: ''').lower()
        
# Block of code for creating a new user.
    if menu == 'r':
        first_bool = True
        second_bool = True
        if input_username == 'admin':                                    # This block is part of compulsory Task Part 2
            pass                                                         # To only allow admin to register new users
        else:                                                            #
            print('You are not authorized to register new users.')       #
            first_bool = False                                           #
            second_bool = False                                          #
        while second_bool == True:
            new_username = input('\nPlease enter your new username: ')
            if new_username in username_list:
                print('This user is already registered, please enter a new username: \n')
            else:
                username_list.append(new_username)
                second_bool = False
        while first_bool == True:
            new_password = input('\nPlease enter your new password: ')
            new_password_check = input('nPlease confirm your new password: ')
            if new_password == new_password_check:
                with open('user.txt','a') as user_file:
                    user_file.write(f'\n{new_username}, {new_password}')
                password_list.append(new_password)
                print("\nNew user has been registered, returning to main menu...\n")
                first_bool = False
            else:
                print('Your passwords do not match, please try again:\n')
                
# Block of code for creating new tasks           
    elif menu == 'a':
        while True:
            task_user = input('Please specify the user to whom the task has been assigned to: ')       
            if task_user in username_list:
                first_bool = True
                task_title = input("Please give the new task a title: ")
                task_description = input("Please give a short description of your task: \n\n")
                while first_bool == True:   
                    try:
                        task_date = input("Finally, please enter the final date of task submission in format 'DD MM YYYY': ")
                        task_date = datetime.strptime(task_date, "%d %m %Y").date()
                    except ValueError as ve:
                        print("The format of your date is incorrect, please try again: ")
                    else:
                        if task_date < date.today():
                            print("Your submission date is already past, please enter a new date: ")
                        else:
                            first_bool = False
                current_date = date.today().strftime("%d %b %Y")
                with open('tasks.txt','a') as task_file:
                    task_file.write(f"\n{task_user}, {task_title}, {task_description}, {current_date}, {task_date.day} {task_date.strftime('%b')} {task_date.year}, No")
                print("\nNew task added, returning to main menu...\n")
                break
            else:
                print("\nYou have entered an invalid username, please try again: ")

# Block of code for viewing all tasks
    elif menu == 'va':
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                task_list = line.split(',')
                print('---------------------------------------------------------------\n')
                print(f'Task:                     {task_list[1]}')
                print(f'Assigned to:               {task_list[0]}')
                print(f'Date assigned:            {task_list[3]}')
                print(f'Due date:                 {task_list[4]}')
                print(f'Task complete?            {task_list[5]}')
                print(f'Task description:\n{task_list[2].strip()}\n')
                print('---------------------------------------------------------------')
                print("\n")

# Block of code for viewing all tasks for the user logged in.
    elif menu == 'vm':
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                task_list = line.split(',')
                if task_list[0] == input_username: # Code line to check who is logged in.
                    print('---------------------------------------------------------------\n')
                    print(f'Task:                     {task_list[1]}')
                    print(f'Assigned to:               {task_list[0]}')
                    print(f'Date assigned:            {task_list[3]}')
                    print(f'Due date:                 {task_list[4]}')
                    print(f'Task complete?            {task_list[5]}')
                    print(f'Task description:\n{task_list[2].strip()}\n')
                    print('---------------------------------------------------------------')
                    print("\n")

# Exit block
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

# Additional block for viewing statistics. This code is only part of Compulsory task 2.
    elif menu == 's' and input_username == 'admin':
        task_count = 0
        user_count = 0
        user_list = []
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                task_list = line.split(',')
                task_count += 1
                if task_list[0] not in user_list:
                    user_count += 1
                    user_list.append(task_list[0])
        print(f"The total number of tasks is {task_count}.")
        print(f"The total number of users with tasks are {user_count}.")

# Final else statement of entire code to account for incorrect choices in the main menu.
    else:
        print("You have made a wrong choice, Please try again")

# I didn't want to convolute the code with too much commentary in between all the statements. However I will note a
# few things I did extra or differently here;
# I used try-except blocks for some areas of code to account for incorrect input.
# I also used while loops for most of my input requests to account for incorrect input.
# Additionally I added return statements in the while loops if for example the username was input correctly but no valid password,
# to not get stuck on entering a password, but to go back to entering a username again.
# Aside from this I also used lists instead of dictionaries for username and passwords to make it look cleaner and
# not take up additional memory.
# I also provided a countermeasure for making sure the right password matched with the right username, and not be able
# to log in one username with a different password, and for if a username was already registered as to not create it again.
# Submitting a new task also took datetime inputs and created it in the same format as previous tasks and did not allow
# a submission date before the current date.





































        
