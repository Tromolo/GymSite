from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import User,Trainer,TrainingPlan,DietPlan,Goal , Payment
from .forms import UserForm , TrainerForm, TrainingPlanForm , DietPlanForm, GoalForm , PaymentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    trainers = Trainer.objects.all()
    users = User.objects.all()
    return render(request, 'users.html', {'users': users, 'form': form, 'trainers':trainers})

def trainers(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainers')
    else:
        form = TrainerForm()

    trainers = Trainer.objects.all()
    return render(request, 'trainers.html', {'trainers': trainers, 'form' : form})

def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def trainer_detail(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    return render(request, 'trainer_detail.html', {'trainer': trainer})

def assign_trainer(request, user_id, trainer_id):
    user = get_object_or_404(User, pk=user_id)
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    user.trainer = trainer
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def create_training_plan(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    if request.method == 'POST':
        form = TrainingPlanForm(request.POST, trainer=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_detail', trainer_id=trainer.id)
    else:
        form = TrainingPlanForm(trainer=trainer)
    return render(request, 'create_training_plan.html', {'form': form})

def user_training_plans(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    training_plans = TrainingPlan.objects.filter(user=user)
    return render(request, 'user_training_plans.html', {'training_plans': training_plans})

def create_diet_plan(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    if request.method == 'POST':
        form = DietPlanForm(request.POST, trainer=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_detail', trainer_id=trainer.id)
    else:
        form = DietPlanForm(trainer=trainer)
    return render(request, 'create_diet_plan.html', {'form' : form})

def user_diet_plans(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    diet_plans = DietPlan.objects.filter(user=user)
    return render(request, 'user_diet_plans.html', {'diet_plans': diet_plans})

def create_goal(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = GoalForm(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user_id)
    else:
        form = GoalForm(user=user)
    return render(request, 'create_goal.html', {'form': form})

def user_show_goal(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    goals = Goal.objects.filter(user=user)
    return render(request, 'user_show_goal.html', {'goals': goals , 'user' : user})

def update_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal, user=goal.user)
        if form.is_valid():
            form.save()
            return redirect('user_show_goal', user_id=goal.user.id)
    else:
        form = GoalForm(instance=goal, user=goal.user)
    return render(request, 'update_goal.html', {'form': form})


def delete_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    if request.method == 'POST':
        goal.delete()
        return redirect('user_show_goal', user_id=goal.user.id)
    return render(request, 'confirm_delete.html', {'object': goal})

def create_payment(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = PaymentForm(user=user)
        return render(request, 'create_payment.html', {'form': form})

def user_show_payment(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    payments = Payment.objects.filter(user=user)
    return render(request, 'user_show_payment.html', {'payments': payments, 'user' : user})

def update_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment, user=payment.user)
        if form.is_valid():
            form.save()
            return redirect('user_show_payment', user_id=payment.user.id)
    else:
        form = PaymentForm(instance = payment, user = payment.user)
        return render(request, 'update_payment.html', {'form': form})
    
def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    if request.method == 'POST':
        payment.delete()
        return redirect('user_show_payment', user_id=payment.user.id)
    return render(request, 'confirm_delete.html', {'object': payment})
    
def trainer_show_training_plan(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    training_plans = TrainingPlan.objects.filter(trainer=trainer)
    return render(request, 'trainer_show_training_plan.html', {'trainer': trainer, 'training_plans': training_plans})


def trainer_show_diet_plan(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    diet_plans = DietPlan.objects.filter(trainer=trainer)
    return render(request, 'trainer_show_diet_plan.html', {'trainer': trainer, 'diet_plans': diet_plans})
