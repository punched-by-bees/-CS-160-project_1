
def format_fun():
  print("---------")

def main():
  print("Groccery Budget App")
  toggle = True
  format_fun()

  total_cost_of_all_products = float(input("budget = "))
  format_fun()


  while(toggle == True):
    by_weight = int(input("Enter 1 for weighed goods, enter 0 for non-weighed goods: "))
    format_fun
    if (by_weight == 1 ):
     format_fun
     cost_per_lb = float(input("Price per pound = "))
     format_fun
     total_weight_of_product = float(input("total weight of product = "))
     format_fun
     sales_tax_rate = float(input("Enter sales tax percentage or sale: "))

    elif(by_weight == 0 ):
     orig_cost_of_product = float(input("Enter cost of product: "))
     sales_tax_rate = float(input("Enter sales tax percentage or sale: "))
     # new_total_cost_of_all_products = float
     format_fun()

    # 12% = 12/100 = 0.12
    sales_tax_rate_conversion = sales_tax_rate/100
    total_cost_of_product = orig_cost_of_product + (sales_tax_rate_conversion * orig_cost_of_product)

    new_total_cost_of_all_products = total_cost_of_all_products - total_cost_of_product

    # print("Total Cost of Product = ", total_cost_of_product)
    print("Budget left =", new_total_cost_of_all_products)
  if(new_total_cost_of_all_products < 0):
   toggle = False
   print("Done shopping!")

format_fun()

main()

