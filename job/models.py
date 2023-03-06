from django.db import models
Job_type=[
    ('full time','full time'),
    ('part time','part time')
]

# Create your models here.
class job(models.Model):
    title=models.CharField(max_length=50)
    job_type=models.CharField(max_length=15,choices=Job_type)
    descrition =models.TextField(max_length=1000,default='descrition')
    published_at =models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=1)
    experiance=models.IntegerField(default=1)
    catagory=models.ForeignKey('Category',on_delete=models.CASCADE)




    def __str__(self):
        return self.title

class Category (models.Model):
    title=models.CharField(max_length=50)  


    def __str__(self):
        return self.title      
   

