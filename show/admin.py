#coding:utf-8
from django.contrib import admin
from .models import Salary,User,LoadUserFile,LoadSalaryFile
from django.conf import settings
from .insert import insert
import os 
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display 	= ('username','staffnum','idcard','banknum','active')
	search_fields	= ['username','staffnum','idcard','banknum']
	list_filter 	= ['created','updated','active']
	#list_editable	= ['idcard','banknum','active']
	date_hierarchy	= 'created'


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
	list_display 	= ('staffnum','salarytime','created','updated')
	search_fields	= ['staffnum__staffnum']
	list_filter 	= ['created','updated','salarytime']
	date_hierarchy	= 'created'



def loadUserIn(modeladmin,request,queryset):
	filename 	= os.path.join(settings.BASE_DIR,'media/',str(queryset[0].userfile))
	print(filename)
	insert(filename,"1")
loadUserIn.short_description="importuserdata"

def loadSalaryIn(modeladmin,request,queryset):
	filename 	= os.path.join(settings.BASE_DIR,'media/',str(queryset[0].salaryfile))
	#print(filename)
	insert(filename,"2")
loadSalaryIn.short_description="importsalarydata"




@admin.register(LoadSalaryFile)
class LoadSalaryFile(admin.ModelAdmin):
	list_display	= ['name','created']
	actions = [loadSalaryIn]

@admin.register(LoadUserFile)
class LoadUserFile(admin.ModelAdmin):
	list_display	= ['name','created']
	actions = [loadUserIn]
