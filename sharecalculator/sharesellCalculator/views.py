from django.shortcuts import render

# Create your views here.

def index(request):
 return render(request,'share_sell_form.html')



def sell_calculate(request):
        buy_price =int( request.GET["buy_price"])
        sell_price =int( request.GET["sell_price"])
        share_number = int(request.GET["share_number"])
        capital_gain = float(request.GET["capital_gain"])

        share_amount_buy = buy_price * share_number
        share_amount_sell = sell_price * share_number


        # if share_amount_buy <= 50000:
        #     broker_commission_buy = (0.40*share_amount_buy)/100
        
        # elif share_amount_buy >=50001 and share_amount_buy<= 500000:
        #     broker_commission_buy = (0.37*share_amount_buy)/100

        # elif share_amount_buy >=500001 and share_amount_buy<= 2000000:
        #     broker_commission_buy = (0.34*share_amount_buy)/100

        # elif share_amount_buy >=2000001 and share_amount_buy<= 10000000:
        #     broker_commission_buy = (0.3*share_amount_buy)/100

        # else:
        #     broker_commission_buy = (0.27*share_amount_buy)/100

        # sebon_commision_buy = (0.015* share_amount_buy)/100



        # sell commission calculate
        if share_amount_sell <= 50000:
            broker_commission_sell = (0.40*share_amount_sell)/100
        
        elif share_amount_sell >=50001 and share_amount_sell<= 500000:
            broker_commission_sell = (0.37*share_amount_sell)/100

        elif share_amount_sell >=500001 and share_amount_sell<= 2000000:
            broker_commission_sell = (0.34*share_amount_sell)/100

        elif share_amount_sell >=2000001 and share_amount_sell<= 10000000:
            broker_commission_sell = (0.3*share_amount_sell)/100

        else:
            broker_commission_sell = (0.27*share_amount_sell)/100

        sebon_commision_sell = (0.015* share_amount_sell)/100


        dp_fee = 25

        total_fee_sell =  broker_commission_sell+sebon_commision_sell+ dp_fee
        
        # share_buy_calculation = broker_commission_buy + share_amount_buy + sebon_commision_buy +dp_fee

        share_sell_calculation_BeforeCapitalGainTax= broker_commission_sell + share_amount_sell + sebon_commision_sell +dp_fee
        
        profit_loss = sell_price - buy_price

        if profit_loss > 0:
            capital_gain_amount=(capital_gain * profit_loss)/100
        elif profit_loss < 0:
            capital_gain_amount = 0
        else:
            capital_gain_amount = 0
        


        profit_loss_amount = profit_loss* share_number
       
        
        capital_gain_amount = (capital_gain*profit_loss* share_number)/100
        if capital_gain_amount > 0:
            capital_gain_amount= capital_gain_amount
        else:
            capital_gain_amount= 0

        receivable_amount = share_amount_sell - capital_gain_amount - total_fee_sell

        # cost_per_share = share_buy_calculation/share_number
    
        return render(request,'result_sell.html', 
        {
           "share_amount_sell":share_amount_sell,
           "broker_commission_sell":broker_commission_sell,
           "sebon_commision_sell":sebon_commision_sell,
           "dp_fee":dp_fee,
           "profit_loss_amount": profit_loss_amount,
           "capital_gain_amount":capital_gain_amount,
           "receivable_amount":receivable_amount

        })
        











        # def dict_lookup(request):
        #     #Creating a dictionary of items
        #     dic = ({"share_amount_sell":share_amount_sell,
        #     "broker_commission_sell":broker_commission_sell,
        #     "sebon_commision_sell":sebon_commision_sell,
        #     "dp_fee":dp_fee,
        #     "profit_loss":profit_loss,
        #     "capital_gain_amount":capital_gain_amount})
        #     dict = {'dict1': dic }

        
