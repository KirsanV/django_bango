from django.views import View, generic
from django.shortcuts import render
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import ProductForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

User = get_user_model()


class CanEditMixin:
    def user_can_edit(self, user, obj):
        if not user or not getattr(user, "is_authenticated", False):
            return False
        if getattr(obj, "owner", None) == user:
            return True
        if user.groups.filter(name="ProductModerators").exists():
            return True
        if user.has_perm("catalog.can_unpublish_product") or user.has_perm("catalog.delete_product"):
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        objs = context.get("products")
        if objs is not None:
            for obj in objs:
                obj.can_edit = self.user_can_edit(user, obj)
            return context

        obj = context.get("product") or context.get("object")
        if obj is not None:
            obj.can_edit = self.user_can_edit(user, obj)
        return context


class HomeView(CanEditMixin, generic.ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactsView(View):
    template_name = 'contacts.html'

    def get(self, request):
        return render(request, self.template_name, {'success_message': ''})

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print("Пользователь ввел:")
        print(f"Имя: {name}")
        print(f"Номер телефона: {phone}")
        print(f"Сообщение: {message}")

        success_message = 'Ваше сообщение успешно отправлено! Спасибо.'
        return render(request, self.template_name, {'success_message': success_message})


class ProductDetailView(CanEditMixin, generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, CanEditMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not self.user_can_edit(request.user, obj):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, CanEditMixin, generic.DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not self.user_can_edit(request.user, obj):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)