def create_product(request, productos):
  nombre = request.form.get('nombre')
  precio = request.form.get('precio')
  stock = request.form.get('stock')

  productos.append({
      'nombre': nombre,
      'precio': float(precio),
      'stock': int(stock)
  })
  
  return productos