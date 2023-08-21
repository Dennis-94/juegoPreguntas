from django.db import models

# Create your models here.
"""class User(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField(default=0)
"""

class Level(models.Model):
    name = models.CharField(max_length=50, null= False, blank= False)
    weight = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.id}  | {self.name}  | {self.weight}"

class Question(models.Model):
    question = models.TextField(null= False, default="")
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}  | {self.question}  | {self.level}"

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    answer = models.TextField(null= False, default="")
    is_correct = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.id}  | {self.answer}  | {self.is_correct}"
        

class Attemp(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.question}  | {self.answer}"












"""class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    emp_name =  models.CharField(max_length=60)
    emp_department = models.CharField(max_length=60)
    emp_age = models.IntegerField(default=0)

class Comment(models.Model):
    author = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    """