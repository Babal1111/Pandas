from django.shortcuts import render

def odd_even_checker(request):
    result = None
    number = None

    if request.method == "POST":
        number = request.POST.get('number')
        if number and number.isdigit():
            num = int(number)
            result = "Even" if num % 2 == 0 else "Odd"
        else:
            result = "Please enter a valid number"

    return render(request, 'home.html', {'result': result, 'number': number})
