from datetime import datetime
from neo_api_client import NeoAPI
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
import redis
import time
import datetime

redis_client = redis.Redis(host='localhost', port=6379, db=0)


CS = "dFZGrIDg8hEXkXkOfPfnVus8LDca"
CK = "N3Mt8S8yWurhevxOUC7L8HsQvdwa"

MOB_NO = "+917058287084"

PASSWORD = "RohanPawar@1"

MPIN = "369121"

#--------------------------------------------------------------------------

client = NeoAPI(consumer_key=CK, consumer_secret=CS, environment='prod',
                access_token=None, neo_fin_key=None)

resLogin = client.login(mobilenumber=MOB_NO,password=PASSWORD )
resSession = client.session_2fa(OTP=MPIN)

#--------------------------------------------------------------------------


# Constants
TOKEN = '3499'  # Token for Tata Steel
TRADING_SYMBOL = 'TATASTEEL'
EXCHANGE_SEGMENT = 'nse_cm'
PRODUCT = 'MIS'
ORDER_TYPE = 'MKT'
VALIDITY = 'DAY'
QUANTITY = '1'

#--------------------------------------------------------------------------



# Function to place order
def place_order(transaction_type, price=None):
    try:
        order = client.place_order(
            exchange_segment=EXCHANGE_SEGMENT,
            product=PRODUCT,
            price=str(price) if price else None,
            order_type=ORDER_TYPE,
            quantity=QUANTITY,
            validity=VALIDITY,
            trading_symbol=TRADING_SYMBOL,
            transaction_type=transaction_type,
            amo='NO',
            disclosed_quantity='0',
            market_protection='0',
            pf='N',
            trigger_price='0',
            tag=None
        )
        return order
    except Exception as e:
        print(f"Exception when calling OrderApi->place_order: {e}")
        return None


# Main trading logic
order_count = 0
pnl = 1  # Start with profit state


while order_count < 20:
    current_time = datetime.datetime.now().time()
    if current_time >= datetime.time(9, 0) and current_time <= datetime.time(15, 15):
        if pnl == 1:
            buy_order = place_order('B')
            if buy_order and buy_order.get('stat') == 'Ok':
                buying_price = float(redis_client.hget('stock_data', TOKEN))
                print(f"Bought at {buying_price}")
                order_count += 1
                
                while True:
                    ltp = float(redis_client.hget('stock_data', TOKEN))
                    if ltp >= buying_price * 1.001:
                        sell_order = place_order('S')
                        if sell_order and sell_order.get('stat') == 'Ok':
                            print(f"Sold at {ltp}, Profit!")
                            pnl = 1
                        break
                    elif ltp <= buying_price * 0.998:
                        sell_order = place_order('S')
                        if sell_order and sell_order.get('stat') == 'Ok':
                            print(f"Sold at {ltp}, Loss!")
                            pnl = 0
                        break
                    time.sleep(5)  # Check every 5 seconds

        elif pnl == 0:
            sell_order = place_order('S')
            if sell_order and sell_order.get('stat') == 'Ok':
                selling_price = float(redis_client.hget('stock_data', TOKEN))
                print(f"Sold at {selling_price}")
                order_count += 1
                
                while True:
                    ltp = float(redis_client.hget('stock_data', TOKEN))
                    if ltp <= selling_price * 0.999:
                        buy_order = place_order('B')
                        if buy_order and buy_order.get('stat') == 'Ok':
                            print(f"Bought at {ltp}, Loss!")
                            pnl = 1
                        break
                    elif ltp >= selling_price * 1.002:
                        buy_order = place_order('B')
                        if buy_order and buy_order.get('stat') == 'Ok':
                            print(f"Bought at {ltp}, Profit!")
                            pnl = 0
                        break
                    time.sleep(5)  # Check every 5 seconds
    else:
        print("Market is closed.")
        break

print("Order reached order_count.")

# if __name__ == '__main__':


#     #------------------------------- Running the strategies----------------------------


#     cur_time = datetime.datetime.now().strftime("%H:%M:%S")
#     entry_flag = False
#     order_response = {}
#     current_order_id = []

#     while (cur_time >= "09:30:00" and cur_time <="15:10:00"):
            
#             cur_time = datetime.datetime.now().strftime("%H:%M:%S")
            
#             if(entry_flag==False):

#                 # check if there is any signals (This  function will read the stock_action of all the stocks of "stock_id_list_main" lists stocks)

#                 picked_stock = stock_to_pick(stock_id_list_main)

#                 if(picked_stock!=0):
#                     current_balance = get_balance()
#                     #print(f"type : {type(picked_stock[0])} picked stock : {picked_stock[0]}")
#                     # time.sleep(10)
#                     current_price = get_current_stock_price_id(picked_stock[0])
                
#                     quantity = 1
                    

#                     #-------------------- Placing the order here ------------------------------
#                     stock_action = picked_stock[1]['action']
#                     order_response = place_order(picked_stock[0],stock_action,quantity)
                    

#                     if(order_response["status"] == "success"):
#                         entry_flag=True
#                         print(f"order placed")
#                         current_order_id = order_response["data"]["orderId"]

#                         if(stock_action=="sell"):
#                             target = current_price-current_price*0.0024
#                             stop_loss = current_price*1.0024
#                         else:
#                             target = current_price*1.0024
#                             stop_loss = current_price-current_price*0.0024
                        
#                         order_placed = True
#                         cur_time = datetime.datetime.now().strftime("%H:%M:%S")
                        
#                         while(order_placed and cur_time<="15:16:00"):
#                             current_price_now = get_current_stock_price_id(picked_stock[0])
#                             if(stock_action=="sell"):

#                                 if(current_price_now <=target):
#                                     square_off_all_orders()
#                                     print("Target Hit !")
#                                     order_placed = False
#                                     entry_flag = False
#                                 elif(current_price_now >=stop_loss):
#                                     square_off_all_orders()
#                                     print("Stop Loss Hit !")
#                                     order_placed = False
#                                     entry_flag = False
#                                 else:
#                                     time.sleep(0.5)
#                             else:
#                                 if(current_price_now >=target):
#                                     square_off_all_orders()
#                                     print("Target Hit !")
#                                     order_placed = False
#                                     entry_flag = False
#                                 elif(current_price_now <=stop_loss):
#                                     square_off_all_orders()
#                                     print("Stop Loss Hit !")
#                                     order_placed = False
#                                     entry_flag = False
#                                 else:
#                                     time.sleep(0.5)

#                     else:
#                         print(f"Failed in placing order, Remarks : {order_response} ")
#                         time.sleep(10)
#                 else:
#                     time.sleep(5)
            
#             else:
                
#                 current_positions = get_positions()
#                 if(len(current_positions["data"])==0):
#                     entry_flag==False
#                 else:
#                     time.sleep(5)
                
#                 #do something
                
            
            
            
#     if(cur_time>="15:16:00"):
#         print("......................Squaring off all positions.......................")
#         square_off_all_orders()
    
#     print("......................Todays trading session ends here :).......................")
#             #--------------------------------------------------------------
