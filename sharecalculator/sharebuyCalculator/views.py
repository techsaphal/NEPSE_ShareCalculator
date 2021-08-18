from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'share_buy_form.html')


def buy_calculate(request):
    buy_price =int( request.GET["buy_price"])
    share_number = int(request.GET["share_number"])

    share_amount = buy_price * share_number

    if share_amount <= 50000:
        broker_commission = (0.40*share_amount)/100
    
    elif share_amount >=50001 and share_amount<= 500000:
        broker_commission = (0.37*share_amount)/100

    elif share_amount >=500001 and share_amount<= 2000000:
        broker_commission = (0.34*share_amount)/100

    elif share_amount >=2000001 and share_amount<= 10000000:
        broker_commission = (0.3*share_amount)/100


    else:
        broker_commission = (0.27*share_amount)/100

    
    sebon_commision = (0.015* share_amount)/100
    dp_fee = 25

    
    share_buy_calculation = broker_commission + share_amount + sebon_commision +dp_fee

    cost_per_share = share_buy_calculation/share_number
   
    return render(request,'result.html',
    { "share_amount":share_amount,"broker_commission":broker_commission,
    "sebon_commision":sebon_commision,"share_buy_calculation":share_buy_calculation,
    "dp_fee":dp_fee,"cost_per_share":cost_per_share })