from django.shortcuts import get_object_or_404, render, redirect
from .models import StaffModel
from django.db.models import Q
from .forms import StaffModelForm


def add_staff_view(request):
    form = StaffModelForm()
    return render(request, "add_staff.html", context={
        "form": form
    })

def staff_view(request, id):
     try:
        staff_obj = StaffModel.objects.get(id=id)
        return render(request, 'staff.html', context={
          'staff' : staff_obj
        } )
     except StaffModel.DoesNotExist:
          return redirect('home')




def delete_item(request, id):
        try:
           item = StaffModel.objects.get(id=id)
           item.delete()
           return redirect('home')
        except StaffModel.DoesNotExist:
           return redirect('home')

def edit_item(request, id):
     item = get_object_or_404(StaffModel, id=id)
     if request.method == 'POST':
          item.first_name = request.POST.get('first_name')
          item.last_name = request.POST.get('last_name')
          item.phone_number = request.POST.get('phone_number')
          item.birth_day = request.POST.get('birth_day')
          item.photo = request.POST.get('photo')
        
          item.save()
          return redirect('home')
     return render(request, 'edit.html', {'item': item})


def home_view(request):
     
    q = request.GET.get('q')

    staff_Objects = StaffModel.objects.all().order_by("-id")
    if q: 
        if q.isdigit():
            staff_Objects = StaffModel.objects.filter(Q(age=int(q)))
        else:
            staff_Objects = StaffModel.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) )
    else:
        staff_Objects = StaffModel.objects.all()
    staff_Objects = staff_Objects.order_by("-id")

    return render(request, 'home.html', context={
        'staff_objects' : staff_Objects
    })





def index_view(request):
    students = [
        {
            "id": 1,
            "first_name": "Ali",
            "last_name": "Aliyev",
            "age": 22
        },
         {
            "id": 2,
            "first_name": "Alibek",
            "last_name": "Aliyev",
            "age": 27
        },
         {
            "id": 3,
            "first_name": "Kozim",
            "last_name": "Nabiyev",
            "age": 19
        },
         {
            "id": 4,
            "first_name": "Hoshim",
            "last_name": "Zokirov",
            "age": 31
        },
         {
            "id": 5,
            "first_name": "Nodir",
            "last_name": "Murodov",
            "age": 20
        }
    ]
    title_home = "Hello Django"
    return render(request, 'index.html', context={
        "students": students, "text": title_home
    })