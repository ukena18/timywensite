from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name


class Item(models.Model):
    todoList = models.ForeignKey(TodoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.text


#
# >>> from main.models import Item,TodoList
# >>> t = TodoList(name="me mama")
# >>> t.save()
# >>> Todo.objects.all()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'Todo' is not defined
# >>> TodoList.objects.all()
# <QuerySet [<TodoList: me mama>]>
# >>> t.item_set.all()
# <QuerySet []>
# >>> t.item_set.create(text = "goto mall",complete=True)
# <Item: goto mall>
# >>> t.item_set.all()
# <QuerySet [<Item: goto mall>]>
# >>>
