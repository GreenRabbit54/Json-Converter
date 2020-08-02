from django.db import models

class Persons(models.Model):
    rank = models.IntegerField()
    employer = models.CharField(max_length=100)
    employeesCount = models.IntegerField()
    medianSalary = models.IntegerField()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return self.rank






from json import load as json_load

with open('data.json') as f:
    json_data = json_load(f)
for record in json_data:
    Persons.objects.bulk_create([

        Persons(
            id=record['rank'],
            employer=record['employer'],
            employeesCount=record['employeesCount'],
            medianSalary=record['medianSalary'],
        )



])

print('ok')
print(json_data)