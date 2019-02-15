def pengulangan ():
    print ('masukan bilangan :')
    a=int(input('masukan bilangan a '))
    b=int(input('masukan bilangan b '))
    c=int(input('masukan bilangan c '))

    if a>b:
        if a>c:
            print ('bilangan terbesarnya :',a)
        else:
            print ('bilangan terbesarnya :',b)
    else:
        if b>c:
            print ('bilangan terbesarnya :',b)
        else:
            print ('bilangan terbesarnya :',c)



pengulangan ()
