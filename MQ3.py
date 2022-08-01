# Then check whether the user's password is strict or not.
#  A strong password should follow all these rules:

# At least its length should be 6
# Maximum length should not exceed 16
# Must be at least a dollar sign ($)
# At least password must be 2 or 8
# Password must be capital or capital Z
# If the password follows these rules,
#     print"strong password", otherwise type "week password"

from builtins import input, int, len, print


# print("create strong passwoed")
a=(input("enter strong password"))
b=len(a)
if b>6 and b<16:
    if "$" in a:
        if "2" in a or "8" in a:
            if "A" in a or "z" in a:
                print("strong password")
            else:
                print("week password")
        else:
            print("week password")
    else:
        print("week password")
else:
    print("week password")