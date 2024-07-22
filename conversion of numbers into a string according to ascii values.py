#taking a group of numbers as a string , reversing it and print character as per their ascii values 
string=input()
reverse=string[::-1]
i=0
password=""
while i<len(string):
    if i<len(string):
        two_digit_num=int(reverse[i:i+2])
    else :
        two_digit_num=-1 
    if i<len(string):
        three_digit_num=int(reverse[i:i+3])
    else:
        three_digit_num=-1
    if (65<=two_digit_num<=90)or (97<=two_digit_num<=122) or (two_digit_num==32):
        password+=chr(two_digit_num)
        i+=2
        continue
    if (65<=three_digit_num<=90)or (97<=three_digit_num<=122) or (three_digit_num==32):
        password+=chr(three_digit_num)
        i+=3
        continue
    i+=1
print(password)
