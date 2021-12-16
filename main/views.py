from django.shortcuts import render,redirect
from .models import TodoList,Item
# Create your views here.
from .forms import CreateListForm, CreateItemForm


def home(request):
    lists = TodoList.objects.all()
    context = {"lists":lists}
    return render(request, "main/home.html",context)


def about(request):
    return render(request, "main/about.html")


def todo(request, pk):
    todolist = TodoList.objects.get(id=pk)
    items = Item.objects.filter(todoList__name=todolist)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get('save'):
            for item in todolist.item_set.all():
                if request.POST.get("c"+str(item.id)) == "clicked":
                    print("happen")
                    item.complete = True
                else:
                    print("no happen")
                    item.complete = False
                print("item save")
                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("newItem")
            if len(txt)>2:
                todolist.item_set.create(text=txt,complete=False)

    context = {"todolist": todolist,"items":items}
    return render(request, "main/todo.html", context)


def create(request):
    form = CreateListForm()
    if request.method == "POST":
            form = CreateListForm(request.POST)
            if form.is_valid():
                n=form.cleaned_data["name"]
                print(n)
                request.user.todolist_set.create(name=n)
                return redirect('main-home')
    context = {"form":form}
    return render(request, "main/create.html",context)


def view(request):
    lists = request.user.todolist_set.all()
    context = {"lists":lists}
    return render(request, "main/view.html", context)