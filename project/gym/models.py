from django.db import models

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=12)
    specialisation = models.CharField(max_length=100)
    skills = models.CharField(max_length=50)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=12)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment of {self.amount} {self.type} by {self.user} on {self.date}"

class DietPlan(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField()
    plan_type = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.plan_type} Diet Plan for {self.user} created on {self.created_at}"

class TrainingPlan(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField()
    description = models.TextField(max_length=100)

    def __str__(self):
        return f"Training Plan by {self.trainer} for {self.user}"
    
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_description = models.CharField(max_length=200)
    target_date = models.DateTimeField()
    status = models.CharField(max_length=12)

    def __str__(self):
        return f"Goal for {self.user}: {self.goal_description}, Target Date: {self.target_date}, Status: {self.status}"