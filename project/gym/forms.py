from django.utils import timezone
from django import forms
from .models import User, Trainer,TrainingPlan,DietPlan, Goal, Payment

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email', 'phone']


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name' , 'surname', 'email', 'phone', 'specialisation' , 'skills']

class TrainingPlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        trainer = kwargs.pop('trainer')
        super(TrainingPlanForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(trainer=trainer)
        self.fields['trainer'].initial = trainer
        self.fields['created_at'].initial = timezone.now()

    class Meta:
        model = TrainingPlan
        fields = ['trainer', 'user', 'created_at', 'description']

class DietPlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        trainer = kwargs.pop('trainer')
        super(DietPlanForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(trainer=trainer)
        self.fields['trainer'].initial = trainer
        self.fields['created_at'].initial = timezone.now()

    class Meta:
        model = DietPlan
        fields = ['trainer', 'user', 'created_at', 'plan_type','description']

class DateInput(forms.DateInput):
    input_type = 'date'

class GoalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(GoalForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user

    class Meta:
        model = Goal
        fields = ['user', 'goal_description', 'target_date', 'status']
        widgets = {
            'target_date': DateInput(),
        }

class PaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PaymentForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user
            self.fields ['date'].initial = timezone.now()
            self.fields['amount'].initial = 0
            
    class Meta:
        model = Payment
        fields = ['user', 'amount', 'date', 'type']
