def remove_dollar_sign(s):
    s = input('enter the string: ')
    remove = s.replace('$','')
    return remove
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

