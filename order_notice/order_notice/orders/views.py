from django.shortcuts import render
from django.utils import timezone

def order_notice(request):
    context = {
        'person_name': 'John Doe',
        'company': 'XYZ Corp',
        'ship_date': timezone.now(),
        'item_list': ['Lenovo Laptop ', 'Samsung 15 TV', 'LG Refrigerator'],
        'ordered_warranty': True,
    }
    return render(request, 'orders/order_notice.html', context)

