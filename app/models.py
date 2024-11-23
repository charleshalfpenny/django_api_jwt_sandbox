from django.db import models


class Employee(models.Model):

  class Meta:
    db_table = 'customer'
    verbose_name_plural = "employees"
        
  last_name = models.CharField(max_length=20, blank=False, default='')
  first_name = models.CharField(max_length=20, blank=False, default='')
  age = models.IntegerField(blank=False, default=0)   

  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'