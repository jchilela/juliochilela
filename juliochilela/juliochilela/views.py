from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect


def en(request):
	template = 'en.html'
	return render(request,template)

def pt(request):
	template = 'pt.html'
	return render(request,template)

def login(request):
        template = 'login.html'
        if request.method == 'GET':
        	user = request.GET.get('email')
	        password = request.GET.get('password')
	        #resultado = Utilizador.objects.filter(user=user,password=password)
	        #if resultado:
	        	#resultado = Utilizador.objects.filter(user=user,password=password)	        	
	        	#request.session['user']=user
	        	#request.session['password']=password
	   
	        	#template='home.html'
				#request.session['usuario_activo']=str(membro)
			#return HttpResponseRedirect('/home/')
	        #elif request.GET.get('email') and request.GET.get('password'):	
	         	#resultado = Utilizador.objects.all()
	       #  	resultado='Utilizador ou password incorrectos'
			#resultado='Utilizador ou password incorrectos'
	       #  	return render (request, template,{'resultado':resultado})
	else:
		a=2
	return  render(request, template)	   