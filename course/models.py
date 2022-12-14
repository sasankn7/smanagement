from django.db import models

# Create your models here.


class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_title=models.CharField(max_length=100)
    instractor_name=models.CharField(max_length=100)
    capacity=models.IntegerField(default=30)
    open_seats=models.IntegerField(default=30)
    
    class Meta:
        verbose_name_plural='Course'
        db_table='course'
    def __str__(self):
        return self.course_title
    
class Students(models.Model):
        reg_no=models.AutoField(primary_key=True)
        name=models.CharField(max_length=100)
        email=models.EmailField(max_length=100)
        course_id=models.ForeignKey('Course',on_delete=models.CASCADE)
        phone=models.CharField(max_length=100)
        instractor_name=models.CharField(max_length=100)
        
        class Meta:
            verbose_name_plural='Students'
            db_table='students'
        def __str__(self):
            return self.name
        
class Instractor(models.Model):
    instractor_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    course_id=models.ForeignKey('Course',on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)
    course_title=models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='Instractor'
        db_table='instractor'
        
    def __str__(self):
        return self.name
    
    