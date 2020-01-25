import re
def comp(s):
        if re.match("[\w\d]+@[\w\d]+.[es|com|net|nz]",s):
                print("Es un Email Correcto")
        else:
                print("Usted su loquera usted tiene su pampara apaga")
