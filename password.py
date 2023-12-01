import random
def password(n,bg,jg,kg,var,b,w):
    char=''
    y=''
    z=''
    c=''
    
    if n<=12: 
        for i in range(0,bg):
            g = random.choice(var)
            y+=g  
        for i in range(0,jg):
            h = random.choice(b)
            z+=h 
        for i in range(0,kg):
            q = random.choice(w)
            c+=q 
        char += y+z+c
        return (char)

    else:
        return("error")

    
a = input("enter the name of user for the password")


def paint(fx):
    def mfx():
        print("--" * 15)
        fx()
        print("--" * 15)
    return mfx

def extra():
    n = int(input("enter the number of charater you want "))

    @paint
    def hlo():
        
        if n>=12:
            pass
            
        else:
            def hit():
                
                var = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                bg= int(input("enter the number of charater u want"))
                b = '123456789'
                jg= int(input("enter the number of digit u want"))
                w = '!@#$%&*'
                kg= int(input("enter the number of special  u want"))
                if bg+jg+kg == n:
                    
                    t = password(n,bg,jg,kg,var,b,w)
                    print('The generated password is')
                    print(t)
                else:
                    print('''plz choose alphabet digit and special,
                                character wisely''')
                    pass
            hit()

    hlo()



extra()

while True:
    r = input("type 'y' to if u want to get another password , otherwise 'n'")
    if r == 'y':
        extra()
    
    else:
        print("enjoy")
        break
    

