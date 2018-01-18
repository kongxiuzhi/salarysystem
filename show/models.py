from django.db import models


# Create your models here.



class User(models.Model):
	staffnum	= models.CharField(max_length=10,primary_key=True,unique=True)
	username 	= models.CharField(max_length=128)
	idcard		= models.CharField(max_length=18)
	banknum		= models.CharField(max_length=19)
	password	= models.CharField(max_length=250)
	active		= models.BooleanField(default=False)
	created		= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.staffnum
	class Meta:
		ordering =['-created','staffnum']

class Salary(models.Model):
	staffnum 	= models.ForeignKey(User,on_delete=models.CASCADE,related_name='salary')
	salarytime	= models.CharField(max_length=20)
	gwgz 	= models.DecimalField("岗位工资",max_digits=10,decimal_places=3)
	zjjt 	= models.DecimalField("职级津贴",max_digits=10,decimal_places=3)
	zwjt 	= models.DecimalField('职务津贴',max_digits=10,decimal_places=3)
	blgz 	= models.DecimalField("保留工资",max_digits=10,decimal_places=3)
	nggz 	= models.DecimalField('年功工资',max_digits=10,decimal_places=3)
	dqlcjt 	= models.DecimalField('地区留才津贴',max_digits=10,decimal_places=3)
	wpjt 	= models.DecimalField('外派津贴',max_digits=10,decimal_places=3)
	tgjt 	= models.DecimalField('特岗津贴',max_digits=10,decimal_places=3)
	gwgt 	= models.DecimalField('岗位津贴',max_digits=10,decimal_places=3)
	yjgz1 	= models.DecimalField('业绩工资1(OT)',max_digits=10,decimal_places=3)
	yjgz2 	= models.DecimalField('业绩工资2(OT)',max_digits=10,decimal_places=3)
	jbf 	= models.DecimalField('加班费',max_digits=10,decimal_places=3)
	cybjt	= models.DecimalField('长夜班津贴',max_digits=10,decimal_places=3)
	cdztkk 	= models.DecimalField('迟到早退扣款',max_digits=10,decimal_places=3)
	kgkk 	= models.DecimalField('旷工扣款',max_digits=10,decimal_places=3)
	bjkk 	= models.DecimalField('病假扣款',max_digits=10,decimal_places=3)
	sjkk 	= models.DecimalField('事假扣款',max_digits=10,decimal_places=3)
	zjljlj 	= models.DecimalField('总经理激励金',max_digits=10,decimal_places=3)
	xmjlj 	= models.DecimalField('项目激励金',max_digits=10,decimal_places=3)
	jhhj 	= models.DecimalField('结婚贺金',max_digits=10,decimal_places=3)
	tabc 	= models.DecimalField('提案报酬',max_digits=10,decimal_places=3)
	bjf 	= models.DecimalField('褒奖费',max_digits=10,decimal_places=3)
	sqbf	= models.DecimalField('税前补发',max_digits=10,decimal_places=3)
	sqkk 	= models.DecimalField('税前扣款',max_digits=10,decimal_places=3)
	yfgz 	= models.DecimalField('应发工资',max_digits=10,decimal_places=3)
	yanglbxgr 	= models.DecimalField('养老保险个人',max_digits=10,decimal_places=3)
	sybxge 	= models.DecimalField('失业保险个人',max_digits=10,decimal_places=3)
	yilbxgr 	= models.DecimalField('医疗保险个人',max_digits=10,decimal_places=3)
	zfgjjgr 	= models.DecimalField('住房公积金个人',max_digits=10,decimal_places=3)
	qynjgrjfsqkk 	= models.DecimalField('企业年金个人缴费税前扣款',max_digits=10,decimal_places=3)
	qynjgrjfsqbk 	= models.DecimalField('企业年金个人缴费税前补缴',max_digits=10,decimal_places=3)
	gzxzgrsds 	= models.DecimalField('工资薪资个人所得税',max_digits=10,decimal_places=3)
	dsznf 	= models.DecimalField('独生子女费',max_digits=10,decimal_places=3)
	kckk 	= models.DecimalField('餐费扣款',max_digits=10,decimal_places=3)
	jtzf 	= models.DecimalField('集体房租',max_digits=10,decimal_places=3)
	qynjgrjfshkk 	= models.DecimalField('企业年金个人缴费税后扣款',max_digits=10,decimal_places=3)
	qynjgrjfshbk 	= models.DecimalField('企业年金个人缴费税后补缴',max_digits=10,decimal_places=3)
	shbf  	= models.DecimalField('税后补发',max_digits=10,decimal_places=3)
	shkk  	= models.DecimalField('税后扣款',max_digits=10,decimal_places=3)
	sfgz 	= models.DecimalField('实发工资',max_digits=10,decimal_places=3)
	created		= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return str(self.staffnum)
	class Meta:
		ordering = ["-created","staffnum__staffnum"]

class LoadUserFile(models.Model):
	userfile 	= models.FileField(upload_to='useradd/%Y/%m/%d/%s')
	created 	= models.DateTimeField(auto_now_add=True)
	name 		= models.CharField(max_length=64)

	def __str__(self):
		return self.name 
	class Meta:
		ordering = ['-created']

class LoadSalaryFile(models.Model):
	salaryfile 	= models.FileField(upload_to='salaryadd/%Y/%m/%d/%s')
	created 	= models.DateTimeField(auto_now_add=True)
	name 		= models.CharField(max_length=64)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['-created']
		