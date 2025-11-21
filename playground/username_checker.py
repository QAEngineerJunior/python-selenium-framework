def check_username(username):
    print("Testing username:", username)

    if len(username) >= 5:
        print(" Regel 1: lengte ok")
    else:
        print("Regel 1: Te kort")

    if any(c.isalpha() for c in username):
        print("Regel 2 : bevat een letter")
    else:
        print("Regel 2 : geen letter aanwezig")

    if " " not in username:
        print("Regel 3: Geen spaties")
    else:
        print("Regel 3: Spaties niet toegelaten")


    if username[-1].isalnum():
        print(" Regel 4: Correct einde")
    else:
        print ("Regel 4: Mag niet eindigen op symbool")

# testcases

check_username("Miguel")
check_username("Mi uel")
check_username("12345!")
