from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import HttpResponse
from .forms import ProfileForm
# from .utils import calculate_risk

class LogIn(LoginView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        rememberme = request.POST.get('rememberme')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request=request, message="User not found!!!")
            return redirect('login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request=request, message="Incorrect password entered")
            return redirect('login')
        login(request=request, user=user)
        if not rememberme:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        messages.success(request=request, message="You've successfully logged in!")
        return redirect('profile')


class SignUp(CreateView):
    model = User
    fields = "__all__"
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        try:
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')

            if password1 != password2:
                messages.success(request, 'The passwords in both password fields are not the same!!!')
                return redirect('signup')

            if User.objects.filter(username=username).first():
                messages.success(request, "Such a user has already registered!!!")
                return redirect('signup')

            if User.objects.filter(email=email).first():
                messages.success(request, "This email has already been registered!!!")
                return redirect('signup')

            user_obj = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
            user_obj.set_password(raw_password=password1)
            user_obj.save()
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error {e}")
            return redirect('signup')

def user_logout(request):
    logout(request)
    return redirect(to='login')

@login_required
def profilepage(request):
    current_user = request.user
    current_profile = Profile.objects.get(user_id=current_user.id)
    
    context={'profile':current_profile}
    return render(request, 'profile.html', context)

@login_required
def update_profile(request,id):
    current_user = request.user
    if current_user.id != id:
        return redirect('profile')
    
    profile = Profile.objects.get(user_id=id)
    form = ProfileForm(request.POST or None, instance=profile)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request,'update_profile.html',{'form':form,'profile':profile})

@login_required
def apply_loan(request):
    interest_rate = 0.15
    loan_term = 24
    monthly_interest_rate = interest_rate / 12
    current_user = request.user
    current_profile = Profile.objects.get(user_id=current_user.id)
    current_expenditure=current_profile.own_house+current_profile.house_rent+current_profile.grocery_expense+current_profile.current_emis+current_profile.other_expenses
    current_balance=current_profile.current_salary-current_expenditure
    if(current_balance<=10000):
        return HttpResponse('Oops! better luck next time ')
    else:
        rate_calc=((1+monthly_interest_rate)**loan_term)/(((1+monthly_interest_rate)**loan_term)-1)
        principal = current_balance/(monthly_interest_rate*rate_calc)
        ans=round(principal)
        repayment_amount=(principal*0.0875)*2+principal
        res=round(repayment_amount)
        obj={"response":"Congrats! your Loan is Approved","principal":ans,"current_balance":current_balance,"repayment_amount":res}
        return render(request,"output.html",obj)
        # return HttpResponse(principal)
