#lecture 2
'''
#example
x = int(input("請輸入成績(0~100) : "))
if x > 100 or x < 0:
    print('不要騙喔! OAO')
elif x >= 90:
    print('Nice!!')
elif x >= 60:
    print('Pass')
else:
    print('好課值得一修再修3修重修畢業後繼續修')
'''
#sample code 1b - revised
count = 0
while count < 3:
    x = input("Is the TA handsome? (y/n)")
    if x == 'y' or count == 2:
        break
    print("Are you sure? Give you another chance. ")
    count += 1
if x != 'y':
    print("Am I this ugly? QQ")
else:
    print("Thank you! ")

#sample code 2 - revised
print("prime numbers in the range of 1~20: ")
