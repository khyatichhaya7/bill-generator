import mysql.connector

def bill():
    id=int(input("Enter order_id : "))
    name=input("Enter product name : ")
    price=float(input("Enter the price : "))
    quantity=int(input("Enter the quantity : "))
    total=price*quantity

    # MySQL se connection
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="khyati814",
        database="ecommerceee"
    )

    cursor = con.cursor()

    sql="INSERT INTO productss(order_id,product_name,p_price,quantity,amount) VALUES(%s,%s,%s,%s,%s)"
    values=(id,name,price,quantity,total)
    cursor.execute(sql,values)
    con.commit()
    print("Data successfully inserted into productss table✅")



    # for notpad
    x=str(id) 
    y=".txt"
    z=x+y
    file=open(z,"w")     
    s=(f'id: {id} \n name : {name} \n price : {price} \n quantity : {quantity} \n total : {total}')
    file.write(s)
bill()  

