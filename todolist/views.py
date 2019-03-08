from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import TodoList, Category
from apscheduler.schedulers.background import BackgroundScheduler

import datetime,smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def index(request):

    todos = TodoList.objects.all()
    categories = Category.objects.all()

    def startSchedule(date,email,title,content):
        scheduler = BackgroundScheduler()
        scheduler.add_job(send, trigger='date', next_run_time=str(date), args=[email,title,content])
        scheduler.start()

    def send(email,title,content):
        
        gmail_user = 'todoappasif@gmail.com'  
        gmail_password = '12345678todo'
        sent_from = 'todoappasif@gmail.com'

        message = MIMEMultipart("alternative")
        message["Subject"] = title
        message["From"] = gmail_user
        message["To"] = email
        text = content
        part = MIMEText(text, "plain")
        message.attach(part)


        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(gmail_user, gmail_password)
                server.sendmail(
                    gmail_user, email, message.as_string()
                )
        except:  
            print('Something went wrong...')

            

        return render(request, "todolist/index.html", {"todos": todos, "categories":categories})

    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            email = request.POST["email"]
            category=Category.objects.filter(name=category).order_by('id').first()
            date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
            AsDate = date_time_obj.date()
            AsTime = date_time_obj.time()
            Todo = TodoList(title=title, content=content, due_date=AsDate, due_time=AsTime, email=email, category=category)
            startSchedule(date_time_obj,email,title,content)
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
            email = request.POST["email"]
            category=Category.objects.filter(name=category).order_by('id').first()
            date_time_obj = datetime.datetime.strptime(due_date, '%Y-%m-%dT%H:%M')
            AsDate = date_time_obj.date()
            AsTime = date_time_obj.time()
            startSchedule(date_time_obj,email,title)
            Todo = TodoList(id=int(updateId),title=title, content=content, due_date=AsDate, due_time=AsTime, email=email, category=category) 
            Todo.save()


    return render(request, "todolist/index.html", {"todos": todos, "categories":categories})