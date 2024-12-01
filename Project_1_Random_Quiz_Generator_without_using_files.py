import random

registration_email = []
registration_password = []

def Registration():
    while(True):
        email = input("Please enter your email:\n").casefold().strip()
        if email.endswith("gmail.com") and ("@" in email):
            if (" " or '\t' ) not in email:
                pass
            else:
                print("Please enter the email which should not contain white space between character")
                continue
        else:
            print("Please enter the email which should contain ('@') and should ends with ('gmail.com')")
            continue

        temp = 0
        if email in registration_email:
            print("Please enter valid email. This email has already registered")
            while(True):
                num = input("Enter '1' for try again and '2' for Home Page: \n")
                if num.isalpha():
                    print("Please enter a valid input")
                    continue
                elif num == '1':
                    break
                elif num == '2':
                    temp = int(num)
                    break
                else:
                    print("Please enter a valid input")
                    continue
            if temp == 2:
                break

            continue

        else:
            password = input("Please enter password:\n")
            while(True):
                password_len = len(password)
                if password_len < 6:
                    print("Please enter a strong password,length of your password should be greater than or equal to 6")
                    password = input()
                    continue
                else:
                    break

            registration_email.append(email)
            registration_password.append(password)
            print("You have registered successfully.")
            break




def Login(email):
    while(True):
        password = input("Please enter password for the registered email\n")
        i = registration_email.index(email)
        if registration_password[i] != password:
            print("Wrong Password")
            continue
        else:
            break




def Generate_Question():
    questions = {"What is the maximum possible length of an identifier?":[16,32,'none of these'],
                 "What is a correct syntax to output 'Hello World' in Python?":["echo('Hello World');",'print("Hello World")','p("Hello World")'],
                 "Which of the following is the correct extension of the Python file?":[".py",".python",".p"],
                 "What will be the value of the following Python expression? 4+3%5 ":[7,2,1],
                 "Which keyword is used for function in Python language?":["Function","def","define"],
                 "Which of the following character is used to give single-line comments in Python?":["#","//","!"],
                 "What will be the output of the following Python code? print(True) if 0.1 + 0.2 == 0.3 else print(False)":["True","False","None"],
                 "Which of the following is used to define a block of code in Python language?":["indentation","key","brackets"],
                 "What will be the output of the following Python code snippet if x=1?  x<<2 ":[4,2,1],
                 "What will be the output of the following Python function? min(max(False,-3,-4), 2,7)":[-4,2,"False"],
                 "Which of the following is not a core data type in Python programming?":["Tuples","Lists","Class"],
                 "What will be the output of the following Python function? len(['hello',2, 4, 6]) ":[4,3,6],
                 "Which one of the following is not a keyword in Python language?":["pass","assert","eval"],
                 "Who developed Python Programming Language?":["Rasmus Lerdorf","Wick van Rossum","Guido van Rossum"],
                 "Which type of Programming does Python support?":["object-oriented programming","structured programming","both"],
                 "Which of the following is the use of id() function in python?":["Id returns the identity of the object","Every object doesn’t have a unique id","Both"],
                 "Which of the following is a Python tuple?":["{1, 2, 3}","[1, 2, 3]","(1, 2, 3)"],
                 "Which of the following is used to represent list in python":["[]","{}","()"],
                 "Which of the following is the correct syntax for type casting ":["datatype(variable)","(datatype)variable","both"]
                 }


    answers = {"What is the maximum possible length of an identifier?":'none of these',
               "What is a correct syntax to output 'Hello World' in Python?":'print("Hello World")',
               "Which of the following is the correct extension of the Python file?":".py",
               "What will be the value of the following Python expression? 4+3%5 ":7,
               "Which keyword is used for function in Python language?":"def",
               "Which of the following character is used to give single-line comments in Python?":"#",
               "What will be the output of the following Python code? print(True) if 0.1 + 0.2 == 0.3 else print(False)":"False",
               "Which of the following is used to define a block of code in Python language?":"indentation",
               "What will be the output of the following Python code snippet if x=1?  x<<2 ":4,
               "What will be the output of the following Python function? min(max(False,-3,-4), 2,7)":"False",
               "Which of the following is not a core data type in Python programming?":"Class",
               "What will be the output of the following Python function? len(['hello',2, 4, 6]) ":4,
               "Which one of the following is not a keyword in Python language?":"eval",
               "Who developed Python Programming Language?":"Guido van Rossum",
               "Which type of Programming does Python support?":"both",
               "Which of the following is the use of id() function in python?":"Id returns the identity of the object",
               "Which of the following is a Python tuple?":"(1, 2, 3)",
               "Which of the following is used to represent list in python":"[]",
               "Which of the following is the correct syntax for type casting ":"datatype(variable)"
               }

    quiz = sorted(questions)
    quiz1 = random.sample(quiz,5)
    for i,item in enumerate(quiz1):
        i += 1
        print(f"Question {i}: {item} ")
        values = questions[item]
        for j,value in enumerate(values):
            j += 1
            print(f"\t {j}: {value}")
        print("\n")


    given_answer = []
    right_answer_given = 0
    for k in range(len(quiz1)):
        k += 1
        while(True):
            answ = input(f"Select the option for Answer {k}:\t")
            if answ.isalpha() or int(answ) < 0 or int(answ) > 3:
                print("Please select the option no as [1,2 or 3].")
                continue
            else:
                answ = int(answ)
                given_answer.append(answ)
                break
    print("\n")
    for l,answ in enumerate(quiz1):
        q = quiz1[l]
        a = questions[q]
        if answers[q] == a[given_answer[l]-1]:
            right_answer_given += 1
        else:
            print(f"The right Answer for Question {l+1} is : {answers[q]} ")

    print(f"\nYou have given {right_answer_given} right answer out of 5")
    given_answer.clear()
    right_answer_given = 0



if __name__ == "__main__" :
    while(True):
        print("Enter '1 for registration' , '2 for login' , '3 to know who has already registered'")
        num = input()
        if num.isalpha():
            print("Please enter the valid input")
            continue

        elif num.isdigit() and num == '1':
            Registration()
            continue

        elif  num.isdigit() and num == '2':
            while (True):
                email = input("Please enter your registered email:\n").casefold()
                if email in registration_email:
                    Login(email)
                    break
                else:
                    print("Account not found")
                    while(True):
                        num2 = input("Press '2' for try again to login and Press '1' for registration:\n")
                        if num2.isalpha():
                            print("Please enter a valid input")
                            continue
                        elif num2 == '1':
                            Registration()
                            break

                        elif num2 == '2':
                            break

                        else:
                            continue

                    continue
            print("\n")
            Generate_Question()
            while(True):
                gen = input("Do you want to generate 5 question again . Press 'y' for Yes and 'n' for No exit: \n").lower()
                while(True):
                    if gen.isnumeric() or gen.isdigit():
                        print("Please enter a valid input:")
                        gen = input()
                        continue
                    elif gen == 'y':
                        Generate_Question()
                        break
                    elif gen == 'n':
                        exit_code = input("Press '1 for Home Page' , 'e for exit':\n")
                        while(True):
                            if exit_code.isalpha() and exit_code != 'e':
                                print("Please enter the valid input:")
                                exit_code = input()
                                continue
                            elif exit_code == 'e':
                                exit()
                            elif exit_code == '1':
                                break
                            else:
                                print("Please enter the valid input:")
                                exit_code = input()
                                continue

                        break
                    else:
                        print("Please enter a valid input:")
                        gen = input()
                        continue
                if gen == 'n':
                    break
                continue
            continue

        elif num.isdigit and num == '3':
            print(f"These are the registered emails: {registration_email}")
            continue
        else:
            print("Please enter a valid input")
            continue

