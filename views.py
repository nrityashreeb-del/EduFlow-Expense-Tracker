from django.shortcuts import render, redirect 
from .models import Expense

def index(request):
    if request.method == "POST":
        item = request.POST.get('item_name')
        price = request.POST.get('amount')
        
        if item and price:
            Expense.objects.create(item_name=item, amount=price)
            return redirect('index') 

    all_expenses = Expense.objects.all().order_by('-date')
    total_amount = sum(expense.amount for expense in all_expenses)
    
    context = {
        'expenses': all_expenses,
        'total': total_amount,
    }
    return render(request, 'tracker/index.html', context)