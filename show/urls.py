from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^login/$',views.loginView,name="login"),
	url(r'^index/(?P<staffnum>\d+)/$',views.indexView,name='index'),
	url(r'^logout/$',views.logoutView,name='logout'),
	url(r'^resetpassword/(?P<staffnum>\d+)/$',views.resetpassword,name='resetpassword'),
	url(r'^showsalary/$',views.showSalary,name='showSalary'),
]