

from rest_framework import viewsets, generics
from django.views import generic
from django.views.generic import View

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.core.files.storage import default_storage
from rest_framework import viewsets, generics
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView


from .forms import UserForm,JobForm,LoginForm
from django.contrib.auth.models import Permission,User
#for update
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Job,JobFinal
from .forms import JobFormFinal,JobFormFinalUpdate
##for user
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from JobSchd.models import JobFinal
from JobSchd.serializers import JobSerializer, UserSerializer

from PopGen.settings import MEDIA_ROOT

import os


#########################################

#### Rest API


#########################################
class JobFinalList(generics.ListCreateAPIView):
    queryset = JobFinal.objects.all()
    serializer_class = JobSerializer
    ##permission_classes = (IsAdminOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class JobFinalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobFinal.objects.all()
    serializer_class = JobSerializer
    ##permission_classes = (IsAdminOrReadOnly, )

#########################################
#########################################











class UserJob(generic.ListView):
    model = JobFinal
    paginate_by = 10

    template_name = 'JobSchd/Details.html'
    def get_queryset(self):
        user=self.request.user
        return user

def saveJobDetails(request):
    checkboxOptions = {'on': True, 'off': False}
    checkboxValues = ['export', 'geo_all_ids', 'collate_across_geos', 'region_all_ids', 'arc' ]
    if 'geo' in request.POST and request.POST['geo'] != "":
        groupQuarterEnabled = True
    else:
        groupQuarterEnabled = False
    newJob = JobFinal()
    newJob.user = request.user
    if not os.path.exists(MEDIA_ROOT + str(request.user) + "/"  + request.POST["job_name"]):
        os.makedirs(MEDIA_ROOT + str(request.user) + "/"  + request.POST["job_name"])

    for k in checkboxValues:
        if k in request.POST:
            exec('newJob.{KEY} = {VALUE}'.format(KEY = k, VALUE = checkboxOptions[request.POST[k]]))
        else:
            exec('newJob.{KEY} = {VALUE}'.format(KEY = k, VALUE = False))

    for k in request.POST:
        if not groupQuarterEnabled and (k.find("groupquarter") != -1):
            exec('newJob.{KEY} = ""'.format(KEY = k))

        elif k in checkboxValues:
            continue
        else:
            exec('newJob.{KEY} = "{VALUE}"'.format(KEY = k, VALUE = request.POST[k]))


    for f in request.FILES:
        short_path = str(request.user) + "/"  + request.POST["job_name"]+"/"+request.FILES[f].name
        file_path = default_storage.save('/'.join([MEDIA_ROOT,short_path]),
                                    request.FILES[f])
        short_path = file_path.split(MEDIA_ROOT+"/")[-1]
        exec('newJob.{KEY} = "{VALUE}"'.format(KEY = f, VALUE = short_path))
    newJob.Job_Pushed = True
    newJob.save()
    return newJob

def updateJobDetails(request, pk):
    checkboxOptions = {'on': True, 'off': False}
    checkboxValues = ['export', 'geo_all_ids', 'collate_across_geos', 'region_all_ids', 'arc' ]
    groupQuarterFields = ['geo', 'region_groupquarter', 'region_groupquarter_files', 'geo_groupquarter','geo_groupquarter_files','sample_groupquarter']
    fileFields = ['geo_to_sample', 'region_to_sample', 'region_to_geo', 'region_household_files', 'region_person_files',
    'region_groupquarter_files', 'geo_household_files', 'geo_person_files', 'geo_groupquarter_files',
    'sample_household', 'sample_person', 'sample_groupquarter' ]
    if 'geo' in request.POST and request.POST['geo'] != "":
        groupQuarterEnabled = True
    else:
        groupQuarterEnabled = False
    
    updateJob = JobFinal.objects.get(pk=pk)
    if not os.path.exists(MEDIA_ROOT + str(request.user) + "/"  + updateJob.job_name):
        os.makedirs(MEDIA_ROOT + str(request.user) + "/"  + updateJob.job_name)
    for k in checkboxValues:
        if k in request.POST:
            exec('updateJob.{KEY} = {VALUE}'.format(KEY = k, VALUE = checkboxOptions[request.POST[k]]))
        else:
            exec('updateJob.{KEY} = {VALUE}'.format(KEY = k, VALUE = False))
    
    for k in request.POST:
        if k in fileFields:
            continue
        elif k in checkboxValues:
            continue
        else:
            exec('updateJob.{KEY} = "{VALUE}"'.format(KEY = k, VALUE = request.POST[k]))

    for f in request.FILES:
        if request.FILES[f] != "":
            short_path = str(request.user) + "/"  + request.POST["job_name"]+"/"+request.FILES[f].name
            file_path = default_storage.save('/'.join([MEDIA_ROOT,short_path]),
                                        request.FILES[f])
            short_path = file_path.split(MEDIA_ROOT+"/")[-1]
            exec('updateJob.{KEY} = "{VALUE}"'.format(KEY = f, VALUE = short_path))
    if not groupQuarterEnabled:
        for l in groupQuarterFields: 
            exec('updateJob.{KEY} = ""'.format(KEY = l))
    updateJob.Job_Pushed = True
    updateJob.save()
    return updateJob

def updateJob(request, pk):
    if request.method == "GET":
        jobObject = JobFinal.objects.get(pk=pk).__dict__
        allValues = dict((k,str(v)) for k,v in jobObject.iteritems())
        checkboxOptions = {True: 'on', False: 'off'}
        checkboxValues = ['export', 'geo_all_ids', 'collate_across_geos', 'region_all_ids', 'arc' ]
        allValues['create'] = False
        return render(request, 'JobSchd/jobfinal_form.html',allValues)

    if request.method == "POST":
        updateJobDetails(request, pk)
        return redirect('/' + str(request.user.id) + '/')
 
    
def createJob(request):
    
    checkboxOptions = {True: 'on', False: 'off'}
    checkboxValues = ['export', 'geo_all_ids', 'collate_across_geos', 'region_all_ids', 'arc' ]
    allFields = JobFinal._meta.get_fields()
     
    
    # All default values
    allValues = {}
    for i in allFields:
        if i.name == "user":
            continue
        if i.get_default() == None:
            allValues[i.name] = ""
        else:
            allValues[i.name] = str(i.get_default())
            allValues[i.name + "_ht"] = str(i.help_text)
    allValues['geo'] = 'geo'
    allValues['region_groupquarter'] = '[gqrtotals]'
    allValues['geo_groupquarter'] = '[gqtotals, gqtype]'
    allValues['create'] = True

    if request.method == "POST":
        saveJobDetails(request)
    return render(request, 'JobSchd/jobfinal_form.html', allValues)


def deleteJob(request, pk):
    try:
        #jobId = request.GET.get('jobId', None)
        obj = JobFinal.objects.get(pk=pk)
        obj.delete()
        data = {
            'is_success': True
    	}
    except DoesNotExist:
        data = {
            'is_success': False
    	}

    return JsonResponse(data)

def validateUpdateSettings(request):

    if request.POST['email'] == "" or request.POST['password'] != request.POST['conf_password'] :
        return False
    return True

def updateSettings(request, pk):

    if request.method == "POST":
	
        if validateUpdateSettings(request):
           user = User.objects.get(id=request.user.id)
           if "password" in request.POST and request.POST["password"] != "":
           	user.set_password(request.POST["password"])
           user.email = request.POST["email"]
           user.save()
           user=authenticate(username=request.user,password=request.POST["password"])

           if user is not None:
               if user.is_active:
                   login(request,user)
           return redirect('/'+str(request.user.id)+'/settings')

    return render(request, 'JobSchd/user_settings.html', {})



class JobFinalCreate(CreateView):
    model = JobFinal
    #fields = '__all__'
    form_class = JobFormFinal
    #success_url = reverse_lazy('user_jobs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobFinalCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('JobSchd:user_details',kwargs={'pk': self.request.user.id})


class JobFinalUpdate(UpdateView):
    model = JobFinal
    form_class = JobFormFinalUpdate
    def get_success_url(self):
        return reverse('JobSchd:user_details',kwargs={'pk': self.request.user.id})

class JobFinalDelete(DeleteView):
    model = JobFinal
    form_class = JobFormFinal

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobFinalCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('JobSchd:user_details',kwargs={'pk': self.request.user.id})

class DetailsView(generic.DetailView):
    model = User
    template_name = 'JobSchd/Details.html'

class UserCreate(CreateView):
    model = User
    fields = ['username','email','password','first_name','last_name']


class IndexView(generic.ListView):
    template_name = 'JobSchd/index.html'

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)

def team(request):
    return render(
        request,
        'JobSchd/team.html',
    )



class UserFormView(View):
    form_class=UserForm
    template_name='JobSchd/registration_form.html'

    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            # clean ,normalize the data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return User Objects if cred are correct

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('JobSchd:index')

        return render(request,self.template_name,{'form':form})





