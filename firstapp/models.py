from django.db import models

class Member(models.Model):
  id = models.IntegerField(primary_key=True)
  firstname = models.CharField(max_length=255, default ="0000000000")
  lastname = models.CharField(max_length=255,default ="0000000000")
  d_o_b = models.CharField(max_length=250,default ="YYYY/MM/DD")
  address = models.TextField(max_length=255, default ="0000000000")
  mobile = models.IntegerField(default ="0000000000")
  email = models.CharField(max_length=255, default ="0000000000")
  m_type = models.CharField(max_length=255, default ="0000000000")

class Book(models.Model):
  id = models.IntegerField(primary_key=True)
  book_name = models.CharField(max_length=255)
  writer_name = models.CharField(max_length=255)
  publisher_name = models.CharField(max_length=255, default= "XYZ")
  type_book = models.CharField(max_length=255, default= "Generel")
  book_price = models.CharField(max_length=25, default = "00")
  book_edition = models.CharField(max_length=255, default= "1st")
  b_qty = models.CharField(max_length=255, default="0")

class Users(models.Model):
  id = models.IntegerField(primary_key=True)
  username=models.CharField(max_length=255)
  email_id=models.CharField(max_length=255)
  pass_word=models.CharField(max_length=255)
  l_type=models.CharField(max_length=255,null=True)

class Login_history(models.Model):
  id = models.IntegerField(primary_key=True)
  username=models.CharField(max_length=255)
  user_type=models.CharField(max_length=255)
  date=models.CharField(max_length=255)
  
class B_issue(models.Model):
  id = models.IntegerField(primary_key = True)
  l_Id= models.CharField(max_length=255)
  m_name = models.CharField(max_length=255, default ="0000000000")
  b_Id=models.CharField(max_length=255, default="00")
  book_name = models.CharField(max_length=255, null=True)
  mobile = models.IntegerField(default ="0000000000")
  writer_name = models.CharField(max_length=255, null=True)
  publisher_name = models.CharField(max_length=255, null=True)
  i_date=models.DateField()
  r_date=models.DateField(default = "1999-01-01")
  

class issued(models.Model):
  id = models.IntegerField(primary_key = True)
  l_Id= models.CharField(max_length=255)
  m_name = models.CharField(max_length=255, default ="0000000000")
  b_Id=models.CharField(max_length=255, default="00")
  book_name = models.CharField(max_length=255, null=True)
  mobile = models.IntegerField(default ="0000000000")
  writer_name = models.CharField(max_length=255, null=True)
  publisher_name = models.CharField(max_length=255, null=True)
  i_date=models.DateField()
  r_date=models.DateField(null=True)
  rqst_date=models.DateField(null=True)
  risu_date=models.DateField(null=True)

class rturn(models.Model):
  id = models.IntegerField(primary_key = True)
  I_Id= models.IntegerField(default="0001")
  l_Id= models.CharField(max_length=255)#memberID
  m_name = models.CharField(max_length=255, default ="0000000000")
  b_Id=models.CharField(max_length=255, default="00")
  book_name = models.CharField(max_length=255, null=True)
  mobile = models.IntegerField(default ="0000000000")
  writer_name = models.CharField(max_length=255, null=True)
  publisher_name = models.CharField(max_length=255, null=True)
  i_date=models.DateField() #issue date
  r_date=models.DateField(null=True) #return Date
  risu_date=models.DateField(null=True) #reissue date
  fine=models.IntegerField()