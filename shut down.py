def shutdown(answer):
    if answer == "Yes":
        print("Shutting down")
    elif answer == "No":
        print("Abort shut down")
    else:
        print("Sorry")


user_input = input("Do you want to shut down? (Yes/No): ")
shutdown(user_input)