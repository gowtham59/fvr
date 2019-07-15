x1=int(input())
string=input()
s2="aeiou"
final_string=""
for i in string:
    if(i not in s2):
        final_string+=i
print("".join(reversed(final_string)))
