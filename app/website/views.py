from typing import Any
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import DataCris
from django.views.generic import TemplateView, DeleteView
from .forms import DataCrisForm, AddDataCrisForm
from django.views.generic import TemplateView, FormView
from django.shortcuts import get_object_or_404, redirect
from website.utils import q_search
from django.db.models.query import QuerySet
from django.core.paginator import Paginator


# Class based view
class IndexView(TemplateView):
    model = DataCris
    template_name = "website/index.html"
    context_object_name = "items"
    allow_empty = False
    paginate_by = 12

    def get_queryset(self) -> QuerySet[Any]:
        items = DataCris.objects.all()
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if query:
            items = q_search(query)

        if order_by == 'masa_up':
            items = sorted(items, key=lambda x: x.get_masa_in_grams())
        elif order_by == 'masa_down':  # default order (по убыванию)
            items = sorted(items, key=lambda x: x.get_masa_in_grams(), reverse=True)
        elif order_by == 'by_id':  # default order (по убыванию)
            items =items.order_by('id')
        else:
            items = items.order_by('id')

        return items


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = self.get_queryset()

        paginator = Paginator(items, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['items'] = page_obj  # Use the paginated items
        context['page_obj'] = page_obj

        return context



class SingleIndexView(FormView):
    template_name = "website/single.html"
    form_class = DataCrisForm

    def get_object(self):
        return get_object_or_404(DataCris, id=self.kwargs["pk"])

    def form_valid(self, form):
        item = self.get_object()

        item.typ = form.cleaned_data['typ']
        item.masa = form.cleaned_data['masa']
        item.czystosc = form.cleaned_data['czystosc']
        item.barwa = form.cleaned_data['barwa']
        item.pochodzenie = form.cleaned_data['pochodzenie']
        item.wlasciciel = form.cleaned_data['wlasciciel']
        
        # Zapisz zmiany w obiekcie
        item.save()
        messages.success(self.request, "Item was successfully updated")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = self.get_object()
        return context

    def get_success_url(self):
        return reverse("website:index")


class AddIndexView(FormView):
    template_name = "website/add_record.html"
    form_class = AddDataCrisForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Item was successfully created")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse("website:index")



def delete_record(request, pk):
    item = get_object_or_404(DataCris, id=pk)
    item.delete()
    messages.success(request, "Item was successfully deleted")
    return redirect("website:index")
