password = "Olga2009"
if len(password) <8:
    print("Te kort")
else:
    print("lengte ok")


if any(c.isupper() for c in password):
    print("hoofdletter aanwezig")
else:
    print("geen hoofdletter")


if any(c.isdigit() for c in password):
    print("cijfer aanwezig")
else:
    print("geen cijfer aanwezig")


specials = "!@#$%^&*()[]{}"
if any(c in specials for c in password):
    print("special teken aanwezig")
else:
    print("geen speciaal teken aanwezig")


