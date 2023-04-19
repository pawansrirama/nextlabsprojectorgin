from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib.auth.views import LoginView
from .forms import *
from django.views.generic import DetailView



# This function will check admin username and password match's with suoeruser username and password
def admin_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user_obj = User.objects.filter(username = username)

		if not user_obj.exists():
			messages.warning(request, 'Account not found ')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		user_obj = authenticate(username = username , password = password)

		if user_obj and user_obj.is_superuser:
			login(request , user_obj)
			return redirect('loginauth/')

		messages.info(request,'invalid password')
		return redirect('invalidcredentials/')

	return render(request ,'login.html')



#if the username and password matched, new app can be added with detials 
def admin_page(request):
	if request.method=="POST":
		form=LoginDetials(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/user_login/')
	else:
		form=LoginDetials()
	return render(request,'loginauth.html',{'form':form})


#if admin types wrong username and password then it render an html file saying wrong credential login in again
def invaild_log(request):
	return render(request,'login_again.html')



#login for user
def user_page(request):
	if request.method=="POST":
		form=userLoginDetials(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('user_login')
	return render(request,'user_cre.html')


#after login home page is displayed with added apps
def user_login(request):
	user=myLoginDetials.objects.all()
	user1=myUserDetials.objects.all()
	return render(request,'user_Login.html',{'user':user,'user1':user1})


#function the renders the profile of user
def  profile(request):
	user1=myUserDetials.objects.all()
	return render(request,'profile.html',{'user1':user1})




#function calculate total points earned when app is downloaded
def totalpoints(request):
	user1=myUserDetials.objects.all()
	user=myLoginDetials.objects.all()
	my_value=[obj.points_amount for obj in user] 
	total=sum(my_value)
	return render(request,'totalpoints.html',{'total':total,'user1':user1})



#function render all the downloaded apps and display's the updated screenshorts
def task(request):
	user=myLoginDetials.objects.all()
	user1=myUserDetials.objects.all()
	user2=myscreenshot.objects.all()
	return render(request,'task.html',{'user':user,'user1':user1,'user2':user2})



#function renders detail of particular app when clicked and screenshot can be uploaded here
def ItemDetailView(request,id):
    app = myLoginDetials.objects.get(id=id)
    user1=myUserDetials.objects.all()
    if request.method == 'POST':
    	form2=userscreenshot(request.POST,request.FILES)
    	if form2.is_valid():
    		form2.save()
    		return redirect('user_login')

    form2 = userscreenshot()
    return render(request, 'item_detail.html',{'app': app,'form2':form2,'user1':user1})
