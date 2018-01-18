from django import forms

class LoginForm(forms.Form):
	staffnum = forms.CharField(max_length=10)
	password = forms.CharField(widget=forms.PasswordInput())

class PasswordResetForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput())
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())

class DateForm(forms.Form):
	years = (('2016','2016'),('2017','2017'),('2018','2018'))
	months = (('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08'),('09','09'),('10','10'),('11','11'),('12','12'))
	year = forms.ChoiceField(choices=years)
	month = forms.ChoiceField(choices=months)