from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .forms import LoginForm,PasswordResetForm,DateForm
from .models import User,Salary
from django.urls import reverse

# Create your views here.


def indexView(request,staffnum):
	staffnum1 = request.session.get('staffnum')
	if staffnum == staffnum1:
		#return redirect('/login/')
	#salary = Salary.objects.get(staffnum=staffnum)
		user = User.objects.get(staffnum=staffnum)
		if not user.active:
			return redirect(reverse('resetpassword',args=[staffnum]))
		else:
			form = DateForm()
			return render(request,'show/index.html',{'staffnum':staffnum,'form':form})
	else:
		return redirect('/login/')


def loginView(request):
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			staffnum = form.cleaned_data['staffnum']
			password = form.cleaned_data['password']
			user = User.objects.get(staffnum=staffnum)
			if not user:
				return HttpResponse("do not have the person")
			elif user.password==password:
				request.session['username'] = user.username
				request.session['staffnum'] = user.staffnum
				return redirect(reverse('index',args=[user.staffnum]))
			else:
				return HttpResponse("staffnum or password wrong")
	else:
		form = LoginForm()

	return render(request,'show/login.html',{'form':form})

def logoutView(request):
	del request.session['staffnum']
	del request.session['username']

	return redirect('/login/')

def resetpassword(request,staffnum):
	staffnum1 = request.session.get('staffnum')
	if staffnum == staffnum1:
		if request.method =="POST":
			form = PasswordResetForm(request.POST)
			if form.is_valid():
				datas = form.cleaned_data
				password = datas['password']
				try:
					user = User.objects.get(staffnum=staffnum,password=password)
				except User.DoesNotExist:
					HttpResponse("password error")
				
				if datas['password1'] and datas['password2'] and datas['password1'] == datas['password2']:
					user.password = datas['password1']
					user.active = True
					user.save()
					return redirect(reverse('index',args=[user.staffnum]))
				else:
					return HttpResponse("again")

		else:
			form = PasswordResetForm()
		return render(request,'show/resetpasswd.html',{'form':form})
	else:
		return redirect('/login/')

def showSalary(request):
	staffnum = request.session.get('staffnum')
	if staffnum:
		if request.method == 'POST':
			form = DateForm(request.POST)
			if form.is_valid():
				year = form.cleaned_data['year']
				month = form.cleaned_data['month']
				date = year + month
				try:
					salary = Salary.objects.get(staffnum=staffnum,salarytime=date)
				except Salary.DoesNotExist:
					return HttpResponse("salary null")
				return render(request,'show/showsalary.html',{'date':date,'salary':salary})




