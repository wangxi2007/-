from Admin import admin
from User import user
import sys
my_admin=admin()
my_user=user()
s=int(input("请输入你的身份(管理员/用户),管理员请输入1,用户请输入2:" ))
if s==1:
 o=int(input("请输入密码"))
 if o==200721:
    print("你好管理员\n")
    while True:   
        print("你需要做什么:\n添加书籍请输入1\n删除书籍请输入2\n查询书籍请输入3\n展示所有书籍请输入4\n退出请输入5")
        b=int(input())
        if b==1:
            print("请分别输入名字,作者,id")
            a,s,d=input().split()
            d=int(d)
            my_admin.add_book(a,s,d)        
        elif b==2:
              a=int(input("请输入id"))
              my_admin.delete_book(a)
        elif b==3:
             my_admin.serch_book()
        elif b==4:
             my_admin.show_book()
        elif b==5:
             break
 else:
     print("密码错误")
     sys.exit()
else:
     print("你好用户")
     while True:        
          print("你需要做什么\n借书请输入1\n还书请输入2\n退出请输入3")
          b=int(input())
          if b==1:
               s=int(input("请输入借书id"))
               my_user.borrow(s)
          elif b==2:
               s=int(input("请输入还书id"))
               my_user.return_book(s)
          elif b==3:
               break