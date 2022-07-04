import mysql.connector
from fpdf import FPDF
import random
import datetime


mydb  = mysql.connector.connect(host='localhost', user='root', password='', database='DB1')
cur = mydb.cursor()

def showbook():
    query = "SELECT * from bookList"
    cur.execute(query)
    result = cur.fetchall()
    for rec in result:
        print("\nbook id : "+ str(rec[0]) + "\nbook name : "+ str(rec[1]) + "\nbook quantity : "+ str(rec[2]) + "\nbook price : " + str(rec[3]))

def billGenerator(bookname, quantity, price, uname):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)

    dateandtime = datetime.datetime.now()
    pdf.cell(200, 10, txt = str(dateandtime),
            ln = 2, align = 'R')
 
    pdf.cell(200, 10, txt = " ",
            ln = 2, align = 'L')

    pdf.cell(200, 10, txt = "............BOOK STORE............",
         ln = 1, align = 'C')

    pdf.cell(200, 10, txt = " ",
            ln = 2, align = 'L')
  
    pdf.cell(200, 10, txt = "\n\nThanks For Buying Books From Our Store\n\n\n",
            ln = 2, align = 'C')
    
    pdf.cell(200, 10, txt = " ",
            ln = 2, align = 'L')
    pdf.cell(200, 10, txt = " ",
            ln = 2, align = 'L')
    pdf.cell(200, 10, txt = " ",
            ln = 2, align = 'L')

    pdf.cell(200, 10, txt = "Customer Name : "+uname.capitalize(),
            ln = 2, align = 'L')
    
    pdf.cell(200, 10, txt = " ",
            ln = 2, align = 'L')

    pdf.cell(200, 10, txt = "Book Name : "+bookname.capitalize(),
            ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "Price : "+str(price),
            ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "Quantity : "+quantity.capitalize(),
            ln = 2, align = 'L')

    randomnum = random.randint(1000,100000)
    filename = uname+str(randomnum)+".pdf"

    pdf.output(filename) 

def buybook(bookname, price, quantity, tquantity, id, uname):
    tquantity = tquantity-int(quantity)
    userInput = input(str("\n\n# You select "+ str(bookname) +" book for buy \n  Total price is : " + str(price) + "\n  Quantity : "+ str(quantity) +"\n  Please conform your order or buy(y/n) : "))
    if(userInput=='y'):
        query2 = "UPDATE bookList SET totalquantity = {} WHERE id = {}".format(tquantity, id)
        query1 = "INSERT INTO books  (bname, bprice ,bquantity) VALUES (%s,%s,%s)"
        b1 = (bookname, price, quantity)
        cur.execute(query1, b1)
        mydb.commit()
        cur.execute(query2)
        mydb.commit()
        billGenerator(bookname, quantity, price, uname)
        print("\n\n  Thanks for buying books...!\n\n")
        print("  Your bill is generated please check it...!\n\n")
    else:
        print("\nOK...! Try again")

def main():
    loop = 'y'
    condition = 0
    username = input(str("Enter your name : "))
    while(loop == 'y'):
        print("...............Welcome to book store............\n")
        print("...........books...........")
        showbook()
        print("............................")
        userinput = input(str("Select book to buy : "))
        query = "SELECT * from bookList"
        cur.execute(query)
        result = cur.fetchall()
        for data in result:
            if(data[1]==userinput):
                quantity = input(str("How many book do you buy ? : "))
                condition = 1
                if(int(quantity)<=data[2]):
                    price  = data[3] * int(quantity)
                    buybook(data[1], price, quantity, data[2], data[0], username)
                    break
                else:
                    print("\nQuantity is not Available try again\n\n")

        if(condition==0):
            condition = 0
            print("\nBook is not listed try again\n\n")
        

main()