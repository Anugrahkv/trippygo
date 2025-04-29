from django.db import models

# Create your models here.
class reg_tb(models.Model):
	name=models.CharField(max_length=100,null=False)
	email=models.CharField(max_length=100,null=False)
	password=models.CharField(max_length=100,null=False)
	gender=models.CharField(max_length=100,null=False)
	phone=models.CharField(max_length=100,null=False)
	guardian=models.CharField(max_length=100,null=False)
	age=models.CharField(max_length=100,null=False)
	status=models.CharField(max_length=50,null=False,default="1")














###############################################################################################################################################
############################################# ADMIN ###########################################################################################
class adminlogin(models.Model):
    email=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)

class specialcatogory_tb(models.Model):
	categoryfield=models.CharField(max_length=100,null=False)

class addloc_tb(models.Model):
	locationadd=models.CharField(max_length=100,null=False)

class packages_tb(models.Model):
	location= models.ForeignKey(addloc_tb, on_delete=models.CASCADE)
	destination=models.CharField(max_length=100,null=False)
	days=models.CharField(max_length=100,null=False)
	nights=models.CharField(max_length=100,null=False)
	cnum=models.CharField(max_length=100,null=False)
	day1=models.TextField(null=False)
	day2=models.TextField(null=False)
	day3=models.TextField(null=False)
	day4=models.TextField(null=False)
	day5=models.TextField(null=False)
	day6=models.TextField(null=False)
	day7=models.TextField(null=False)
	day7=models.TextField(null=False)
	day8=models.TextField(null=False)
	day9=models.TextField(null=False)
	day10=models.TextField(null=False)
	day11=models.TextField(null=False)
	day12=models.TextField(null=False)
	day13=models.TextField(null=False)
	day14=models.TextField(null=False)
	day15=models.TextField(null=False)
	category=models.CharField(max_length=100,null=False)
	image=models.FileField(upload_to="package/")
	specialcategory=models.CharField(max_length=100,null=False)
	amount=models.CharField(max_length=100,null=False)
	discamount=models.CharField(max_length=100,null=False)
	discpercentage=models.CharField(max_length=100,null=False)

class packageimages_tb(models.Model):
	image1=models.FileField(upload_to="packageimages/")
	image2=models.FileField(upload_to="packageimages/")
	image3=models.FileField(upload_to="packageimages/")
	package=models.ForeignKey(packages_tb,on_delete=models.CASCADE)

class review_tb(models.Model):
	uid=models.ForeignKey(reg_tb,on_delete=models.CASCADE)
	package_id=models.ForeignKey(packages_tb,on_delete=models.CASCADE)
	date=models.CharField(max_length=100,null=False)
	name=models.CharField(max_length=100,null=False)
	experience=models.CharField(max_length=100,null=False)
	image=models.FileField(upload_to="reviewimages/")
	star=models.CharField(max_length=100,null=False)
	status=models.CharField(max_length=50,null=False,default="pending")


# class contact_tb(models.Model):
	# uid=models.ForeignKey(reg_tb,on_delete=models.CASCADE)
	# name=models.CharField(max_length=100,null=False)
	# email=models.CharField(max_length=100,null=False)
	# phone=models.CharField(max_length=100,null=False)
	# message=models.CharField(max_length=100,null=False)

# class servicepackages_tb(models.Model):
# 	destinations=models.CharField(max_length=100,null=False)
# 	days=models.CharField(max_length=100,null=False)
# 	nights=models.CharField(max_length=100,null=False)
# 	packagetype=models.CharField(max_length=100,null=False)
# 	details=models.CharField(max_length=600,null=False)
# 	amount=models.CharField(max_length=100,null=False)



# class tourlist_tb(models.Model):
# 	state=models.CharField(max_length=100)
# 	destination=models.CharField(max_length=100)
# 	packagetype=models.CharField(max_length=100)
# 	amount=models.CharField(max_length=100)
# 	camount=models.CharField(max_length=100)



class booking(models.Model):
	uid=models.ForeignKey(reg_tb, on_delete=models.CASCADE)
	date=models.CharField(max_length=100,null=False)
	bookpackageid=models.ForeignKey(packages_tb,on_delete=models.CASCADE)
	status=models.CharField(max_length=100,null=False)
	trip_in=models.DateField(null=False,default="")
	adults=models.CharField(max_length=100,null=False)
	# amount=models.CharField(max_length=100,null=False)
	childrens=models.CharField(max_length=100,null=False)
	amount=models.CharField(max_length=100,null=False)
	childamount=models.CharField(max_length=100,null=False)
	adultamount=models.CharField(max_length=100,null=False)


class payment_tb(models.Model):
	uid=models.ForeignKey(reg_tb,on_delete=models.CASCADE)
	status=models.CharField(max_length=225)
	bookingid=models.ForeignKey(booking,on_delete=models.CASCADE)
	date=models.DateField()
	amount=models.CharField(max_length=225)

# class searchpayment_tb(models.Model):
# 	uid=models.ForeignKey(reg_tb,on_delete=models.CASCADE)
# 	status=models.CharField(max_length=225)
# 	total=models.CharField(max_length=225)
# 	data=models.DateField()	
# 	tid=models.ForeignKey(tourlist_tb,on_delete=models.CASCADE)
# 	noofdays=models.CharField(max_length=225)
# 	trip_in=models.CharField(max_length=225)
# 	couples=models.CharField(max_length=225)
# 	adult=models.CharField(max_length=225)
# 	children=models.CharField(max_length=225)
# 	members=models.CharField(max_length=225)