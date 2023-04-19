from django.db import models

category=(
	('Entertainment','Entertainment'),('Eductional','Eductional'),('Lifestyle','Lifestyle'),('food','food'),('common','common'),('productivity','productivity'))

sub_category=(
	('social Media','social Media'),('games','games'),('coding','coding'),('kids','kids'),('clothing','clothing'),('fashion','fashion'),('local','local'),('allindia','allindia'),('common','common'),('utility','utility'),('finance','finance'),('music','music'),('travel','travel'))


#database for app
class myLoginDetials(models.Model):
	image=models.ImageField(upload_to='app_images/',blank=False)
	app_name=models.CharField(max_length=100,blank=False)
	app_link=models.CharField(max_length=200,blank=False)
	app_category=models.CharField(choices=category, max_length=255,default=1)
	sub_category=models.CharField(choices=sub_category, max_length=255,default=1)
	points_amount = models.PositiveIntegerField(blank=False)

	def __str__(self):#for displaying app name in admin
		return (self.app_name,self.image)


#database for user
class myUserDetials(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

	def __str__(self):#for displaying user name in admin
		return self.username

#data base for screenshot
class myscreenshot(models.Model):
	image=models.ImageField(upload_to='screenshot/')

	def __str__(self):
		return '<img src="%s"/>' % self.image.url

