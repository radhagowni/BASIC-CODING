#first method
string=input()
#taking position where we need to change
position=int(input())
#character to be replaced
character=input()
s=string[:position]+character+string[position+1:]
print(s)
#alternate method
l=list(string)
l[position]=character
st=''.join(l)
print(st)