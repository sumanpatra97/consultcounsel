from django.db import models

class Forum_table(models.Model):
    question=models.CharField(max_length=100,default=" ")
    email=models.CharField(max_length=100,default="ENTER YOUR EMAILID")
    answer=models.TextField(max_length=2000,blank=True)
    answer_set=models.TextField(max_length=2000,default=" ",blank=True)

class Transaction(models.Model):
    made_by = models.CharField(max_length=100)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=100)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

class Mentor(models.Model):
    Name=models.CharField(max_length=100,blank=False,default=" ")
    Mobileno=models.CharField(max_length=100,blank=True,default=" ")
    Email=models.CharField(max_length=100,blank=False,default=" ")
    Profession=models.CharField(max_length=200,default=" ",blank=True)
    Mentor_Img = models.ImageField(upload_to='',default=" ")

class Donation(models.Model):
    Name = models.CharField(max_length=90)
    Email=models.CharField(max_length=50,blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    Amount = models.IntegerField(default=100)
    Mobileno = models.CharField(max_length=100,default="100",blank=True)


class Primemember(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Mobileno=models.CharField(max_length=50)
    Plan=models.CharField(max_length=20,default=" ")

class Feedback(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=50,default=" ")
    Query=models.CharField(max_length=50)

class transcatid(models.Model):
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    transcation_id = models.CharField(unique=True, max_length=100, null=True, blank=True)

class Demo(models.Model):
    Name=models.CharField(max_length=100,default="")
    Email=models.CharField(max_length=100,default="")
    Mobileno=models.TextField(max_length=200,default="")
