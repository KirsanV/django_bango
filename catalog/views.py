from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    success_message = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print("Пользователь ввел:")
        print(f"Имя: {name}")
        print(f"Номер телефона: {phone}")
        print(f"Сообщение: {message}")
        success_message = 'Ваше сообщение успешно отправлено! Спасибо.'

    return render(request, 'contacts.html', {'success_message': success_message})
