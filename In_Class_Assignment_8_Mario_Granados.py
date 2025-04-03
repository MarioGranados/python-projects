# Mario Granados
# In-Class Assignment 8
# key value pairs



def main():
    # create a key value pari dictionary
    # this will get sorted by the year
    tasks =  {
        'curriculum[2026]': 'software engineering',
        'curriculum[2024]': 'programing funadamentals', 
        'curriculum[2025]': 'Data Structures',
        'curriculum[2023]': 'Data Analysis',
        'curriculum[2022]': 'Computer architecture',
    }       
    # sort the dictionary by the key, or left side of value pair
    sorted(tasks.items())

    print(sorted(tasks.items()))
    print('\n')

    # tasks is still unsorted so we need to re assign its value to the sorted version
    print(tasks)

    # assign sorted value to tasks
    tasks = sorted(tasks.items())
    print('\n')

    # tasks is now sorted by the year
    print(tasks)
    print('\n')
    return

main()