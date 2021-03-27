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

class UserListView(ListView):
    model = User
    template_name = 'dashboard/petient/list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'petients'  # Default: object_list
    paginate_by = 10
    queryset = User.objects.all()  # Default: Model.objects.all()
# Create your views here.
# def petient_list(request):
#     petients = User.objects.all().order_by("-id")
#     page = request.GET.get('page', 1)

#     paginator = Paginator(petients, 10)
#     try:
#         petients = paginator.page(page)
#     except PageNotAnInteger:
#         petients = paginator.page(1)
#     except EmptyPage:
#         petients = paginator.page(paginator.num_pages)

#     print(petients)
#     ctx = {
#         "petients": petients
#     }
#     return TemplateResponse(request, 'dashboard/petient/list.html', ctx)

def create_petient(request):
    petient = User()
    form = CustomerForm(request.POST or None, instance=petient)
    if form.is_valid():
        user = form.save()
        msg = pgettext_lazy(
                'Dashboard message', 'Added Petient %s') % petient
            # send_set_password_email.delay(customer.pk)
        messages.success(request, msg)
        return redirect('dashboard:petient-list')

    ctx = {'form': form, 'petient': petient}
    return TemplateResponse(request, 'dashboard/petient/form.html', ctx)

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
