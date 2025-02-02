'                                         🐍 Students Marks List Project Using Nested If and Iterative Statements 🐍                                                                    ' 

print()#to give a line break
while True:
    # asking the user for input to access their marks
    name = input("Enter your Name: ")
    rgno = int(input("Enter your Rg.No.: "))
    # user's marks
    marks=450

    # if the Name is correct
    while name == "gireesh":
        # if the Name is correct
        if name == "gireesh":
            # if the Rg.No. is correct
            if rgno == 1:
                print()
                print("Welcome to manabadi.com Mr. ", name)
                print()
                print("Your total marks out of 500: ", marks)
                print()
                print("\U0001F31F\U0001F31F Congratulations... You have passed out... \U0001F31F\U0001F31F")
                print()
                break
            # if the Rg.No. is incorrect
            if rgno != 1:
                # asking the user to enter the Rg.No. again
                while rgno != 1:
                    print()
                    print("Please enter a valid Rg.No. ...")
                    rgno = int(input("Enter your Rg.No.: "))
                    # if the user enters correct Rg.No.
                    if rgno == 1:
                        break
                    # if the user enters wrong Rg.No. again
                    if rgno != 1:
                        # asking the user whether he wants to try again or exit
                        if rgno != 1:
                            ropt = input("""
                            you have entered wrong again...
                               
                            1. if you want to try again press 1
                            2. if you want to exit press 2
                               
                            Enter your Option here: """)
                        # if the user wants to exit
                        if ropt != "1":
                            break
            # if the user does not provide correct Rg.No. and wants to exit
            elif rgno != 1:
                break

    # if the Name is incorrect 
    while name != "gireesh":
        # asking the user to enter the Name again
        if name != "gireesh":
            print()
            print("please enter a valid Name..")
            print()
            name=input("Enter your Name: ")
            print()
            # if the user to enter the Name wrong again
            if name != "gireesh":
                # asking the user whether he wants to try again or exit
                nopt=input("""
                           you have entered wrong again...

                           1. if you want to try again press 1
                           2. if you want to exit press 2

                           Enter your Option here: """)
                # if the user wants to exit
                if nopt != "1":
                    break
        # if the user enters correct Name
        while name == "gireesh":
            if name == "gireesh":
                # if the Rg.No. is correct display the marks
                if rgno == 1:
                    print()
                    print("Welcome to manabadi.com Mr. ", name)
                    print()
                    print("your total marks out of 500: ", marks)
                    print()
                    print("\U0001F31F\U0001F31F Congratulations... You have passed out... \U0001F31F\U0001F31F")
                    print()
                    break
            # asking the user again, if the Rg.No. is not correct
            while rgno != 1:
                print()
                print("please enter a valid Rg.No. ...")
                rgno = int(input("Enter your Rg.No.: "))
                # if the user enters the wrong Rg.No. again
                if rgno != 1:
                    # asking the user whether he wants to try again or exit
                    ropt = input("""
                            you have entered wrong again...
                               
                            1. if you want to try again press 1
                            2. if you want to exit press 2
                               
                            Enter your Option here: """)
                    # if the user wants to exit
                    if ropt != "1":
                        break
                # if the user provides correct Rg.No.
                elif rgno == 1:
                    break
    
    # if the user enters wrong name and he wants to exit
    if name != "gireesh":
        print()
        print("Thank you for visiting our site... always keep smiling..."+chr(128522),chr(128522),chr(128522))
        print()
        break
    # if the user enters wrong Rg.No. and he wants to exit
    if rgno != 1:
        print()
        print("Thank you for visiting our site... always keep smiling..."+chr(128522),chr(128522),chr(128522))
        print()
        break
    # if the user enters correct Name and Rg.No. and gets the desired output
    if name == "gireesh" and rgno == 1:
        print()
        print("Thank you for visiting our site... always keep smiling..."+chr(128522),chr(128522),chr(128522))
        print()
        break
    # if above all conditions fail,try this condition and exit
    else:
        print()
        print("Thank you for visiting our site... always keep smiling..."+chr(128522),chr(128522),chr(128522))
        print()
        break
print()
