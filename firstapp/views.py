from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import  Member, Book, Users, B_issue,Login_history,issued,rturn
from django.db.models import Q
from datetime import datetime, timedelta
from django.contrib.auth import logout

def sing_up(request): # Sign Up Page Upload
  return render(request,'sing_up.html')

def singup(request):  # Sign Up Entry
    if request.method == 'POST':
        S1 = request.POST.get("username")
        S2 = request.POST.get("email")
        S3 = request.POST.get("password")
        S4 = request.POST.get("cnfm_password")
        S5 = request.POST.get("user_type")
        if S3==S4:
              T1 = Users(username = S1, email_id = S2, pass_word=S3,l_type=S5)
              T1.save()
        else:
            return render(request,'Msg.html')
        return render(request,'login_entry.html')
    return render(request,'sing_up.html')

def user(request): # Sign up user Detail For table 
  mymembers = Users.objects.all().values()
  template = loader.get_template('user.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def u_delete(request, id): # User Delete
  d1 = Users.objects.get(id=id)
  d1.delete()
  return render(request,'home.html')

def u_edit(request, id):  # User Edit Link
  mymember = Users.objects.get(id=id)
  template = loader.get_template('u_edit.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def edituser(request, id): # User Edit Details
  E1 = request.POST.get("username")
  E2 = request.POST.get("email")
  E3 = request.POST.get("password")
  member = Users.objects.get(id=id)
  member.username = E1
  member.email_id = E2
  member.pass_word = E3
  member.save()
  return render(request,'home.html')

def login_entry(request): # Login Page Upload
  return render(request,'login_entry.html')

def login_submit(request): # Login User With Type
  if request.method == "POST":
        T1 = request.POST.get("username")
        T2 = request.POST.get("password")
        T3 = request.POST.get("user_type")
        T4 = datetime.now()
        user = Users.objects.filter(username=T1, pass_word=T2, l_type=T3).first()
        T1 = Login_history(username = T1, user_type = T2, date=T4)
        T1.save()
        if user:
            if user.l_type == 'admin':
                return render(request, 'home.html') 
            else:
                if user.l_type == 'staff':
                    return render(request, 'staff_dashboard.html') 
                else:
                  if user.l_type == 'member':
                    return render(request, 'member_dashboard.html') 
        else:
            return render(request, 'login_fail.html')

def fail(request): # Login Fail Page
  return render(request,'login_fail.html')

def login_history(request):
    login_users = Login_history.objects.all()  # Assuming Login_history is a model in your app
    context = {'login_users': login_users}
    return render(request, 'home.html', context)

def logout_view(request): # Logout Page
    logout(request)
    return render(request,'login_entry.html')

def member_view(request): # Member Page Upload
    return render(request, 'member_view.html')

def home(request): # Home Page Upload
  return render(request,'home.html')

def registration(request): # Libarary Member Data Entry 
  if request.method == 'POST':
        S1 = request.POST.get("f_name")
        S2 = request.POST.get("l_name")
        S3 = request.POST.get("dob")
        S4 = request.POST.get("address")
        S5 = request.POST.get("mobile")
        S6 = request.POST.get("email")
        S7 = request.POST.get("t_o_m")
        T1 = Member(firstname = S1, lastname = S2, d_o_b=S3, address=S4, mobile=S5, email=S6, m_type=S7)
        T1.save()
        return render(request,'home.html')
  return render(request,'registration.html')

def member_entry(request): # Member Detailes On HTML
  members = Member.objects.all().values()
  template = loader.get_template('member_entry.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))

def editmember(request, id): # Member Data Edit
  S1 = request.POST.get("f_name")
  S2 = request.POST.get("l_name")
  S3 = request.POST.get("dob")
  S4 = request.POST.get("address")
  S5 = request.POST.get("mobile")
  S6 = request.POST.get("email")
  S7 = request.POST.get("t_o_m")
  member = Member.objects.get(id=id)
  member.firstname = S1
  member.lastname = S2
  member.d_o_b = S3
  member.address = S4
  member.mobile = S5
  member.email= S6
  member.m_type = S7
  member.save()
  return render(request,'home.html')

def m_delete(request, id): # Member Delete
  d1 = Member.objects.get(id=id)
  d1.delete()
  return redirect(request,'member_entry.html')

def m_update(request, id): # Member Edit
  member = Member.objects.get(id=id)
  template = loader.get_template('m_update.html')
  context = {
    'member': member,
  }
  return HttpResponse(template.render(context, request))

def add_book(request): # Book Page Upload
  return render(request,'add_book.html')

def book_submit(request): # Add New Book
    if request.method == 'POST':
        S1 = request.POST.get("bname")
        S2 = request.POST.get("writer")
        S3 = request.POST.get("publisher")
        S4 = request.POST.get("type")
        S5 = request.POST.get("edition")
        S6 = request.POST.get("price")
        S7 = request.POST.get("qty")
        T1 = Book(book_name = S1, writer_name = S2, publisher_name=S3, type_book=S4, book_edition=S5, book_price=S6, b_qty=S7)
        T1.save()
        return render(request,'home.html')
    return render(request,'add_book.html')

def delete(request, id): # Delete Book
  d1 = Book.objects.get(id=id)
  d1.delete()
  return render(request,'home.html')

def update(request, id): # Update Book
  books = Book.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):  # Update Book With Details
  US1 = request.POST.get("bname")
  US2 = request.POST.get("writer")
  US3 = request.POST.get("publisher")
  US4 = request.POST.get("type")
  US5 = request.POST.get("edition")
  US6 = request.POST.get("price")
  US7 = request.POST.get("qty")
  member = Book.objects.get(id=id)
  member.book_name = US1
  member.writer_name = US2
  member.publisher_name = US3
  member.type_book = US4
  member.book_edition = US5
  member.book_price = US6
  member.b_qty = US7
  member.save()
  return render(request,'home.html')

def library(request): # Books Details in Library Table
  books = Book.objects.all().values()
  template = loader.get_template('library.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))


def search(request): # Book Search Page Upload
    return render(request, 'search.html')

def search_result(request): # Book Search result Page 
    search_term = request.POST.get("search")
    t = request.POST.get("type")

    book = Book.objects.none()

    try:
        if t == "id":
            book = Book.objects.filter(id=int(search_term))
        elif t == "book_name":
            book = Book.objects.filter(book_name=search_term)
        elif t == "writer_name":
            book = Book.objects.filter(writer_name=search_term)
        elif t == "book_edition":
            book = Book.objects.filter(book_edition=search_term)
        elif t == "type_book":
            book = Book.objects.filter(type_book=search_term)
        elif t == "publisher_name":
            book = Book.objects.filter(publisher_name=search_term)
        elif t == "b_qty":
            book = Book.objects.filter(b_qty=search_term)
        elif t == "book_price":
            book = Book.objects.filter(book_price=search_term)
        else:
            return HttpResponse("Invalid search type.")
    except ValueError:
        return HttpResponse("Invalid search term for the selected type.")

    template = loader.get_template('search.html')
    context = {
        'book': book,
        'results_found': bool(book),
        'search_term': search_term,
    }
    return HttpResponse(template.render(context, request))

def issue(request):  #Book Issue Page
    M = request.POST.get("l_card_id")
    B = request.POST.get("book_id")
    member_exists = Member.objects.filter(id=M).exists()
    book_exists = Book.objects.filter(id=B).exists()
    books_available=Book.objects.filter(b_qty__gt=0)
    if member_exists and book_exists and books_available:
       member = Member.objects.get(id=M)
       book = Book.objects.get(id=B)
       fname = member.firstname
       lname = member.lastname
       mobile_no = member.mobile
       buk_name=book.book_name
       writer=book.writer_name
       publisher=book.publisher_name
       name= fname+" "+lname
       book.b_qty = int(book.b_qty)-int(1)
       S3_str = request.POST.get("i_date")
       S3 = datetime.strptime(S3_str, '%Y-%m-%d')
       S4 = S3 + timedelta(days=15)
       b_i = B_issue(l_Id=M,b_Id=B,i_date=S3, r_date=S4,m_name=name,mobile=mobile_no,book_name=buk_name,writer_name=writer,publisher_name=publisher)
       b_i.save()
       return render(request, 'home.html')
    else:
       return render(request, 'login_fail.html')
    
def b_i_request(request):
    book_issues = B_issue.objects.all().values()
    template = loader.get_template('b_i_request.html')
    context = {
        'book_issues': book_issues,
    }
    return HttpResponse(template.render(context, request))

def b_issue(request): # Book issue Page Upload
  return render(request,'b_issue.html')

def issue_request(request, id):
    book = get_object_or_404(B_issue, id=id)
    template = loader.get_template('issue_request.html')
    context = {'book': book}
    return HttpResponse(template.render(context, request))

def b_issued(request, id):  # Book Issue by admin
  M = request.POST.get("l_card_id")
  B = request.POST.get("book_id")
  US3 = request.POST.get("r_date")
  US4 = request.POST.get("i_date")
  S3 = datetime.strptime(US4, '%Y-%m-%d')
  S4 = S3 + timedelta(days=15)
  member = Member.objects.get(id=M)
  book = Book.objects.get(id=B)
  fname = member.firstname
  lname = member.lastname
  mobile_no = member.mobile
  buk_name=book.book_name
  writer=book.writer_name
  publisher=book.publisher_name
  name= fname+" "+lname
  book.b_qty = int(book.b_qty)-int(1) 
  t1=issued(l_Id=M, b_Id=B, i_date=US4, rqst_date=US3, r_date=S4, m_name=name, mobile=mobile_no, book_name=buk_name, writer_name=writer, publisher_name=publisher)
  rqst = B_issue.objects.get(id=id)
  rqst.delete()
  t1.save()
  return render(request,'home.html')

def reissue(request, id):
    book = get_object_or_404(issued, id=id)
    template = loader.get_template('b_reissue.html')
    context = {'book': book}
    return HttpResponse(template.render(context, request))

def b_reissued(request, id):
    risu = issued.objects.get(id=id)
    i_date = request.POST.get("R_date")
    date = datetime.strptime(i_date, '%Y-%m-%d')
    reissue_date = date + timedelta(days=7)
    risu.risu_date = reissue_date
    risu.r_date = None
    risu.save()
    return render(request, 'home.html')

def i_report(request): # Issued Book Report
  Buks = issued.objects.all().values()
  template = loader.get_template('report.html')
  context = {
    'Buks': Buks,
  }
  return HttpResponse(template.render(context, request))

def b_return(request, id): # Book Return Page
  books = issued.objects.get(id=id)
  template = loader.get_template('return.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))   

def return_b(request, id):  #edit here with fields
    issu = get_object_or_404(issued, id=id)
    member = Member.objects.get(id=id)
    book = Book.objects.get(id=id)
    if request.method == 'POST':
      S1 = request.POST.get("I_no")
      S2 = request.POST.get("book_id")
      S3 = request.POST.get("bname")
      S4 = request.POST.get("writer")
      S5 = request.POST.get("member_id")
      S6 = request.POST.get("m_name")
      S7 = request.POST.get("I_date") #issue Date
      S8 = request.POST.get("R_date") #return Date
      S9 = request.POST.get("b_reissue") #Reissue Date
      current_date = datetime.now()
      if S8:
            days_late = (current_date - S8).days
      elif S9:
          days_late = (current_date - S9).days
      else:
          days_late = 0 

      fine_per_day = 5  
      S10 = max(0, days_late * fine_per_day)
      S11= member.mobile
      S12=book.publisher_name
      rtrn = rturn(I_Id = S1, mobile=S11, publisher_name=S12, b_Id= S2, book_name=S3, writer_name=S4, l_Id=S5, m_name=S6, i_date=S7, r_date=S8, risu_date=S9, fine=S10)
      rtrn.save()
      issu.delete()
    return render(request, 'home.html')

def about_us(request): # About Page pload
  return render(request,'about_us.html')


def msg(request): # Error Page Upload
  return render(request,'Msg.html')

# def print(request, id): # recipits page
#   book = get_object_or_404(rturn, id=id)
#   template = loader.get_template('recipites.html')
#   context = {'book': book}
#   return HttpResponse(template.render(context, request))

def u_dash(request): # Staff Dashboard Upload
    return render(request, 'staff_dashboard.html')

def m_dash(request): # Member Dashboard Upload
    return render(request, 'member_dashboard.html')

def member_view(request): # Member Detailes For Staff View
  members = Member.objects.all().values()
  template = loader.get_template('member_view.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))

def rtr_file(request): # Books Details in Library Table
  books = rturn.objects.all().values()
  template = loader.get_template('rturnfile.html')
  context = {
    'books': books,
  }
  return HttpResponse(template.render(context, request))

def print(request, id): # # recipits page upload
  books = rturn.objects.get(id=id)
  template = loader.get_template('recipites.html')
  context = {
    'books': books,
  }
  return render(request, 'home.html')
  return HttpResponse(template.render(context, request))

# def print_detail(request,id): # recipits page print
#   {'id': id}
#   return render(request, 'home.html')