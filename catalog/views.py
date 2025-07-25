from django.views import View, generic
from django.shortcuts import render
from .models import Product

from .forms import ProductForm
from django.urls import reverse_lazy


class HomeView(generic.ListView):
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


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        return super().form_valid(form)


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = '/'