from task import*
import json
def save_tasks():
  with open("D:/xiangmu.txt","w",encoding="UTF-8") as f:
    json.dump(tasks,f,ensure_ascii=False)
def load_tasks():
  global tasks
  try:
   with open("D:/xaingmu.txt","r",encoding="UTF-8") as f:
     tasks=json.load(f)
  except:
    
    open("D:/xaingmu.tst","w",encoding="UTF-8")
    pass
  

def show_tasks():
  for t in tasks:
    if t["done"]:
     print("yes")
    else:
     print(t)
def add_tasks():
  a=int(input("请输入代办事项数字"))
  b=input("请输入待办事项")
  tasks.append({"id":a,"thing":b,"done":False})
def  compelte_tasks():
  a=int(input("请输入完成事项"))
  for t in tasks:
    if t["id"]==a:
      t["done"]="True"

def delete_tasks():
  a=int(input("请输入删除事项"))
  for t in tasks:
     if t["id"]==a:
       tasks.remove(t)
 