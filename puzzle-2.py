#PART 1

file = open('input2.txt')

count = 0

for line in file:
    a = line.split(' ')
    #Output a = ['4-8', 'n:', 'dnjjrtclnzdnghnbnn\n']

    b = a[0].split('-')
    #Output b = ['4', '8']
    
    #Stores the min/max values
    mini = int(b[0])
    maxi = int(b[1])

    #Stores the letter the password must contain
    letter = a[1].strip(':')

    #Stores the password
    password = a[2].strip('\n')
       
    
    letter_count = 0

    for char in password:
    #Determines whether the letter is in the password
        if char == letter:
            letter_count = letter_count + 1
        
    if letter_count >= mini and letter_count <= maxi:
        count = count + 1
                    

print(f"Number of valid passwords: {count}")

#PART 2

file = open('input2.txt')

count = 0

for line in file:
    a = line.split(' ')
    #Output a = ['4-8', 'n:', 'dnjjrtclnzdnghnbnn\n']

    b = a[0].split('-')
    #Output b = ['4', '8']
    
    #Stores the min/max values
    mini = int(b[0])
    maxi = int(b[1])

    #Stores the letter the password must contain
    letter = a[1].strip(':')

    #Stores the password
    password = a[2].strip('\n')

    password_arr = []
    for char in password:
        password_arr.append(char)

    #Determines whether the letter is in only one of the specified positions
    if len(password) >= maxi-1:
        if password_arr[mini-1] == letter or password_arr[maxi-1] == letter:
            if password_arr[mini-1] == letter and password_arr[maxi-1] == letter:
                count = count
            else:
                count = count + 1
                    
print(f"New number of valid passwords: {count}")


     
