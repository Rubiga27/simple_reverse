def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string
string = input("")
reversed_string = reverse_string(string)
print(reversed_string)

"""
Input 1:
A = "scaler"

Input 2:
A = "academy"


Output 1:
"relacs"

Output 2:
"ymedaca"
"""
