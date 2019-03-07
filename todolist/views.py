from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import TodoList, Category

# Create your views here.
def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            #return redirect("/") #reloading the page

        elif "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST.getlist("checkedbox") #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo

        elif "taskUpdate" in request.POST:
            updateId = request.POST["taskUpdate"]
            todo = TodoList.objects.get(id=int(updateId))
            return render(request, "todolist/update.html", {"todo" : todo,"todos": todos, "categories":categories})

        elif "taskUpdated" in request.POST:
            updateId = request.POST["taskUpdated"]
            #todo = TodoList.objects.get(id=int(updateId))
            category = request.POST["category_select"] 
            title = request.POST["description"]
            due_date = str(request.POST["date"])
            content = title + " -- " + due_date + " "
            category=Category.objects.filter(name=category).order_by('id').first()
            Todo = TodoList(id=int(updateId),title=title, content=content, due_date=due_date, category=category) 
            Todo.save()


    return render(request, "todolist/index.html", {"todos": todos, "categories":categories})