def check_pass(passwaord):
    if len(passwaord) == 4   :
        return passwaord.isdigit()
    else :
        return False

print(check_pass("4&0!"))