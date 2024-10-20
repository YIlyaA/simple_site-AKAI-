from django.urls import reverse
from django.contrib import messages
from .models import DataCris
from .forms import DataCrisForm, AddDataCrisForm
from django.views.generic import TemplateView, FormView
from django.shortcuts import get_object_or_404, redirect
from website.utils import q_DataCris
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from website.paginations import PaginatedViewMixin


class DataCrisFormViewMixin:
    model = DataCris
    success_message = "Item was successfully processed"
    error_message = "Error"

    def get_object(self):
        return get_object_or_404(self.model, id=self.kwargs.get("pk"))

    def form_valid(self, form):
        form.save()
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class IndexView(TemplateView, PaginatedViewMixin):
    template_name = "website/index.html"

    def get_queryset(self) -> QuerySet[DataCris]:
        order_by: str = self.request.GET.get("order_by")
        query: str = self.request.GET.get("q")

        items = q_DataCris(query) if query else DataCris.objects.all()
        if items.count() == 0:
            messages.warning(self.request, "No items found")
            return items

        match order_by:
            case 'masa_up':
                items = sorted(items, key=lambda x: x.get_masa_in_grams())
            case 'masa_down':
                items = sorted(items, key=lambda x: x.get_masa_in_grams(), reverse=True)
            case 'by_id':
                items = items.order_by('-id')
            case _:
                items = items.order_by('id')

        return items

    def get_context_data(self, **kwargs) -> dict:
        context: dict = super().get_context_data(**kwargs)
        items = self.get_queryset()
        context['page_obj'] = self.paginate_queryset(items, self.paginate_by)
        context['items'] = context['page_obj']
        return context


class SingleIndexView(DataCrisFormViewMixin, FormView):
    template_name = "website/single.html"
    form_class = DataCrisForm
    success_message = "Item was successfully updated"

    def get_form(self, form_class=None) -> DataCrisForm:
        form_class = self.get_form_class()
        return form_class(instance=self.get_object(), **self.get_form_kwargs())

    def get_context_data(self, **kwargs) -> dict[str, object]:
        context: dict = super().get_context_data(**kwargs)
        context["item"] = self.get_object()
        return context

    def get_success_url(self):
        return reverse("website:index")


class AddIndexView(DataCrisFormViewMixin, FormView):
    template_name = "website/add_record.html"
    form_class = AddDataCrisForm
    success_message = "Item was successfully created"

    def get_success_url(self):
        return reverse("website:index")


def delete_record(request, pk: int):
    item = get_object_or_404(DataCris, id=pk)
    item.delete()
    messages.success(request, "Item was successfully deleted")
    return redirect("website:index")
