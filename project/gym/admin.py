from django.contrib import admin
from .models import User, Trainer, Payment, DietPlan, TrainingPlan, Goal

# Register your models here.
admin.site.register(Trainer)
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(TrainingPlan)
admin.site.register(Goal)
admin.site.register(DietPlan)
