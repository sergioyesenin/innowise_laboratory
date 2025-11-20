from datetime import date

def Generate_profile (age):
    
    # Logic of 'life stage'

    life_stage = ""
    if age <=12:
        life_stage = "Child"
    elif age >= 13 and age<=20:
        life_stage = "Teenager"
    else:
        life_stage = "Adult"
    return life_stage

def main():
   
    # Greeting
    print("Hello!\n")

    # Input full name
    user_name = input("Please, enter your full name ")


    # Use loop to give a chance if input was incorrect
    while True:
        # Input birth age
        birth_age_str = input("Enter your birth age ")
        # Get current year
        current_year = date.today().year
         
        # Use try-except to avoid ValueError
        try: 
            # Convert str to int
            birth_age = int(birth_age_str)
            # Logic to avoid unrealistic age of user
            if birth_age <= 1900:
                print("The year must be in the range 1900–{current_year}. Please try again.\n")
            else: break

        except ValueError:
            print("Error: you must enter a number.\n")


    # Count age
   
    current_age = current_year - birth_age
    
    # Create an empty list and str
    hobbies = []
    hobby = ""

    # Loop for input hobbies
    while hobby.lower() != "stop":
        hobby = input("Enter your hobby or type 'stop' to finish ")
        if hobby.lower() != "stop":
            hobbies.append(hobby)
    
    # Create a string with "life stage"
    life_stage = Generate_profile(current_age)

    # Create a dict with user info
    user_profile = {"Name": user_name, "Age": current_age, "Life stage": Generate_profile(current_age), "Hobbies": hobbies}


    # Output of user info
    print("---")
    print("Profile summary:")
    for key, value in user_profile.items():
        if key == "Hobbies":
            # Logic of output hobbies
            if len(hobbies) == 0:
                print("You didn't mention any hobbies")
            else:
                print("Favorite hobbies (", len(hobbies), ")")
                for hobby in user_profile["Hobbies"]:
                    print("- " + hobby)
        else:
             print(key, ":", value)
    print("---")

# Start program from "main" function
if __name__ == "__main__":
    main()