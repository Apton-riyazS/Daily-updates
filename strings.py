print("string operations")
#variable creation
s= ('hi world'' today')
#basic string operations
print (s[0])
print (s[4])
print (s+' how are you')
#strip() remove last and first white space
print(s.lower(),s.upper(),s.strip(),s.startswith('hi'),s.endswith('riyaz'))
print (s.replace('hi world','hello world'))
#returns a list of substrings separated by the given delimiter
print(s.split('delim'))
#opsite of split(), joins the elements in the given list together 
# using the string as the delimiter
print(s.join(['hi','today']))
#string slice 
s=('hello')
print(s[1:4])  #print 'ell'
print(s[:])  #print  'Hello' .
print(s[1:]) #print  ''ello' '.
print(s[-1] ) #print 'o' -- last char (1st from the end).
print(s[-4])  #print 'e' -- 4th from the end.
# %string %d -int %s-string, %f-float
 #if statement
speed =int(input("\n Enter your value: "))
print('speed: %d' %speed)
if speed >= 80:
    if speed >= 100:
        print ('danger plz stop')
    else:
        print('slow down')
else:
    print('you can go')
#while loop
a = int(input('enter a number below 50:')) 
# Condition of the while loop
while a < 50 :  
    # Find the mod of 2
    if a%2 == 0:  
        print("The number "+str(a)+" is even")
    else:
        print("The number "+str(a)+" is odd")

    # Increment `number` by 1
    a = a+1
print('***********')
