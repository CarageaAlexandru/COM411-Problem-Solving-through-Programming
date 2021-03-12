def escape_by(plan):
    if plan == "jumping over":
        return print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        return print("We cannot escape that way! The boulder is too fast!")
    elif plan == "going deeper":
        return print("That might just work! Let's go deeper!")
    else: 
        return print("We cannot escape that way! The boulder is in the way")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
