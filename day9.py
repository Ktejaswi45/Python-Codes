s=input()
vowels='aeiou'
a=s[0:4]
for i in s[:5]:
    if i in vowels:
        print("yes")
    else:
        print("no")
        