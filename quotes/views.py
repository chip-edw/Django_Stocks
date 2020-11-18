from django.shortcuts import render, redirect
from django.contrib import messages
from quotes.forms import StockForm
from quotes.models import Stock
from stocks.settings import API_PK


def home(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=" + API_PK)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker':  "To get started, enter a ticker symbol in the Stock Quote search button in the Navbar above"})

    

def about(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_e27b7fa174b744c8b456f5e394b8a3a9")
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker':  "To get started, enter a ticker symbol in the Stock Quote search button in the Navbar above"})
    


def add_stock(request):
    import requests
    import json

    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been Added!"))
            return redirect('add_stock')
        
    else:
        ticker = Stock.objects.all()
        output_api =[]
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_e27b7fa174b744c8b456f5e394b8a3a9")
            try:
                api = json.loads(api_request.content)
                output_api.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'add_stock.html', {'ticker': ticker, 'output_api': output_api})



def delete_stock(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Deleted !"))
    return redirect(add_stock)