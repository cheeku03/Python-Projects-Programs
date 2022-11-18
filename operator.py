#reversing a number using operators

#first method
a=1234
st=""
st+=str(a%10) #'4'
a=a//10
st+=str(a%10) # '4'+'3'
a=a//10
st+=str(a%10) # '43'+'2'
a=a//10
st+=str(a%10) # '432' +'1'
print(st)  #'4321'

#second method
a=1234
st=0
st=st*10+a%10    #0+4

a=a//10
st=st*10+a%10    #4*10 + 3

a=a//10
st=st*10+a%10    #43*10 +2

a=a//10
st=st*10+a%10    #432*10 + 1
print(st)
