# Lists and Strings

# Strings and slices
user_name = "Mr. Ubial"

# Slice user_name -> "Mr."
# "Mr. Ubial"
#  0123456789
user_name[0]            # "M"
print(user_name[0:3])   # "Mr."
print(user_name[:3])    # "Mr."
print(user_name[4:])    # "Ubial"

print(f"{user_name}'s last name is {user_name[4:]}!")


# Lists and stepping