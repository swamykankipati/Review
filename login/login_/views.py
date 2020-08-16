from django.shortcuts import render
from django.contrib import messages
def account(request):
	if(request.method=='POST'):
		first_name=request.POST['username']
		pass_word=request.POST['password']
		if(first_name=='swami' and pass_word=='apssdc'):
			messages.info(request,"login successfully")
			return render(request,"account.html",{})
		else:
			messages.error(request,"invalid credentials")
			return render(request,"login.html",{})
	return render(request,"login.html",{})


def login(request):
	return render(request,"login.html",{})

	

