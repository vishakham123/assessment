from django.shortcuts import render
from django.apps.registry import apps
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic.list import ListView

from .forms import CustomerForm

User = apps.get_model('user', 'User')

# class UserListView(ListView):
#     model = User
#     template_name = 'dashboard/petient/list.html'  
#     context_object_name = 'petients'  
#     paginate_by = 10
#     queryset = User.objects.all() 
def listView(request):
    return TemplateResponse(request, 'dashboard/petient/list_new.html')

def userList(request):
    data = []
    users = User.objects.all()
    for i in users:
        res = {}
        res['id'] = i.id
        res['first_name'] = i.first_name
        res['last_name'] = i.last_name
        res['birth_date'] = i.birth_date
        data.append(res)

    return JsonResponse(data, safe=False)



def create_petient(request):
    return TemplateResponse(request, 'dashboard/petient/form_new.html')

def ajax_form(request):
    if request.is_ajax():
        first_name = request.POST.get('first_name', None) 
        last_name = request.POST.get('last_name', None)
        birth_date = request.POST.get('birth_date', None)

        data = {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date
        }
        User.objects.create(**data)

        return JsonResponse({'msg':'Your form has been submitted successfully',
                            'status': True})

    


def edit_petient(request, pk=None):
    petient = get_object_or_404(User, pk=pk)
    form = CustomerForm(request.POST or None, instance=petient)
    if form.is_valid():
        form.save()

        msg = pgettext_lazy(
            'Dashboard message', 'Updated Petient %s') % petient
        messages.success(request, msg)
        return redirect('dashboard:petient-list')
    ctx = {'form': form, 'petient': petient}
    return TemplateResponse(request, 'dashboard/petient/form.html', ctx)

def customer_details(request, pk):
    queryset = User.objects.all()
    petient = get_object_or_404(queryset, pk=pk)
    ctx = {
        'petient': petient}
    return TemplateResponse(request, 'dashboard/petient/detail.html', ctx)

def delete_petient(request, pk=None):
    petient = get_object_or_404(User, pk=pk)
    petient.delete()
    msg = pgettext_lazy(
            'Dashboard message', 'Delete Petient %s') % petient
    messages.success(request, msg)
    return JsonResponse({"msg":"Petient Delete Successfully!", "success":True})
