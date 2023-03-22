#  File: Report.py
#  Description: Prints a data report in a specific format
#  Student's Name: Amber
#  Date Created: March 1, 2020
#  Date Last Modified: March 8, 2020

def main ():

    # input data
    companyName = "Lone Star Corporation"
    date = "March 5, 2020"
    cash = 7505.54
    acctsRec = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machAndEquip = 8329.99
    patents = 2000.00
    acctsPay = 93569.23
    stock = 88100.00
    totalAssets = (cash + acctsRec+ supplies + land + buildings + machAndEquip + patents)
    stockEquity = (acctsPay + stock)


    print ("")
    print (companyName.upper().center(80))
    print ("Balance Sheet".center(80))
    print (date.center(80))
    print (format("",'80s'))

    print (format(" ",'<42s'),"Liabilities and")
    print ("Assets",format("   Stockholders' Equity",'>59s')+format("",'12s'))
    print (format("_"*80))
    print ("")

    
    print (format("   Cash",'<28s'),format(cash,'>9.2f')+format("Liabilities:",'>17s')+format("",'<25'))
    print (format("   Accounts Receivable",'<28s'),format(acctsRec,'>9.2f'),format("      Accounts Payable",'>23s')+format("",'8s')+format(acctsPay,'>10.2f'))
    print (format("   Supplies",'<28s'),format(supplies,'>9.2f')+format("",'<42'))
    print (format("   Land",'<28s'),format(land,'>9.2f')+format("",'<42'))
    print (format("   Buildings",'<28s'),format(buildings,'>9.2f')+format("      Stockholders' Equity:",'>29s')+format("",'<13'))
    print (format("   Machines and Equipment",'<28s'),format(machAndEquip,'>9.2f'),format("          Capital Stock",'<30s'),format(stock,'10.2f'))
    print (format("   Patents",'<28s'),format(patents,'>9.2f')+format("",'<42'))
    print ("")

    print (format("Total Assets",'<28s'),format(totalAssets,"<10.2f",)+format("",'<4s')+format("Total Liabilities and",'<37s'))
    print (format("      Stockholders' Equity",'>66s')+format("",'<4s')+(format(stockEquity,'>10.2f')))






    
main ()
