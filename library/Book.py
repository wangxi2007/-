import json
import os
def cunchu():
    with open("D:/test.txt","w",encoding="UTF-8") as f:
            f.write(json.dumps(books,ensure_ascii=False,default=lambda obj:obj.to_dict(),indent=4))
            f.flush()
class book:
    def __init__(self,name,author,id):
        self.name=name
        self.author=author
        self.id=id
        self.borrowed=False
    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "id": self.id,
            "borrowed": self.borrowed
        }
if not os.path.exists("D:/test.txt"):
 books=[book("西游记","吴承恩",1),
            book("红楼梦","曹雪芹",2),
            book("三国演义","罗贯中",3),
            book("水浒传","施耐庵",4)]
 cunchu()
books=[]
with open("D:/test.txt","r",encoding="UTF-8") as f:
    data=json.load(f)
    for b in data:
        my_b=book(b["name"],b["author"],b["id"])
        my_b.borrowed=b["borrowed"]
        books.append(my_b)
