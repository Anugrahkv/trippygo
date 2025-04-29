from django.shortcuts import render,redirect
from travelapp.models import *
from django.http import HttpResponseRedirect
import os 
import datetime
from datetime import timedelta,date
import string
from datetime import datetime as dd
# Create your views here.
def index(request):
	# specialcatogory=specialcatogory=specialcatogory_tb.objects.all()

	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')
	location=addloc_tb.objects.all().order_by("locationadd")
	query=packages_tb.objects.filter(category="DISCOUNT OFFERS")[:4]
	query1=packages_tb.objects.filter(specialcategory="Solo")[:4]
	query2=packages_tb.objects.filter(specialcategory="Honeymoon")[:4]
	query3=packages_tb.objects.filter(specialcategory="Holiday")[:4]
	query4=packages_tb.objects.filter(specialcategory="Family")[:4]


	print(specialcatogory,"*************")
	return render(request,"index.html",{'data':query,'datas':query1,'datass':query2,'datasss':query3,'datassss':query4,"specialcatogory":specialcatogory,"location":location})

def about(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')	
	# return render(request,"about.html",{"specialcatogory":specialcatogory})
	query=packages_tb.objects.filter(category="DISCOUNT OFFERS")[:4]
	return render(request,"about.html",{'data':query,"specialcatogory":specialcatogory})


def services(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')
	data=review_tb.objects.filter(status="approved")[:2]
	query=packages_tb.objects.all()
	return render(request,"services.html",{"specialcatogory":specialcatogory,"data":data,"query":query})
	
def details(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')
	pid=request.GET['pid']
	query=packages_tb.objects.filter(id=pid)
	data=packageimages_tb.objects.filter(package=pid)
	query1=review_tb.objects.filter(package_id=pid)


	return render(request,"details.html",{"specialcatogory":specialcatogory,'query':query,'data':data,'query1':query1})





def special(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')		
	sid=request.GET["scid"]
	print(sid,"////////////////")
	query=packages_tb.objects.filter(specialcategory=sid)
			# query=packages_tb.objects.filter(state=varplace,packagetype=varpackagestype)
	print(query,"*****************")
	return render(request,"special.html",{'data':query,"specialcatogory":specialcatogory})
	# category=specialcatogory_tb.objects.all()
	# return render(request,"special.html",{"category":category})


	
def discount(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')		
	# if request.session.has_key('myid'):		
	# 	if request.method=="POST":

			# data=[]
			# data=[vartrip_in,noofdays,varmembers,varadult,varchildren]
			# print(data,"**************")
	query=packages_tb.objects.filter(category="DISCOUNT OFFERS")
			# query=packages_tb.objects.filter(state=varplace,packagetype=varpackagestype)

	return render(request,"discount.html",{'data':query,"specialcatogory":specialcatogory})
	# 	else:
	# 		return render(request,"discount.html")
	# else:
	# 	return render(request,"login.html")
	# return render(request,"discount.html")

def contact(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')	
	return render(request,"contact.html",{"specialcatogory":specialcatogory})


# def pricing(request):
# 	if request.session.has_key('myid'):	
# 		query=packages_tb.objects.all()
# 		return render(request,"pricing.html",{'data':query})
# 	else:
# 		return HttpResponseRedirect('/login/')



# def contact(request):
	# specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')	
	# if request.method=="POST":
	# 	varname=request.POST['Name']
	# 	varemail=request.POST['Email']
	# 	varphone=request.POST['Phone']
	# 	varmessage=request.POST['Message']
	# 	add=contact_tb(name=varname,email=varemail,phone=varphone,message=varmessage)
	# 	add.save()
		# return render(request,"contact.html",{"specialcatogory":specialcatogory})
	# else:
	# 	return render(request,"contact.html",{"specialcatogory":specialcatogory})




def register(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')	
	if request.method=="POST":
		varname=request.POST['Name']
		varemail=request.POST['Email']
		varpassword=request.POST['Password']
		vargender=request.POST['Gender']
		varphone=request.POST['Phone']
		varguardian=request.POST['Guardian']
		varage=request.POST['Age']
		check=reg_tb.objects.all().filter(email=varemail)
		if check:
			return render(request,"register.html",{"specialcatogory":specialcatogory})
		else:
			query=reg_tb(name=varname,email=varemail,password=varpassword,gender=vargender,phone=varphone,guardian=varguardian,age=varage)
			query.save()
			return render(request,"register.html",{"specialcatogory":specialcatogory})
	else:
		return render(request,"register.html",{"specialcatogory":specialcatogory})

def login(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')	
	if request.method=="POST":
		email=request.POST['Email']
		password=request.POST['Password']
		check=reg_tb.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session["myid"]=x.id
				request.session["uname"]=x.name

				return HttpResponseRedirect("/")
		else:
			return render(request,"login.html",{"error":"Invalid Details or Not registered","specialcatogory":specialcatogory})
	else:
		return render(request,"login.html",{"specialcatogory":specialcatogory})

def logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['uname']

		return HttpResponseRedirect('/')
	else: 
		return HttpResponseRedirect('/')


# def toursearch(request):
# 	if request.session.has_key('myid'):

# 		if request.method=="POST":
# 			vardate= datetime.datetime.now().date
# 			varpackagestype=request.POST['packagestype']
# 			varplace=request.POST['place']
# 			# varuser=request.session['myid']
# 			vartrip_in=request.POST['trip_in']
# 			vartrip_out=request.POST['trip_out']
# 			varmembers=request.POST['members']
# 			varcouples=request.POST['couples']
# 			varadult=request.POST['adult']
# 			varchildren=request.POST['children']

# 			search=tourlist.objects.filter(state=varplace,packagetype=varpackagestype)
# 			lists={'vartrip_in':vartrip_in,'vartrip_out':vartrip_out,'varmembers':varmembers}
# 			if search:
# 				return render(request,"search.html",{"data":search,'lists':lists})

				
# 			else:
# 				return render(request,"index.html",{'error':"no package list aviliable as your selection "})
# 		else:
# 			return render(request,"index.html")
# 	else:
# 		return render(request,"login.html")


# def booking(request):
# 	if request.session.has_key('myid'):
# 		if request.method=="POST":
# 			bid=request.GET['bid']
# 			data=tourlist_tb.objects.filter(id=bid)

# 	else:
# 		return render(request,"login.html")

# def offerbooking(request):
# 	if request.session.has_key('myid'):
# 		if request.method=="POST":
# 			bid=request.GET['bid']
# 			tripdate=request.POST['tripdate']
# 			cdate=datetime.datetime.now().date()

# 			data=packages_tb.objects.filter(id=bid)
# 			add=offerbooking(date=cdate,tid=tripid,status="paid",user=usrid,trip_in=tripdate)
# 			add.save()
# 			return render(request,"index.html")
# 		else:
# 		return render(request,"login.html")


def searching(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')	
	if request.session.has_key('myid'):		
		if request.method=="POST":
			# varpackagestype=request.POST['packagestype']
			varlocation=request.POST['location']
			# vartrip_in=request.POST['trip_in']
			# noofdays=request.POST['noofdays']
			# varmembers=request.POST['members']
			# varcouples=request.POST['couples']
			# varadult=request.POST['adult']
			# varchildren=request.POST['children']
			
			data=[]
			# data=[vartrip_in,noofdays,varmembers,varadult,varchildren]
			# print(data,"**************")
			query=packages_tb.objects.filter(location=varlocation)
			# query=packages_tb.objects.filter(state=varplace,packagetype=varpackagestype)

			return render(request,"searching.html",{'data':query,"search":data,"specialcatogory":specialcatogory})
		else:
			return render(request,"searching.html",{"specialcatogory":specialcatogory})
	else:
		return render(request,"login.html",{"specialcatogory":specialcatogory})

def order(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')
	uid=request.session['myid']
	query=booking.objects.filter(uid=uid).order_by("-id")
	if query:
		for x in query:
			submit_date=x.trip_in
			date_time_str = submit_date
			submit_date = dd.strptime(date_time_str, '%Y-%m-%d').date()
			# if x.bookpackageid.days:
			cout_day=x.bookpackageid.days
			cout_day=int(cout_day)
			pkg=x.bookpackageid.id
			status=x.status
			# else:
			# 	cout_day=0
		print(submit_date,"------------------------",type(submit_date))
		# print(cout_day,"------------------------")
		cdate=datetime.datetime.now().date()

		total_day=submit_date+timedelta(days=cout_day)
		ctotal_day=submit_date-timedelta(days=3)

		# print(ctotal_day,"/////////////////////////////")
		review=review_tb.objects.filter(uid=uid,package_id=pkg)
		# print(review,"888888888888888888888888888888888")


		if cdate>=total_day:
			if not review:
				if status == "booked":
					reviewdate='yes'
				else:
					reviewdate='no'

			else:
				reviewdate='no'
		else:
			reviewdate='no'


		# if cdate<ctotal_day:
		# 	if status == "booked":
		# 		cancel='yes'
		# 	else:
		# 		cancel='no'

			
		# else:
		# 	cancel='no'
		cancel=ctotal_day

		data=packages_tb.objects.all()
		return render(request,"order.html",{"specialcatogory":specialcatogory,'query':query,'data':data,'reviewdate':reviewdate,"review":review,"cancel":cancel,"cdate":cdate})

	else:
		# specialcatogory=specialcatogory_tb.objects.all()
		return render(request,"order.html",{"specialcatogory":specialcatogory})

# def completed(request):
# 	bid=request.GET["bid"]
# 	booking.objects.filter(id=bid).update(status="completed")
# 	return HttpResponseRedirect("/order/")

def cancel(request):
	bid=request.GET["bid"]
	booking.objects.filter(id=bid).update(status="canceled")
	return HttpResponseRedirect("/order/")

def review(request):
	if request.method=="POST":
		pkgs=request.GET["pid"]
		varname=request.POST['name']
		varimage=request.FILES['image']
		# varimage=request.FILES.get['image']
		varstar=request.POST['star']
		varexperience=request.POST['experience']
		uid=request.session['myid']
		vardate=datetime.datetime.now().date()

		userid=reg_tb.objects.get(id=uid)
		pkgt=booking.objects.filter(id=pkgs)
		for x in pkgt:
			pkg=x.bookpackageid.id
		pkgid=packages_tb.objects.get(id=pkgs)
		check=review_tb.objects.filter(name=varname,image=varimage,star=varstar,experience=varexperience,uid=userid,package_id=pkgid,date=vardate)
		if check:
			pkgt=packages_tb.objects.filter(id=pkg)
			return render(request,"review.html",{"pkg":pkg,"pkgt":pkgt})
		else:
			add=review_tb(name=varname,image=varimage,star=varstar,experience=varexperience,uid=userid,package_id=pkgid,date=vardate)
			add.save()
			booking.objects.filter(id=pkgs).update(status="completed")
			return render(request,"review.html",{"msg":"Thank You for Submiting Review"})
	else:
		pkg=request.GET["pid"]
		pkgt=packages_tb.objects.filter(id=pkg)
		return render(request,"review.html",{"pkg":pkg,"pkgt":pkgt})

	
# def searching(request):
# 	if request.session.has_key('myid'):		
# 		if request.method=="POST":
# 			# varpackagestype=request.POST['packagestype']
# 			varlocation=request.POST['location']
# 			# vartrip_in=request.POST['trip_in']
# 			# noofdays=request.POST['noofdays']
# 			# varmembers=request.POST['members']
# 			# varcouples=request.POST['couples']
# 			# varadult=request.POST['adult']
# 			# varchildren=request.POST['children']
			
# 			data=[]
# 			# data=[vartrip_in,noofdays,varmembers,varadult,varchildren]
# 			# print(data,"**************")
# 			query=packages_tb.objects.filter(location=varlocation)
# 			# query=packages_tb.objects.filter(state=varplace,packagetype=varpackagestype)

# 			return render(request,"searching.html",{'data':query,"search":data})
# 		else:
# 			return render(request,"searching.html")
# 	else:
# 		return render(request,"login.html")



###############################################################################################################################################
############################################# ADMIN ###########################################################################################


def admin_login(request):
	if request.method=="POST":
		email=request.POST['Email']
		password=request.POST['Password']
		check=adminlogin.objects.filter(email=email,password=password)
		if check:
			for x in check:
				request.session["nameid"]=x.id
				request.session['adminemail']=x.email
				# return HttpResponseRedirect("/")
				return render(request,"admin/adminindex.html",{"success":"Login Success"})

		else:
			return render(request,"admin/adminlogin.html",{"error":"Invalid Details or Not registered"})
	else:
		return render(request,"admin/adminlogin.html")

def adminlogout(request):
	if request.session.has_key('nameid'):
		del request.session['nameid']
		del request.session['adminemail']
		return HttpResponseRedirect('/')
	else: 
		return HttpResponseRedirect('/')

def adminindex(request):
	return render(request,"admin/adminindex.html")

def booked(request):
	query=booking.objects.all()
	data=payment_tb.objects.all().filter(status="paid").order_by("-id")
	return render(request,"admin/booked.html",{'query':query,'data':data})

def bookingcancel(request):
	# query1=booking.objects.all()
	query=booking.objects.all().filter(status="canceled").order_by("-id")
	# data=payment_tb.objects.all().filter(status="canceled").order_by("-id")
	return render(request,"admin/bookingcancel.html",{'query':query})

# def reviewlist(request):
# 	query=review_tb.objects.all()
# 	return render(request,"admin/reviewlist.html",{'query':query})
# 	# return render(request,"admin/reviewlist.html")

def reviewlist(request):
    upd=review_tb.objects.all().filter(status="pending")
    upd1=review_tb.objects.all().filter(status="approved")
 
    return render(request,"admin/reviewlist.html",{'db':upd,'db1':upd1})


    # query=turf_owner_reg_tb.objects.all()
    # return render(request,"admin/turfownerlist.html",{'query':query})

def admin_approve_review(request):
    id=request.GET['id']
    review_tb.objects.all().filter(id=id).update(status="approved")
    upd=review_tb.objects.all().filter(status="pending")
    upd1=review_tb.objects.all().filter(status="approved")
    return render(request,"admin/reviewlist.html",{'db':upd,'db1':upd1})

def delete_review(request):
	pid=request.GET['pid']
	review_tb.objects.filter(id=pid).delete()
	return HttpResponseRedirect("/reviewlist/")	



# def contactform(request):
# 	contactdetails=contact_tb.objects.all()
# 	return render(request,"admin/contactform.html",{"query":contactdetails})

	# return render(request,"admin/contactform.html")

def images(request):
	destinationname=packages_tb.objects.all()
	if request.method=="POST":
		varimage1=request.FILES['image1']
		varimage2=request.FILES['image2']
		varimage3=request.FILES['image3']
		destination=request.POST['destination']
		destination=packages_tb.objects.get(id=destination)

		add=packageimages_tb(image1=varimage1,image2=varimage2,image3=varimage3,package=destination)
		add.save()
		
		return render(request,"admin/images.html",{"destinationname":destinationname})
	else:
		return render(request,"admin/images.html",{"destinationname":destinationname})



def packages(request):
	if request.method=="POST":
		varlocation=request.POST['location']
		vardestination=request.POST['destination']
		vardays=request.POST['days']
		varnights=request.POST['nights']
		varcnum=request.POST['cnum']
		varcategory=request.POST['category']
		varimage=request.FILES['image']
		varspecialcategory=request.POST['specialcategory']
		varamount=request.POST['amount']
		vardiscamount=request.POST['discamount']
		vardiscpercentage=request.POST['discpercentage']
		varlocation=addloc_tb.objects.get(id=varlocation)

		if vardays == "1":
			varday1=request.POST['day1']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all()
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == "2":
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == "3":
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == "4":
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 5:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 6:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 7:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 8:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 9:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 10:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 11:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 12:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 13:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			varday13=request.POST['day13']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		elif vardays == 14:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			varday13=request.POST['day13']
			varday14=request.POST['day14']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		else:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			varday13=request.POST['day13']
			varday14=request.POST['day14']
			varday15=request.POST['day15']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,day15=varday15,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			if check:
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
			else:
				add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,day15=varday15,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				add.save()
				category=specialcatogory_tb.objects.all() 
				location=addloc_tb.objects.all().order_by("locationadd")
				return render(request,"admin/packages.html",{"category":category,"location":location})
		
		# check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,day15=varday15,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
		# if check:
		# 	return render(request,"admin/packages.html")
		# else:
		# 	add=packages_tb(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,day15=varday15,image=varimage,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
		# 	add.save()
		# 	return render(request,"admin/packages.html")
	else:
		category=specialcatogory_tb.objects.all()
		location=addloc_tb.objects.all().order_by("locationadd")
		return render(request,"admin/packages.html",{"category":category,"location":location})

def userlist(request):
	query=reg_tb.objects.all()
	return render(request,"admin/userlist.html",{'query':query})



def packagelist(request):
	query=packages_tb.objects.all()
	return render(request,"admin/packagelist.html",{'query':query})	


def userreject(request):
   duid=request.GET["did"]
   query=reg_tb.objects.filter(id=duid).update(status="0")
   return HttpResponseRedirect("/userlist/")

def useraprove(request):
   duid=request.GET["did"]
   query=reg_tb.objects.filter(id=duid).update(status="1")
   return HttpResponseRedirect("/userlist/")


def admincate(request):
	category=specialcatogory_tb.objects.all()
	return render(request,"admin/packages.html",{"category":category})


# def tourpacklist(request):
# 	query=tourlist_tb.objects.all()
# 	return render(request,"admin/tourpacklist.html",{'query':query})	

# def offerbooking(request):
# 	query=payment_tb.objects.all()
# 	return render(request,"admin/offerbooking.html",{'query':query})

# def servicepackages(request):
# 	if request.method=="POST":
# 		vardestinations=request.POST['destinations']
# 		vardays=request.POST['days']
# 		# vardetails=request.POST['details']
# 		varnights=request.POST['nights']
# 		varamount=request.POST['amount']
# 		varpackagetype=request.POST['packagetype']	
# 		check=servicepackages_tb.objects.all().filter(destinations=vardestinations,days=vardays,nights=varnights,cnum=varcnum,amount=varamount,packagetype=varpackagetype)
# 		if check:
# 			return render(request,"admin/servicepackages.html")
# 		else:
# 			add=servicepackages_tb(destinations=vardestinations,days=vardays,nights=varnights,cnum=varcnum,amount=varamount,packagetype=varpackagetype)
# 			add.save()
# 			return render(request,"admin/servicepackages.html")
# 	else:
# 		return render(request,"admin/servicepackages.html")


# def tourpack(request):
# 	if request.method=="POST":
# 		varstate=request.POST['state']
# 		vardestination=request.POST['destination']
# 		vartype=request.POST['type']
# 		varamount=request.POST['amount']
# 		varcamount=request.POST['camount']		
# 		check=tourlist_tb.objects.all().filter(state=varstate,location=varlocation,destination=vardestination,packagetype=vartype,amount=varamount,camount=varcamount)
# 		if check:
# 			return render(request,"admin/tourpack.html")
# 		else:
# 			add=tourlist_tb(state=varstate,location=varlocation,destination=vardestination,packagetype=vartype,amount=varamount,camount=varcamount)
# 			add.save()
# 			return render(request,"admin/tourpack.html")
# 	else:
# 		return render(request,"admin/tourpack.html")
# 	return render(request,"admin/tourpacklist.html")




def bookings(request):
	if request.method=="POST":
		uid=request.session['myid']
		tid=request.GET['tid']
		ttid=packages_tb.objects.get(id=tid)
		uidd=reg_tb.objects.get(id=uid)
		# varstatus=request.POST['status']
		vardate=datetime.datetime.now().date()
		vartrip_in=request.POST['trip_in']
		varadults=request.POST['adults']
		varchildrens=request.POST['childrens']
			
		varchildamount=request.POST['childamount']
		varadultamount=request.POST['adultamount']
		varamount=float(varchildamount)+float(varadultamount)
		add=booking(bookpackageid=ttid,uid=uidd,status="pending",date=vardate,trip_in=vartrip_in,adults=varadults,childrens=varchildrens,amount=varamount,childamount=varchildamount,adultamount=varadultamount)
		add.save()
		obj = booking.objects.filter(uid=uidd).latest('id').id
		# dd= booking.objects.get('id')
		print(obj,"---------------------------------------")
		return redirect(f"/payment/?tid={tid}&bid={obj}")
	else:
		price=request.GET['gt']
		return render(request,"details.html",{"price":price})

def payment(request):
	if request.method == "POST":
		tid=request.GET['tid']
		bid=request.GET['bid']
		ttid=booking.objects.get(id=bid)
		data=booking.objects.filter(id=bid)
		vartamount=request.POST['amount']
		uid=request.session['myid']
		uidd=reg_tb.objects.get(id=uid)
		vardate=datetime.datetime.now().date()
		add=payment_tb(bookingid=ttid,uid=uidd,status="paid",date=vardate,amount=vartamount)
		add.save()
		booking.objects.filter(id=bid).update(status="booked")
		return HttpResponseRedirect("/")
	else:
		tid=request.GET['tid']
		bid=request.GET['bid']
		ttid=booking.objects.get(id=bid)
		data=booking.objects.filter(id=bid)
		return render(request,"payment.html",{"data":data,"tid":tid,'bid':bid})

# def searchbookings(request):
# 	if request.session.has_key('myid'):
# 		if request.method=="POST":
# 			uid=request.session['myid']
# 			uidd=reg_tb.objects.get(id=uid)
# 			cdate=datetime.datetime.now().date()
# 			amount=request.POST['amount']
# 			sid=request.GET['sid']
# 			add=serachpayment_tb(uid=uidd,status=paid,amount=amount,date=cdate)
# 			add.save()
# 			return render(request,"index.html")
# 		else:
# 			price=request.GET['gt']
# 			return render(request,"bookings.html",{"price":price})



def specialfield(request):
	if request.method=="POST":
		varcategoryfield=request.POST['categoryfield']
		check=specialcatogory_tb.objects.all().filter(categoryfield=varcategoryfield)
		if check:
			return render(request,"admin/specialfield.html")
		else:
			add=specialcatogory_tb(categoryfield=varcategoryfield)
			add.save()
			return render(request,"admin/specialfield.html")
	else:
		return render(request,"admin/specialfield.html")

def specialfieldlist(request):
	query=specialcatogory_tb.objects.all()
	return render(request,"admin/specialfieldlist.html",{'query':query})

def addlocation(request):
	if request.method=="POST":
		varlocationadd=request.POST['locationadd']
		check=addloc_tb.objects.all().filter(locationadd=varlocationadd)
		if check:
			return render(request,"admin/addlocation.html")
		else:
			add=addloc_tb(locationadd=varlocationadd)
			add.save()
			return render(request,"admin/addlocation.html")
	else:
		return render(request,"admin/addlocation.html")

def locationlist(request):
	query=addloc_tb.objects.all()
	return render(request,"admin/locationlist.html",{'query':query})

def imageslist(request):
	query=packageimages_tb.objects.all()
	return render(request,"admin/imageslist.html",{'query':query})


def updatepkgimg(request):
	if request.method == "POST":
		imgup=request.POST['imgup']
		imgup2=request.POST['imgup2']
		imgup3=request.POST['imgup3']
		pid=request.GET['pid']
		if imgup == "Yes":
			image1=request.FILES["image1"]
			oldrec=packageimages_tb.objects.filter(id=pid)
			updrec=packageimages_tb.objects.get(id=pid)
			for x in oldrec:
				imgurl=x.image1.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image1=image1
			updrec.save()

		if imgup2 == "Yes":
			image2=request.FILES["image2"]
			oldrec=packageimages_tb.objects.filter(id=pid)
			updrec=packageimages_tb.objects.get(id=pid)
			for x in oldrec:
				imgurl=x.image2.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image2=image2
			updrec.save()

		if imgup3 == "Yes":
			image3=request.FILES["image3"]
			oldrec=packageimages_tb.objects.filter(id=pid)
			updrec=packageimages_tb.objects.get(id=pid)
			for x in oldrec:
				imgurl=x.image3.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image3=image3
			updrec.save()




		# packageimages_tb.objects.filter(id=pid).update()
		return HttpResponseRedirect("/imageslist/")

	else:
		pid=request.GET['pid']
		query=packageimages_tb.objects.filter(id=pid)
		return render(request,"admin/imageslistupdate.html",{'query':query})

def deletepkgimg(request):
	pid=request.GET['pid']
	packageimages_tb.objects.filter(id=pid).delete()
	return HttpResponseRedirect("/imageslist/")	



def package_delete(request):
    if request.session.has_key('nameid'):
        pid=request.GET['uuid']
        oldrec=packages_tb.objects.filter(id=pid)
        for x in oldrec:
            imageurl=x.image.url
            pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
            if os.path.exists(pathtoimage):
                os.remove(pathtoimage)
                # prfloat('Successfully deleted')
        packages_tb.objects.filter(id=pid).delete()
        packageimages_tb.objects.filter(package=pid).delete()
        return HttpResponseRedirect("/packagelist/")
    else: 
        return HttpResponseRedirect('/adminlogin/')


def update(request):
	if request.method == "POST":
		pid=request.GET['uuid']
		varlocation=request.POST['location']
		vardestination=request.POST['destination']
		vardays=request.POST['days']
		varnights=request.POST['nights']
		varcnum=request.POST['cnum']
		varcategory=request.POST['category']
		imgup=request.POST['imgup']
		if imgup == "yes":
			varimage=request.FILES['image']
			oldrec=packages_tb.objects.filter(id=pid)
			updrec=packages_tb.objects.get(id=pid)
			for x in oldrec:
				imgurl=x.image.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.image=varimage
			updrec.save()
		
		varspecialcategory=request.POST['specialcategory']
		varamount=request.POST['amount']
		vardiscamount=request.POST['discamount']
		vardiscpercentage=request.POST['discpercentage']
		location=addloc_tb.objects.all().order_by("locationadd")
		varlocation=addloc_tb.objects.get(id=varlocation)


		if vardays == "1":
			varday1=request.POST['day1']
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			category=specialcatogory_tb.objects.all()
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == "2":
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
				
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == "3":
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == "4":
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
		
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 5:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 6:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 7:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 8:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 9:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 10:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
		
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 11:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
		
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 12:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
		
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 13:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			varday13=request.POST['day13']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
		
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		elif vardays == 14:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			varday13=request.POST['day13']
			varday14=request.POST['day14']
		
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")
		else:
			varday1=request.POST['day1']
			varday2=request.POST['day2']
			varday3=request.POST['day3']
			varday4=request.POST['day4']
			varday5=request.POST['day5']
			varday6=request.POST['day6']
			varday7=request.POST['day7']
			varday8=request.POST['day8']
			varday9=request.POST['day9']
			varday10=request.POST['day10']
			varday11=request.POST['day11']
			varday12=request.POST['day12']
			varday13=request.POST['day13']
			varday14=request.POST['day14']
			varday15=request.POST['day15']
			check=packages_tb.objects.all().filter(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,day15=varday15,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
		
			packages_tb.objects.filter(id=pid).update(location=varlocation,destination=vardestination,days=vardays,nights=varnights,cnum=varcnum,day1=varday1,day2=varday2,day3=varday3,day4=varday4,day5=varday5,day6=varday6,day7=varday7,day8=varday8,day9=varday9,day10=varday10,day11=varday11,day12=varday12,day13=varday13,day14=varday14,day15=varday15,category=varcategory,specialcategory=varspecialcategory,amount=varamount,discamount=vardiscamount,discpercentage=vardiscpercentage)
			
			category=specialcatogory_tb.objects.all() 
			location=addloc_tb.objects.all().order_by("locationadd")
			return HttpResponseRedirect("/packagelist/")

		
	else:
		pid=request.GET['uuid']
		data=packages_tb.objects.filter(id=pid)
		location=addloc_tb.objects.all().order_by("locationadd")

		return render(request,"admin/update.html",{"data":data,"location":location})


# def imageslistupdate(request):
# 	query=packageimages_tb.objects.all()
# 	return render(request,"admin/imageslistupdate.html",{'query':query})	

def reviewpage(request):
	specialcatogory=packages_tb.objects.raw('SELECT * FROM travelapp_packages_tb GROUP BY specialcategory ORDER BY specialcategory')
	data=review_tb.objects.filter(status="approved")
	return render(request,"reviewpage.html",{"specialcatogory":specialcatogory,"data":data})