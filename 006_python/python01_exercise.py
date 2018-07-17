# Problem - 1
list = [1,3,4,5,6]
def is_pat_present(list):
    n = len(list)
    n = n-1
    n = n-2
    i = 0
    while(i<n):
        if(list[i]==1 and list[i+1]==2 and list[i+2]==3):
            return True
        i = i+1
    return False
print("List is: ",list)
print("Pattern present in the list? ",is_pat_present(list))

# Problem - 2
def string_bits(str):
    out = ""
    i = 0
    n = len(str)-1
    while(i<=n):
        if(i%2 == 0):
            out = out + str[i]
        i=i+1
    return out

def string_bit(str):
    out = str[::2]
    return out

print(string_bit("anshuman"))

# Problem - 3
def same_end(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    m = len(str1)-1
    n = len(str2)-1
    i = min(m,n)
    while(i>0):
        i = i - 1
        if(str1[m]!=str2[n]):
            return False
        m = m - 1
        n = n - 1
    return True

print(same_end("AnShUmAN","man"))


# Problem - 4
def doublecondachar(str):
    strret = ""
    n = len(str)-1
    i = 0
    while(i<=n):
        strret = strret + str[i] + str[i]
        i = i + 1
    return strret

print(doublechar("Anshuman"))


# Problem - 5
def teen_sum(a,b,c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    d = a+b+c
    return d

def fix_teen(n):
    if(n==13 or n==14 or n==17 or n==18 or n==19):
        return 0
    else:
        return n

print(teen_sum(1,2,3))
print(teen_sum(1,13,1))
print(teen_sum(1,2,15))

# Problem - 6
def even_count(list):
    i = 0
    count = 0
    n = len(list)
    while(i<n):
        if(list[i] % 2 == 0):
            count = count + 1
        i = i + 1
    return count

print(even_count([1,2,3,54,6,5345,36,456,456,436,45,457,45,63,3]))
