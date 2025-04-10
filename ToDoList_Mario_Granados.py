# Mario Granados
# Todo List Application

# import time for user experience during loading process
import time

# shows the optinos the user can select, returns user option
def option_prompt():
    return input(
        "Enter 1: to add a tast\n Enter 2: display all tasks\n Enter 3: look up a task\n Enter 4: Save and exit\n"
    )

# writes the todo list to a txt file, I had to do this for a personal project and its pretty easy
# I added some time delays, because i've learned user's like loading times.
def write_to_file(file_name, list):
    print("Creating file...")
    time.sleep(1)
    with open(file_name, "w") as file:
        for key, value in list.items():
            file.write(f"Task: {key}, Description: {value}\n")
    print("Writting to file...")
    time.sleep(2)

    print("File created successfully!")


# main function, this is where the program starts and ends
def main():
    # user tells us what we will name the file
    file_name = input("Enter the name of the file to save your todo list: ")
    # the todo list, I should of probaly named this to_do_list but I realized that at the end.
    list = {}
    # if user does not type the .txt extension, we do it for them, of if they don't enter then we default
    if ".txt" not in file_name:
        file_name += ".txt"
    elif file_name == "":
        file_name = "todo_list.txt"
    
    # call to the main propmt, we will do this through out the loop
    option = option_prompt()
    # loop and check for user option, then we do what is respectfully asked, saving value key pairs
    while True:
        if option == "1":
            list[input("Enter the name of the task: ")] = input(
                "Enter the description of the task: \n"
            )
            option = option_prompt()
        elif option == "2":
            for key, value in list.items():
                print(f"Task: {key}, Description: {value}\n")
            option = option_prompt()
        elif option == "3":
            search_query = input("Enter the name of the task to look up: ")
            if search_query in list:
                print(f"Task: {search_query}, Description: {list[search_query]}\n")
            option = option_prompt()

        elif option == "4":
            # save the file upon exit
            write_to_file(file_name, list)
            break
        else:
            # in case user enters something else
            print("Invalid option")
            option = option_prompt()
    return
# end
main()

# i could of done a read function, not difficult but I have another project to finish. 
