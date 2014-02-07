from django.db import models,connection

# Create your models here.
class loftk_articlesManager(models.Manager):
	def title_count(self,keyword):
		return self.filter(title__icontains=keyword).count()
	
	def getlist(self):
		cursor = connection.cursor()
		cursor.execute("""select * from mysiteapp_loftk_articles""")
		return [row[1] for row in cursor.fetchall()]
	
class Author(models.Model):
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=20)
	enname = models.CharField(max_length=20)

class loftk_articles(models.Model):
	cat_id = models.IntegerField()
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.CharField(max_length=100)
	create_date = models.DateTimeField()
	objects = loftk_articlesManager()
	
	def __unicode__(self):
		return self.title

class user(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length=200)
	
class userrole(models.Model):
	user = models.ForeignKey(user)
	rolename = models.CharField(max_length=250)
	
class role(models.Model):
	userrole = models.ForeignKey(userrole)
	roles = models.CharField(max_length=200)

class Person(models.Model):
	 name = models.CharField('作者姓名', max_length=10)  
	 age = models.IntegerField('作者年龄')  
	
class Book(models.Model):  
	person = models.ForeignKey(Person)  
	title = models.CharField('书籍名称', max_length=10)  
	pubtime = models.DateField('出版时间')  
	
class Meta:
	app_label = ''
	

