class TodoList:
  x=[1,4,3,5,765,345,3,3,5,22,5]

  def add_items(self,a):
    x = self.x.append(a)
    print('to-do added')

  def view_items(self):
    print(self.x)

  def remove_item(self,index = None):
      if index == None:
        print('enter a valid index')
      else:
        try:
          x = self.x.pop(index)
        except:
          print('enter a valid index')

y=TodoList()
y.view_items()

y.remove_item()