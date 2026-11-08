from Book import book,books,cunchu
from User import user
import json
class admin(user):
    def add_book(self,name,author,id):
       b=book(name,author,id)
       books.append(b)
       print("添加成功")
       cunchu()
    def delete_book(self,id): 
        count=0
        for bin in books:
            if bin.id==id:
                books.remove(bin)
                print("删除成功")
                cunchu()
                count=1
                break
        if count==0:
            print("没有这本书")
    def show_book(self):
        with open("D:/test.txt","r",encoding="UTF-8") as f:
            bin=json.load(f)
        for b in bin:
           print(b)

    def serch_book(self):
       s=int(input("请输入id:"))
       count=0
       for b in books:
                   if b.id==s:
                       print("书名:",b.name,"作者:",b.author,"编号:",b.id,b.borrowed)
                       count=1
       if count==0:
            print("没有这本书")
        

