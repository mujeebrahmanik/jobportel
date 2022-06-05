from django.db import models

# Create your models here.
class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=100)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title

#python manage.py makemigrations
#python manage.py migrate

# ORM query for creating table objects
# Jobs.objects.create(job_title="UI developer",company_name="luminar",location="kakkanad",salary="250000",experience="3")

#fetching all objects from database
#qs=Jobs.objects.all()   qs is a variable

#fetching specific objects from database ( in case of fetching objects where experiences equal to 1)
#Jobs.objects.filter(experience=1)

#fetching specific objects from database ( in case of fetching objects where experiences greater than  1)
#Jobs.objects.filter(experience__gt=1)

#fetching specific objects from database ( in case of fetching objects where experiences less than  1)
#Jobs.objects.filter(experience__lt=1)

#fetching specific objects from database ( in case of fetching objects where experiences greater than or equal to  1)
#Jobs.objects.filter(experience__gte=1)

#fetching specific objects from database ( in case of fetching objects where experiences less than or equal to 1)
#Jobs.objects.filter(experience__lte=1)

#fetching specific object from database
# qs=Jobs.objects.get(id=5)

#update database values for a specific object(in case of experience of id 5)
#qs=Jobs.objects.get(id=5)
#qs.experience=2(new value)
#qs.save()

#delete object from database(incase of id 2)
#qs=Jobs.objects.get(id=2)
#qs.delete()