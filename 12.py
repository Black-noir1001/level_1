def isVoild(passw):
        if   passw.isdigit() and len(passw) == 4:
            return (True)
        else :
            return (False)
        
print(isVoild("3868")) # true
