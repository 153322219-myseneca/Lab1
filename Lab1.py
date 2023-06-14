def calculate_age():
    current_year = 2023  # set the current year
    
    try:
        birth_year = int(input("Enter your birth year: "))  # ask the user for their birth year and convert it to an integer
        age = current_year - birth_year  # calculate the age
        print("Your age is", age)  # print the age
        
    except ValueError:
        print("Please enter an integer for the birth year.")

calculate_age()  # call the function


def helloWorld():
	print('Hello World')


helloWorld()


