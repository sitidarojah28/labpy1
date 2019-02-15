# labpy1


Program 1 (Program mencari bilangan terbesar)
1).Alur Agoritmanya :

-Mendefinisikan perulangan dengan mengetikkan ;
	def pengulangan():
   
-Memasukkan 3 bilangan  ;
	 print ('Masukkan bilangan :')
    	 a=int(input('masukan bilangan a  : '))
    	 b=int(input('masukan bilangan b   : '))
    	 c=int(input('masukan bilangan c  : '))

-Membandingkan nilai a,b,c dengan rumus if ;
    if a>b:
        if a>c:
            print ('bilangan terbesarnya  :',a)
        else:
            print ('bilangan terbesarnya  :',c)
    else:
        if b>c:
            print ('bilangan terbesarnya : ',b)
        else:
            print ('bilangan terbesarnya  :',c)


	return pengulangan()


2).Berikut kode lengkapnya :


def pengulangan():
    print ('masukkan bilangan :')
    a=int(input('masukan bilangan a  '))
    b=int(input('masukan bilangan b  '))
    c=int(input('masukan bilangan c '))

    if a>b:
        if a>c:
            print ('bilangan terbesarnya  :',a)
        else:
            print ('bilangan terbesarnya  :',c)
    else:
        if b>c:
            print ('bilangan terbesarnya :',b)
        else:
            print ('Bilangan terbesarnya adalah :',c)

pengulangan()

3.Berikut Flowchatnya :

![img](https://github.com/sitidarojah28/labpy1/blob/master/flowlabpy1.png)


4.Berikut screenshotnya :
![img](https://github.com/sitidarojah28/labpy1/blob/master/hasillabpy1.png)