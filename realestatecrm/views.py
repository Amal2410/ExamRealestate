from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from realestatecrm.forms import RealestateForm

from realestatecrm.models import Realestate

class RealestateCreateView(View):

    template_name="realestate_add.html"

    form_class=RealestateForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():
            
            form_instance.save()

            return redirect("realestate-list")
        
        return render(request,self.template_name,{"form":form_instance})

class RealestateListView(View):

    template_name="realestate_list.html"

    def get(self,request,*args,**kwargs):

        qs=Realestate.objects.all()

        return render(request,self.template_name,{"data":qs})
    
class RealestateUpdateView(View):

    template_name="realestate_update.html"

    form_class=RealestateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_object=Realestate.objects.get(id=id)

        form_instance=self.form_class(instance=employee_object)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_object=Realestate.objects.get(id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=employee_object)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("realestate-list")
        
        return render(request,self.template_name,{"form":form_instance})
    
class RealestateDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Realestate.objects.get(id=id).delete()

        return redirect("realestate-list")
    