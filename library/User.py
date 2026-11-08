from Book import book,books,cunchu
import json
class user:
    def borrow(self,id):
            for b in books:
                if b.id==id:                  
                    if b.borrowed==False:
                       b.borrowed=True
                       cunchu()
                       print("借书成功")
                    else:
                        print("这本书已经被借走了")
                count=+1
    def return_book(self,id):
        for bin in books:
            if bin.id==id:
                if bin.borrowed==True:
                    bin.borrowed=False
                    print("还书成功")
                    cunchu()
                else:
                    print("这本书没有被借走")