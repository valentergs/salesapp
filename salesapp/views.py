from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView
# from reports.views import ReportsListView
from salesapp.models import Customers, SapBase

def landing(request):
    return render(request, 'salesapp/landing.html')

def home(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse('Your account is not active')
            else:
                print('Some tried to login and failed')
                print('Username: {} and password {}'.format(username,password))
                return HttpResponse('Invalid username or password!')
        else:
            return render(request, 'index.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing'))

class CustomersListView(ListView):
    queryset = SapBase.objects.order_by('soldToName')
    context_object_name = 'cust_list'
    model = SapBase
    template_name = 'salesapp/customer_list.html'

    def get_queryset(self):
        qs = super(CustomersListView, self).get_queryset()
        return qs.filter(sellerNumber=self.request.user)

class CustomersDetailView(DetailView):
    model = SapBase
    context_object_name = 'cust_detail'
    template_name = 'salesapp/customer_detail.html'

class CustomersUpdateView(UpdateView):
    fields = ('products', 'is_active', 'country')
    model = SapBase
