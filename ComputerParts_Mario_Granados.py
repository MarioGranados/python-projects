# Mario Granados  
# Lab Assignment 2  

''' Functions to add, remove, or display the current list start here  

These functions work this way for code readability. '''  

def add_part(parts):
    part_action = input('What part do you want to add: ')
    parts.append(part_action)

def remove_part(parts):
    part_action = input('What part do you want to remove: ')
    # If the user input does not exist, we give a promp
    if part_action in parts:
        parts.remove(part_action)
    else:
        print('Part not found in the list.')

def view_parts(parts):
    print(f'Here are the current parts: {parts}')

''' Functions for logic end here '''  

# 'break' seemed to break the entire app, 'exit()' seems to be the correct equivalent
def exit_program():
    print('Goodbye')
    exit()

# Main program  
def main():
    # Initialize parts  
    parts = []

    ''' Looked up switch-case in Python since a bunch of if-else statements made the code look ugly.  
    This is similar to hashmaps or key pairs.  

    Key: Function '''  
    cases = {
        '1': add_part,
        '2': remove_part,
        '3': view_parts,
        '4': exit_program
    }
    
    print('Welcome to our computer parts store, select an option to continue:\n')

    # Loop program until exit()  
    while True:
        print('1: Add a part')
        print('2: Remove a part')
        print('3: View parts')
        print('4: Exit')

        # User input  
        user_input = input('\nEnter your choice: ')

        # Learned this works in key pairs as well  
        if user_input in cases:
            # If user input is '1', we go to the key '1': value = function named add_part and execute it passing the 'parts' list
            if user_input in {'1', '2', '3'}:
                cases[user_input](parts)
            else:
                # exit_program doestn have params
                cases[user_input]()
        else:
            print('Please select a proper input')

main()