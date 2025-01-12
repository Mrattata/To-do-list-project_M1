def display():

    """ this funbction is the display menu and returns the users input """

    print('Welcome to My To Do List! \n')
    print('\t Add Tasks:  type add \n')
    print('\t Delete Tasks:  type delete \n')
    print('\t View all Tasks:   type view\n')
    print('\t Quit:  type quit \n')
    
    #this is my validation for the user input, making sure there is no error with it

    try:

        choice=input('What would you like to do? \n')

        choice=choice.lower()

        choice=choice.strip()

        if choice!='add' and choice!='delete' and choice!= 'view' and choice!= 'quit':

            raise

    except:

        print('That is an invalid input please try again \n')

    else:

        return choice

    
    
def add_choice(tasks):
    """"this function adds tasks the the my_tasks list, it uses a while loop so the user can add multiple tasks without going back to the main menu"""
    
    ans='yes'

    while ans=='yes':

        task=input('What task would you like to add? \n')

        task=task.strip()

        tasks.append(task)

        #more validations to prevent errors
        
        try:

            ans=input('Would you like to add another task, yes or no? \n')

            ans=ans.lower()

            ans=ans.strip()

            if ans!='yes' and ans!='no':

                raise

        except:

            while ans!='yes' and ans!='no':

                ans=input('Invalid responce, please type yes or no \n')
            

        

    return tasks

def remove_choice(tasks):

    """this function removes tasks from the my_tasks list, using a while loop for removing multiple tasks without going to the main menu"""

    ans='yes'

    while ans=='yes':

        try:

            task=input('What task would you like to delete? \n')

            task=task.strip()

            if task not in tasks:

                raise

        except:

            #this loop makes sure the task they want to remove is on thier list of tasks 

            while task not in tasks:

                task=input('this task is not on your list, please try again \n')

                task=task.strip()

        tasks.remove(task)

    #more validations to prevent errors

        try:

            ans=input('Would you like to delete another task, yes or no? \n')

            ans=ans.lower()

            ans=ans.strip()

            if ans!='yes' and ans!='no':

                raise

        except:

            while ans!='yes' and ans!='no':

                ans=input('Invalid responce, please type yes or no \n')

    return tasks


def view_choice(tasks):

    """this function shows the user the full list of tasks currently on thier list"""

    #just in case thier list of tasks is empty this will print

    if not tasks:

        print('you have no tasks to do! \n')

    #this for loop is to show the list of tasks without brackets

    else:
        print('These are all your tasks! \n')

        for task in tasks:

            print(f'\t{task}\n')





#empty list of tasks ready to be used for the program

my_tasks=[]

#this loop is so the user can constantly add, remove, and view their tasks until they decide to quit

flag=True

while flag:

    choice=display()

    if choice=='add':

        add_choice(my_tasks)

    elif choice=='delete':

        my_tasks=remove_choice(my_tasks)

    elif choice=='view':

        view_choice(my_tasks)

    elif choice=='quit':

        break

print('Thanks for using My To Do List!')

