from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q


def home(request):
    student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=77)

    # student_data = Student.objects.exclude(marks=77)

    #student_data = Student.objects.order_by('city')

    # student_data = Student.objects.order_by('-city')

    # student_data = Student.objects.order_by('?')

    # student_data = Student.objects.order_by('name')
    #student_data = Student.objects.order_by('id').reverse()[5:]
    #student_data = Student.objects.order_by('id').reverse()[:5]

    # student_data = Student.objects.values()

    # student_data = Student.objects.values_list()

    # student_data = Student.objects.values('name','city')

    # student_data = Student.objects.values_list('id','name',named=True)

    # student_data = Student.objects.using('default')

    # student_data = Student.objects.dates('pass_date', 'month')

    ########### second table ###########

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # student_data = qs2.intersection(qs1)

    # qs1 = Student.objects.values_list('id','name', named=True)
    # qs2 = Teacher.objects.values_list('id','name', named=True)
    # student_data = qs1.difference(qs2)

    ##### AND OR operator #####

    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106)

    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=108) | Student.objects.filter(roll=109)

    # student_data = Student.objects.get(pk=9)
    # student_data = Student.objects.create(name='Gaurav',roll=114, city='Rajkot', marks=59, pass_date='2020-4-6' )
    
    #student_data = Student.objects.create(name='Putin', roll=115, city='Porbandar', marks=67, pass_date='2019-6-9')
    
    #student_data = Student.objects.create(
     #   name="Gaurav", roll=111, city="Vijaynagar", marks=54, pass_date="2020-4-9"
    #)

    print("Return:", student_data)
    print()
    return render(request, "home.html", {"students": student_data})
