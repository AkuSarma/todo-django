from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    my_id = models.AutoField(primary_key=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todoName = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.todoName