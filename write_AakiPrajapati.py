def initial_shop_details():
    """
    function: it is used to display the initial shop details
    """
    print("\n\t\t\t\t\tWeCare Wholesale")
    print("\t\t\t\t       Lazimpat, Kathmandu")
    print("\t\t\t  Contact:01-4000021  Email:wecare@gmail.com")
    print("_"*99)
    print("\n\tDear Customer, Welcome to WeCare Wholesale! Hope you have a wonderful time with us.")
    print("_"*99)

def user_display():
    """
    function: it is used to display available choices
    """
    print("_"*99)
    print("Dear Admin, please choose any one option from the choices below to carry out the operations.")
    print("_"*99)
    print("Please enter 1 to sell the products to the customer.")
    print("Please enter 2 to purchase products from the manufacturer.")
    print("Please enter 3 to exit from the system.")
    print("\n")
    print("_"*99)

def bill_info():
    """
    function: it is used to display a message to the user
    """
    print("_"*99)
    print("The Bill Generation requires you to enter some information below:")
    print("_"*99)

def display_free_items(name,free_products):
    """
    function: it is used to display the free items received by the user
    """
    print("Dear", name, "WeCare Wholesale has an ongoing offer of Buy 3 Get 1 Free in all of our products. You have received", free_products, "items as free items. Thank You for shopping with us!")

def update_after_purchase(nl):
    """
    parameter:the 2D list nl 
    function: it is used to update the stock in file
    """
    file=open("WeCare.txt","w")
    for i in range(len(nl)):
        for j in range(len(nl[i])):
            file.write(nl[i][j])
            if j!=len(nl[i])-1:         #only if j is not the last element
                file.write(",")         #separate each element by ,
        file.write("\n")                #new line after the end of a product
    file.close()
    
def purchase_bill_onscreen(name, phone_no, date_and_time_tdy):
    """
    parameter: the customer name, phone number and current date and time
    function: it is used to display the shop details, and customer details
    """
    
    print("\n\t\t\t\t\tWeCare Wholesale Bill")
    print("\t\t\t\t       Lazimpat, Kathmandu")
    print("\t\t\t  Contact:01-4000021  Email:wecare@gmail.com")
    print("_"*99)
    print("\n\t\t\t\t       CUSTOMER DETAILS")
    print("_"*99)
    print("Customer Name:",name,"\t\t\tCustomer Phone No:",phone_no)
    print("Purchase date and time:", str(date_and_time_tdy))
    print("_"*99)
    print("\n\t\t\t\t       PURCHASE DETAILS")
    print("_"*99)
    print("Item \t\t   Quantity\t Free Items\t Unit Price\t Total")
    print("_"*99)

def restock_bill_onscreen(date_and_time_tdy):
    """
    parameter: the current date and time
    function: it is used to display _ for suitable representation
    """
    print("_"*99)

    #Displaying the final restock bill on the screen
    """
    function: it is used to display the shop details and other bill details
    """
    print("\n\t\t\t\t\tPurchase Bill")
    print("\t\t\t\t       Newroad, Kathmandu")
    print("\t\t\t  Contact:01-4021342  Email:skincare_manufacturegmail.com")
    print("_"*99)
    print("\n\t\t\t\t       CUSTOMER DETAILS")
    print("_"*99)
    print("Shop Name: WeCare Wholesale","\t\t\tCustomer Phone No: 4000021")
    print("Purchase date and time:", str(date_and_time_tdy))
    print("_"*99)
    print("\n\t\t\t\t       PURCHASE DETAILS")
    print("_"*99)
    print("Item \t\t   Quantity\t    Unit Price\t Total")
    print("_"*99)
    
def unique_bill(name, phone_no, date_and_time_tdy, shipping_cost, grand_total, selling_items):
    """
    parameter: name, phone number, current date and time, shipping cost, total with shipping cost
                and selling_items list
    function: it is used to write bill details along with name, quantity, free items, unit price,
              total of each item, total of all items along with shipping cost
    """
    file=open(name+str(phone_no)+".txt","w")
    file.write("WeCare Wholesale Bill")
    file.write("\nLazimpat, Kathmandu")
    file.write("\nContact:01-4000021  Email:wecare@gmail.com\n")
    file.write("-"*100)
    file.write("\nCUSTOMER DETAILS\n")
    file.write("-"*100)
    file.write("\nCustomer Name:"+name)
    file.write("\nCustomer Phone No:"+phone_no)
    file.write("\nPurchase date and time:"+ str(date_and_time_tdy)+ "\n")
    file.write("-"*100)
    file.write("\nPURCHASE DETAILS\n")
    file.write("-"*100)
    file.write("\nItem\t\t Quantity\t Free Items\t Unit Price\t Total\n")
    file.write("-"*100)
    file.write("\n")
    #accessing through the selling_items list where all the purchase information is stored
    for a in selling_items:
        file.write(a[0]+"\t " +str(a[1])+ "\t\t  " +str(a[2])+ "\t\t" +"$"+str(a[3])+ "\t\t" +"$"+ str(a[4])+"\n")
    file.write("-"*100)
    file.write("\n")
    if shipping_cost>0:
        file.write("Shipping Cost: $"+str(shipping_cost))
    file.write("\nGrand Total: $"+str(grand_total))
    file.close()

def file_after_restock(nl):
    """
    parameter: 2D list containing product data
    function: it is used to open the .txt file in write mode, and update it
    """
    file=open("WeCare.txt","w")
    for i in range(len(nl)):
        file.write(nl[i][0]+","+nl[i][1]+","+nl[i][2]+","+nl[i][3]+","+nl[i][4])
        file.write("\n")
    file.close()

#Bill after restock
def bill_after_restock(unique_num, total_of_all, purchase, date_and_time_tdy):
    """
    parameter: unique date and time, total price of all products, purchase list
               and date and time today
    function: to display the bill details
    """
    file=open(unique_num+".txt","w")
    file.write("Purchase Bill")
    file.write("\nNewroad, Kathmandu")
    file.write("\nContact:01-4021342 Email:skincare_manufacturegmail.com\n")
    file.write("-"*100)
    file.write("\nCUSTOMER DETAILS\n")
    file.write("-"*100)
    file.write("\nShop Name: WeCare Wholesale")
    file.write("\nPhone No: 4000021")
    file.write("\nPurchase date and time:"+ str(date_and_time_tdy)+"\n")
    file.write("-"*100)
    file.write("\nPURCHASE DETAILS\n")
    file.write("-"*100)
    file.write("\nItem\t\t Quantity\t Unit Price\t Total\n")
    file.write("-"*100)
    file.write("\n")
    #accessing through the selling_items list where all the purchase information is stored
    for a in purchase:
        file.write(a[0]+"\t " +str(a[1])+ "\t\t" +"$"+str(a[2])+ "\t\t" +"$"+ str(a[3])+"\n")
    file.write("-"*100)
    file.write("\nGrand Total: $"+str(total_of_all))
    file.close()

def option_3():
    """
    function: it is used to display thankyou message
    """
    print("Thank You for choosing us. Have a great day!")

#Invalid choice
def invalid_choice(choices):
    """
    function: it is used to display sorry message
    """
    print("Sorry! The choice",choices,"does not exist. Please enter the correct choice.\n")
