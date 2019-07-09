from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
     "my_list": [
     {
       "restaurant_name": "Anar",
       "food_type": "Persian",

     },
     {
       "restaurant_name": "Lorenzo",
       "food_type": "Italian",
     },
     {
       "restaurant_name": "Early Bird",
       "food_type": "American",
     },
     ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {"restaurant_name":"Anar", "food_type":"Persian"}

    }
    return render(request, 'detail.html', context)
