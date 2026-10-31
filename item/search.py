from hanshu import*
from task import*
load_tasks()
while True:
    print("\n1查看 2添加 3完成 4删除 5退出")
    sum=int(input("请输入功能"))
    if sum==1:
      show_tasks()
      
    if sum==2:
      add_tasks()
      save_tasks()
    if sum==3:
      compelte_tasks()
      save_tasks()
    if sum==4:
      delete_tasks()     
      save_tasks() 
    if sum==5:
      break