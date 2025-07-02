import datetime
from read_AakiPrajapati import read_from_file
from operations_AakiPrajapati import unique_date_time, restock_bill_items, restock_id, restock_again, restock_qty, variables, bill_items, date_time_tdy, final_total, buying_product_qty, buy_more, buying_product_id, buying_product_id, enter_user_details, initialize_variable, display_stock, input_choices, stock_display_choice1, buying_id_validation,purchase_product, update_stock_after_purchase, shipping, stock_display_choice2, restock_id_validation, restock_quantity_validation, stock_after_restock, restock_bill
from write_AakiPrajapati import invalid_choice, option_3, restock_bill_onscreen, purchase_bill_onscreen, display_free_items, bill_info, initial_shop_details, user_display, update_after_purchase, unique_bill, file_after_restock,  bill_after_restock

#Initial display statements
initial_shop_details()
#Reading from file
nl=read_from_file()
#Displaying stock after reading from file
display_stock(nl)

#Providing the user services according to the choice they choose
#Main loop
loop=True
while loop==True:
    user_display()
    #Taking choice as input from the user
    choices=input_choices()
    
    #Selected choice-1: Selling products to the customer 
    if choices==1:
        #displaying print statements
        bill_info()
        #asking user details
        name, phone_no=enter_user_details()
        #initializing variables
        selling_items, total, grand_total, shipping_cost, selling_loop= initialize_variable()

        while selling_loop==True: 
            stock_display_choice1(nl)

            #asking product id
            buying_id=buying_product_id(nl)
            
            #Taking the quantity required by the user
            product_quantity=buying_product_qty(nl)
            free_products, quantity_to_deduct, product_quantity=purchase_product(product_quantity,nl,buying_id)
            
            #Providing information to the customer regarding the Buy 3 Get 1 Free Policy
            display_free_items(name,free_products)
            
            #Updating the stock after purchase
            selling_items, total=update_stock_after_purchase(buying_id, product_quantity, free_products, quantity_to_deduct,selling_items, total, nl)
            #Asking the customer if they want to buy any more products
            selling_loop=buy_more()
        #Asking the customer if they want shipping to be done
        shipping_cost=shipping(shipping_cost)
        #Grand total
        grand_total=final_total(grand_total, total, shipping_cost)
        #Date and time
        date_and_time_tdy=date_time_tdy()
        #Updating the txt file
        update_after_purchase(nl)
        
        #Displaying the final bill on the screen
        purchase_bill_onscreen(name, phone_no, date_and_time_tdy)
        #accessing through the selling_items list where all the purchase information is stored
        bill_items(selling_items, shipping_cost, grand_total)

        #Saving the bill to a new .txt file with unique name
        unique_bill(name, phone_no, date_and_time_tdy, shipping_cost, grand_total, selling_items)

    #Selected choice-2: Restocking products from the manufacturer
    elif choices==2:
        purchase, total_of_all, purchase_loop= variables()
        while purchase_loop==True:
            stock_display_choice2(nl)
            
            #Asking the product ID from the user of the product they want to restock
            restock_product_id=restock_id(nl)
            
            #Taking quantity of required product from the user
            restock_product_qty=restock_qty(nl)
            
            #Updating the stock with new products(updating quantity)
            nl= stock_after_restock(restock_product_id, restock_product_qty,nl)


    
            #Updating the stock in file
            file_after_restock(nl)

            purchase, total_of_all=restock_bill(nl, restock_product_id, restock_product_qty, purchase, total_of_all)
            #Asking user if they want to restock again
            purchase_loop=restock_again()
        date_and_time_tdy=date_time_tdy()

        #Displaying restock bill on screen
        restock_bill_onscreen(date_and_time_tdy)
        #accessing through the purchase list where all the purchase information is stored
        restock_bill_items(total_of_all, purchase)

        #Generation of unique bill
        unique_num=unique_date_time()
        bill_after_restock(unique_num, total_of_all, purchase, date_and_time_tdy)

    elif choices==3:
        option_3()
        loop=False

    else:
       invalid_choice(choices)
                  
        
