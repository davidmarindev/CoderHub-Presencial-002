from flask import Flask, render_template, request, redirect, url_for, flash
import os, time
from modules.json_parser import load_data, save_data
from modules.product import create_product
from modules.sales import export, import_sales_mod

app = Flask(__name__)
IMPORT_PATH = 'data/imports'
EXPORTS_PATH = 'data/exports'


def current_time():
    """Get the current time in a formatted string."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/productos', methods=['GET'])
def products():
    return render_template('productos.html', productos=load_data('productos.json'))
  
@app.route('/productos/agregar', methods=['POST'])
def add_product():
  productos_load = load_data('productos.json')
  productos = create_product(request, productos_load)
  
  save_data('productos.json', productos)
  flash('Producto agregado exitosamente', 'success')
  return redirect(url_for('products'))

@app.route('/ventas', methods=['GET'])
def sales():
    return render_template('ventas.html', ventas=load_data('ventas.json'), 
                                          productos=load_data('productos.json'), 
                                          clientes=load_data('clientes.json'))

@app.route('/ventas/agregar', methods=['POST'])
def add_sale():
    producto = request.form.get('producto')
    cantidad = request.form.get('cantidad')
    cliente = request.form.get('cliente')
    
    ventas = load_data('ventas.json')
    ventas.append({
        'producto': producto,
        'cantidad': int(cantidad),
        'cliente': cliente
    })
    
    save_data('ventas.json', ventas)
    flash('Venta agregada exitosamente', 'success')
    return redirect(url_for('sales'))

@app.route('/clientes', methods=['GET'])
def clients():
    return render_template('clientes.html', clientes=load_data('clientes.json'))
  
@app.route('/clientes/agregar', methods=['POST'])
def add_client():
    nombre = request.form.get('nombre')
    email = request.form.get('email') 

    clientes = load_data('clientes.json')
    clientes.append({
        'nombre': nombre,
        'email': email
    })
    
    save_data('clientes.json', clientes)
    flash('Cliente agregado exitosamente', 'success')
    return redirect(url_for('clients'))
  
@app.route('/ventas/exportar', methods=['GET'])
def export_sales():
    ventas = load_data('ventas.json')
    export(EXPORTS_PATH, current_time(), ventas)
    
    flash('Ventas exportadas exitosamente a ventas.xlsx', 'success')
    return redirect(url_for('sales'))
  
@app.route('/ventas/importar', methods=['POST'])
def import_sales():
    if 'excel_file' not in request.files:
      flash('No se ha seleccionado ningún archivo', 'error')
      return redirect(url_for('sales'))
  
    file = request.files['excel_file']
    if file.filename == '':
        flash('No se ha seleccionado ningún archivo', 'error')
        return redirect(url_for('sales'))
    
    if not file.filename.endswith(('.xlsx', '.xls')):
        flash('El archivo debe ser un Excel (.xlsx, .xls)', 'error')
        return redirect(url_for('sales'))

    ventas = import_sales_mod(IMPORT_PATH, file)
    flash('Ventas importadas exitosamente', 'success')
    return redirect(url_for('sales'))

if __name__ == "__main__":
    app.secret_key = 'mysecretkey'

    app.run(debug=True, port=8000)