import datetime
def display_stock(nl):
    """
    parameter: the 2D list containing data from .txt file
    function: it is used to display the initial stock
    """
    product_id=1                            #introducing product id as 1.
    print("_"*70)                           #prints underscore 70 times
    print("Id\tName\t\tBrand\t\tQty\tPrice\tOrigin")
    print("_"*70)
    for i in range(len(nl)):                #for lists in nl
        print(product_id,end="\t")          #printing the product id of each product
        for j in range(len(nl[i])):         #for elements of list in nl
            print(nl[i][j],end="\t")        #print each element present within lists which are present in nl with space between each element using end=\t since by default each component is printed a new line
        print()                             #change lines after each list ends
        product_id+=1
    print("_"*70)

#taking choices as input from user
def input_choices():
    """
    function: it is used ask the user's choice
    return: to return the choice entered by the user
    """
    choice_loop=False
    while choice_loop==False:
        try:
            choices=int(input("Please enter your choice to continue: "))
            print("\n")
            choice_loop=True
        except:
            print("Please enter a number!")
            choice_loop=False
    return choices

#CHOICE: 1
#asking name and phone number
def enter_user_details():
    """
    function: it is used to ask name and phone number, and restrict the phone number upto 10 digits
    return: to return the name and phone no entered by user
    """
    name=input("Please enter the name of the customer: ")
    phone_no=input("Please enter the phone number of the customer: ")
    #Validating phone number
    while len(phone_no)<10 or len(phone_no)>10:
        print("Phone Number must be 10 digits!")
        phone_no=input("Please enter the phone number of the customer: ")
    print("_"*99)
    print("\n")
    return name, phone_no

def initialize_variable():
    """
    function: it is used to initialize selling_items list, total, grand total, shipping cost and selling_loop
    return: to return the variables that were initialized
    """
    selling_items=[]        #A list to store the items purchased by the customer
    total=0                 #Total bill without shipping
    grand_total=0           #The total cost to be paid by the customer
    shipping_cost=0         #Shipping cost if the customer wants the products to be shipped
    selling_loop=True       #Selling loop to proceed the buying process
    return selling_items, total, grand_total, shipping_cost, selling_loop

def buying_product_id(nl):
    """
    parameter: the 2D list containing product data
    function: it is used to ask ID of product that the user wants to buy, and validate it
    return: to return the validated ID of the product
    """
    buying_loop=False
    while buying_loop==False:
        try:
            #Taking Product ID from the customer
            buying_id=int(input("Please enter the ID of the product you want to buy: "))
            #Validating the entered ID
            buying_id=buying_id_validation(buying_id, nl)
            buying_loop=True
        except:
            print("Please enter a number!")
            buying_loop=False
    return buying_id

def buying_product_qty(nl):
    """
    parameter: 2D list containing product data
    function: it is used to ask the quantity of products that the user wants to buy
    return: quantity of products that the user wants to buy
    """
    purchase_quantity_loop=False
    while purchase_quantity_loop==False:
        try:
            product_quantity=int(input("Please enter the quantity of the product you want to buy: "))
            purchase_quantity_loop=True
        except:
            print("Please enter a number!")
            purchase_quantity_loop=False
    return product_quantity

def purchase_product(product_quantity,nl,buying_id):
    """
    parameter: ID and product quantity entered by the user, 2D list containing product data
    function: it is used to calculate number of free items, quantity to deduct from the stock, to
              check if the product quantity entered by the user is valid, if not it asks the user
              to re-enter the product quantity
    return: number of free items to be received by the customer, total quantity to be deducted from
            stock and total quantity of products to be bought
    """
    free_products= product_quantity//3                  #Gives the quotient without decimal points\
    quantity_to_deduct= product_quantity+free_products  #Total number of products that should be deducted, including the free items

    #Getting the quantity of the product asked by the user
    qty_of_selected_product = nl[buying_id - 1][2]
    #The buying ID is subtracted by 1 because the product that the user is trying to get through id is actually stored at an index -1 than the id in the 2D list
   
    #Checking available stock- validating quantity 
    while product_quantity<=0 or quantity_to_deduct>int(qty_of_selected_product):
    #If the quantity entered by user is <=0 or if the total number of items including the
    #free items after the user has entered the product qty is more than the available stock
        print("Sorry! The quantity as entered is not available in our shop. We request you to kindly check the product table again, and enter the quantity")
        #Asking the user to enter the quantity and calculate the free products once again
        product_quantity=int(input("Please enter the quantity of the product you want to buy: "))
        free_products= product_quantity//3                  #Gives the quotient without decimal points
        quantity_to_deduct= product_quantity+free_products  #Total number of products that should be deducted, including the free items
        print("\n")
    return free_products, quantity_to_deduct, product_quantity
        
def buy_more():
    """
    function: it is used to ask the user if they want to purchase more items
    return: the boolean value of loop based off of user's decision
    """
    buy_more=input("Would you like to purchase more items? (Y/N): ").lower()
    if buy_more=="y" or buy_more=="yes":
        selling_loop=True
    else:
        selling_loop=False
    return selling_loop


def stock_display_choice1(nl):
    """
    parameter: the 2D list containing data from .txt file
    function: it is used to display the stock when choice 1 is entered (sp=cp*2)
    """
    #Displaying the stock available
    print("_"*70)                               #prints underscore 70 times
    print("Id\tName\t\tBrand\t\tQty\tPrice\tOrigin")
    print("_"*70)
    product_id=1                                #resetting product id to 1
    for i in range(len(nl)):                    #for lists in nl
        print(product_id,end="\t")              #printing the product id of each product
        for j in range(len(nl[i])):             #for elements of list in nl
            if j==3:
                print(int(nl[i][j])*2,end="\t") #the selling price is twice the cost price
            else:
                print(nl[i][j],end="\t")        #print each element present within lists which are present in nl with space between each element using end=\t since by default each component is printed a new line
        print()                                 #change lines after each list ends
        product_id+=1
    print("_"*70)

#Validate ID entered by user
def buying_id_validation(buying_id, nl):
    """
    parameter: ID of the product entered by the user, 2D list containing product data
    function: it is used to check if the entered product ID is valid, if not it asks
    the user to re-enter the product ID
    return: it returns the validated ID of product
    """
    #Checking if the product ID is valid
    while buying_id<=0 or buying_id>len(nl):  #Checking if the admin has entered an id less than 0 or greater than the available product ids
        print("Sorry! The ID you have entered is invalid. Please enter a valid ID!")

        #After the invalid ID message has been displayed, asking the admin to enter the ID once again
        buying_id=int(input("Please enter the ID of the product you want to buy: "))
    return buying_id
   
#Updating stock after purchase
def update_stock_after_purchase(buying_id, product_quantity, free_products, quantity_to_deduct,selling_items, total, nl):
    """
    parameter: ID, product quantity, total number of free products, total quantity to be deducted
               from stock, selling_items list, total price of items, 2D list nl
    function: it is used to update the previous stock by deducting the quantity bought and free items,
              to access the name, unit price of the products,
              to calculate the total price of each item
              to add values to the list and calculate total price of all products
    return: selling_items loop and total price of all products
    """
    nl[buying_id - 1][2]=str(int(nl[buying_id - 1][2])-quantity_to_deduct)
                #reducing the previous stock with the quantity to deduct

    #Bill Calculation
    product_name=nl[buying_id - 1][0]           #The name of the required product is stored in product_name
    unit_price=int(nl[buying_id - 1][3])*2      #The price per piece of the required product is stored in unit_price
    #selling price is twice the cost price
    total_price=unit_price*product_quantity     #total price of one product

    #Storage of the purchased items
    selling_items.append([product_name, product_quantity,free_products, unit_price, total_price])  #Storing all information in a list
    total=total+total_price                     #total price of all products chosen by customer
    return selling_items, total

def shipping(shipping_cost):
    """
    parameter: whether the user wants to ship or not, shipping cost
    function: it is used to add the shipping cost if the user wishes to have their products shipped
    return: to return the shipping cost
    """
    ship=input("Do you want the items to be shipped to your location? (Y/N): ").lower()
    if ship=="y" or ship=="yes":
            shipping_cost=500
    return shipping_cost

def final_total(grand_total, total, shipping_cost):
    """
    parameter: the grand total cost with shipping, total cost without shipping, shipping cost
    function: it is used to calculate the grand total price with shipping
    return: to return the grand total
    """
    grand_total=total+shipping_cost
    return grand_total

def date_time_tdy():
    """
    function:it is used to determine the current date and time
    return: to return the current date and time
    """
    date_and_time_tdy=datetime.datetime.now()
    return date_and_time_tdy

def bill_items(selling_items, shipping_cost, grand_total):
    """
    parameter: the selling_items list, shipping cost, and grand total cost with shipping 
    function: to display the item details
    """
    for a in selling_items:
        print(a[0]+"\t\t" +str(a[1])+ "\t   " +str(a[2])+ "\t\t  " +"$"+str(a[3])+ "\t\t" +"$"+ str(a[4]))
    print("_"*99)
    if shipping_cost>0:
        print("Shipping Cost: $"+str(shipping_cost))
    print("Grand Total: $"+str(grand_total))
    print("\n")
    
#CHOICE: 2
#Displaying available stock

def variables():
    """
    function: it is used to initialize purchase loop, total_of_all, and purchase_loop
    return: to return the variables that have been initialized
    """
    purchase=[]             #initializing before loop to add multiple products in a single bill
    total_of_all=0
    purchase_loop=True
    return purchase, total_of_all, purchase_loop

def restock_id(nl):
    """
    parameter: 2D list containing product details
    function: it is used to ask the user to enter the ID of product to be restocked and validate it
    return: to return the validated ID of the product
    """
    restock_loop=False
    while restock_loop==False:
        try:
            restock_product_id=int(input("Please enter the ID of the product you want to restock: "))
            #Validating the product ID
            restock_product_id=restock_id_validation(restock_product_id,nl)
            restock_loop=True
        except:
            print("Please enter a number!")
            restock_loop=False
    return restock_product_id

def restock_qty(nl):
    """
    parameter: 2D list containing product details
    function: it is used to ask the user to enter the quantity of product to be restocked and
              validate it
    return: to return the quantity of the product to be restocked
    """
    restock_quantity_loop=False
    while restock_quantity_loop==False:
        try:
            restock_product_qty=int(input("Please enter the quantity of the product you want to restock: "))
            #Validating the quantity of the product to be restocked
            restock_product_qty=restock_quantity_validation(restock_product_qty)
            restock_quantity_loop=True
        except:
            print("Please enter a number!")
            restock_quantity_loop=False
    return restock_product_qty

def restock_again():
    """
    function: it is used to ask if the user wants to restock more items
    return: to return the boolean value of purchase_loop based off of the user's answer
    """
    print("\nThe stock has successfully been updated!")
    #Asking the user if they want to restock any more products
    restock_more=input("Would you like to restock more items? (Y/N): ").lower()
    if restock_more=="y" or restock_more=="yes":
        purchase_loop=True
    else:
        purchase_loop=False
    return purchase_loop

def restock_bill_items(total_of_all, purchase):
    """
    parameter: the total price of all items, and purchase list
    function: it is used to display item details
    """
    #accessing through the purchase list where all the purchase information is stored
    for a in purchase:
        print(a[0]+"\t\t" +str(a[1])+ "\t\t" +"$"+str(a[2])+ "\t" +"$"+ str(a[3]))
    print("_"*99)
    print("Grand Total: $"+str(total_of_all))
    print("\n")

def unique_date_time():
    """
    function: it is used to concatenate the year, month, day, hour, minute and second to create a unique number
    return: to the unique_num which is the current date and time
    """
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    hour=str(datetime.datetime.now().hour)
    minute=str(datetime.datetime.now().minute)
    second=str(datetime.datetime.now().second)
    unique_num=year+month+day+hour+minute+second
    return unique_num
        
def stock_display_choice2(nl):
    """
    parameter: the 2D list containing data from .txt file
    function: it is used to display the initial stock
    """
    product_id=1
    print("_"*99)
    print("The following operations will be for restocking products")
    print("The available stock is displayed below:")
    print("_"*70)                               #prints underscore 70 times
    print("Id\tName\t\tBrand\t\tQty\tPrice\tOrigin")
    print("_"*70)
    for i in range(len(nl)):                    #for lists in nl
        print(product_id,end="\t")              #printing the product id of each product
        for j in range(len(nl[i])):             #for elements of list in nl
            print(nl[i][j],end="\t")            #print each element present within lists which are present in nl with space between each element using end=\t since by default each component is printed a new line
        print()                                 #change lines after each list ends
        product_id+=1
    print("_"*70)

#Validating ID of the product to be restocked
def restock_id_validation(restock_product_id,nl):
    """
    parameter: ID of the product entered by the user, 2D list containing product data
    function: it is used to check if the entered product ID is valid, if not it asks
    the user to re-enter the product ID to be restocked
    return: it returns the validated ID of product
    """
    while restock_product_id<=0 or restock_product_id>len(nl):
        print("Sorry! Invalid product ID! Please enter the correct product ID\n")
        #Asking the valid product ID from the user of the product they want to restock
        restock_product_id=int(input("Please enter the ID of the product you want to restock: "))
    return restock_product_id

#Validating quantity of the product to be restocked
def restock_quantity_validation(restock_product_qty):
    """
    parameter: quantity of the product entered by the user
    function: it is used to check if the entered product quantity is valid, if not it asks
    the user to re-enter the product quantity
    return: it returns the validated quantity of product
    """
    while restock_product_qty<=0:
        print("Sorry! You must restock atleast 1 item")
        restock_product_qty=int(input("Please enter the quantity of the product you want to restock: "))
    return restock_product_qty

#Updating stock after restocking
def stock_after_restock(restock_product_id, restock_product_qty,nl):
    """
    parameter: ID of the product entered by the user, quantity to be restocked
               2D list containing product data
    function: it is used to update the stock by adding quantity to be restocked
    return: it returns the updated 2D list nl
    """
    nl[restock_product_id-1][2]= str(int(nl[restock_product_id-1][2])+ restock_product_qty)
    return nl


#Bill generation in screen:
def restock_bill(nl, restock_product_id, restock_product_qty, purchase, total_of_all):
    """
    parameter: 2D list nl, ID and quantity of product to be restocked, purchase list, total price of all items
    function: it is used to calculate total price of each item
              to add product name, quantity, unit price and total of each item to the list and 
              to calculate total price of all items
    return: it returns the purchase list and total price of all items
    """
    restock_product_name=nl[restock_product_id - 1][0]   #The name of the required product is stored in restock_product_name
    restock_unit_price=int(nl[restock_product_id- 1][3])
    total_price=restock_product_qty*restock_unit_price
    purchase.append([restock_product_name, restock_product_qty, restock_unit_price, total_price])
    total_of_all=total_of_all+ total_price
    return purchase, total_of_all



