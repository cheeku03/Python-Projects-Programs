import random
when = ['\nA few years ago', '\nYesterday', '\nLast night', '\nA long time ago','\nOn 20th jan','\nAbout 100 years ago', '\nIn the 20 BC', '\nOnce upon a time']
who = ['a Rabbit', 'an Elephant', 'a Mouse', 'a Turtle','a Cat','there lived a King','there was a Man', 'there lived a Farmer']
name = ['Ali', 'Miriam','Daniel', 'Hoouk', 'Starwalker']
age = [', who seemed to be in late 20s,', ', who seemed very old and feeble,',', who looks like a teenager,',', who looks like in mid 50s,']
residence = ['Barcelona. ','India. ', 'Germany. ', 'Venice. ', 'England. ','Australia. ']
time = ['One Day, ','One full-moon night, ']
went = ['Cinema', 'University','Seminar', 'School', 'Laundry']
happened = ['made a lot of friends.\n','eats a burger.\n', 'found a secret key.\n', 'solved a mystery.\n', 'wrote a book.\n','watch a movie.\n']
while True:
    print("1.Print a Story")
    print("2.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        print(random.choice(when) + ', ' + random.choice(who) +" named " + random.choice(name) + random.choice(age)+  ' lives in '  + random.choice(residence) + random.choice(time) + 'He/She' \
      + ' went to the ' +\
      random.choice(went) + ' and ' + random.choice(happened))
    elif ch==2:
        break
    else:
        print("Invalid Choice")
