# from django.shortcuts import render, get_object_or_404
# from .models import Product
#
#
# def home(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', {'products': products})
#
#
# def contacts(request):
#     success_message = ''
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#
#         print("Пользователь ввел:")
#         print(f"Имя: {name}")
#         print(f"Номер телефона: {phone}")
#         print(f"Сообщение: {message}")
#         success_message = 'Ваше сообщение успешно отправлено! Спасибо.'
#
#     return render(request, 'contacts.html', {'success_message': success_message})
#
#
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'product_detail.html', {'product': product})


from django.views import View, generic
from django.shortcuts import get_object_or_404, render
from .models import Product


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

