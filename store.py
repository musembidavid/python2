
Product ={'Small' : 14.99, 'Medium' : 27.99, 'Large': 39.99}
Delivery = {'Land' : [15.00,0.25], 'Air' : [30.00, 1.00], 'Nextday': [48.00,1.50]}



def checkinput(choice):
    print("how many small jars do you want")
    try:
        var1 = float(input())
    except ValueError:
        print('no value entered')
      
    print("how many medium jars do you want")
    try:
        var2 = float(input())
    except ValueError:
        print('no value entered')
    print('how many large jars  do you want')
    try:
        var3 = float(input())
    except ValueError:
        print('no value entered')
  
    


def deliv():
    print('what delivery option?')
    print("by land is" + str(Delivery['Land']))
    print("by Air is" + str(Delivery['Air']))
    print("Nextday is" + str(Delivery['Nextday']))
   
  
    print(Product['Small']*var1 + Product['Medium']*var2 + Product['Large']*var3  )

    
def main():
    choice = input().lower()
    checkinput(choice)
    
    
  

main()
#plz don't touch anything