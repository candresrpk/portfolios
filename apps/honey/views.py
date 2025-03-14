from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction
# Create your views here.


def home_view(request):
    request.patterns = 'honey'
    return render(request, './honey/home.html')


def transactions_list_view(request):
    request.patterns = 'honey'

    transactions = Transaction.objects.filter(owner=request.user)

    context = {
        'transactions': transactions
    }

    return render(request, './honey/transactions.html', context)


def create_view(request):

    context = {
        'form': TransactionForm
    }

    if request.method == 'GET':
        return render(request, './honey/create.html', context)

    else:
        try:
            form = TransactionForm(request.POST)
            print(request.POST)
            if form.is_valid():
                new_transaction = form.save(commit=False)
                new_transaction.owner = request.user

                if new_transaction.transaction_type == 'Expense':
                    new_transaction.amount = new_transaction.amount * -1

                new_transaction.save()
                return redirect('honey:home')
            else:
                context['form'] = form
                context['message'] = 'Pleashe check your input'
                return render(request, './honey/create.html', context)
        except Exception as e:
            context['message'] = str(e)
            return render(request, './honey/create.html', context)
