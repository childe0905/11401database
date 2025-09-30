from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leo930905",   
    database="food_order_system"
)

@app.route("/", methods=["GET", "POST"])
def index():
    cursor = db.cursor(dictionary=True)

    # 取得商品清單
    cursor.execute("SELECT * FROM menu")
    menu = cursor.fetchall()

    # 新增訂單
    if request.method == "POST":
        customer = request.form["customer"]
        item_id = int(request.form["item"])
        quantity = int(request.form["quantity"])

        # 查該商品資料
        cursor.execute("SELECT * FROM menu WHERE id = %s", (item_id,))
        product = cursor.fetchone()
        price = product["price"] * quantity

        cursor.execute(
            "INSERT INTO orders (customer, item, quantity, price) VALUES (%s, %s, %s, %s)",
            (customer, product["name"], quantity, price)
        )
        db.commit()
        return redirect("/")

    # 查詢訂單
    cursor.execute("SELECT * FROM orders ORDER BY created_at DESC")
    orders = cursor.fetchall()

    # 查總營收
    cursor.execute("SELECT SUM(price) AS total FROM orders")
    total = cursor.fetchone()["total"]

    return render_template("index.html", orders=orders, total=total, menu=menu)

# 刪除訂單
@app.route("/delete/<int:order_id>")
def delete(order_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
    db.commit()
    return redirect("/")

# 修改訂單
@app.route("/edit/<int:order_id>", methods=["GET", "POST"])
def edit(order_id):
    cursor = db.cursor(dictionary=True)

    # 取得商品清單
    cursor.execute("SELECT * FROM menu")
    menu = cursor.fetchall()

    if request.method == "POST":
        customer = request.form["customer"]
        item_id = int(request.form["item"])
        quantity = int(request.form["quantity"])

        cursor.execute("SELECT * FROM menu WHERE id = %s", (item_id,))
        product = cursor.fetchone()
        price = product["price"] * quantity

        cursor.execute(
            "UPDATE orders SET customer=%s, item=%s, quantity=%s, price=%s WHERE id=%s",
            (customer, product["name"], quantity, price, order_id)
        )
        db.commit()
        return redirect("/")

    cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
    order = cursor.fetchone()
    return render_template("edit.html", order=order, menu=menu)

if __name__ == "__main__":
    app.run(debug=True)