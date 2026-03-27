#!/usr/bin/python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Cette ligne permet d'accéder aux colonnes par leur nom (ex: row['name'])
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT id, name, category, price FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT id, name, category, price FROM Products')
            
        rows = cursor.fetchall()
        # On convertit les objets Row en dictionnaires classiques
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    
    # 1. Sélection de la source
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        # Pour SQL, on peut passer l'ID directement à la requête pour plus d'efficacité
        products = read_sql(id_param)
        if id_param and not products:
             return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products)
    else:
        return render_template('product_display.html', error="Wrong source")

    # 2. Filtrage manuel pour JSON et CSV (si pas déjà fait en SQL)
    if id_param:
        try:
            target_id = int(id_param)
            products = [p for p in products if p['id'] == target_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
