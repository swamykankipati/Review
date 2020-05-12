from django.shortcuts import render,redirect
from django.http import HttpResponse
def hi(request):
	return HttpResponse("""<h2>Hello Swami</h2>""")
def hello(request):
	return HttpResponse("""<h2>Hello Swami we are in Hello Function</h2>""")
def rollno(reg,id):
	txt = '<h2>This is ur id {} </h2>'.format(id)
	return HttpResponse(txt)
def st(reg,ld):
	txt = '<h2>This is ur id {} </h2>'.format(ld)
	return HttpResponse(txt)
