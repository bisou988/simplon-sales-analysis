import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

# Total quantity sold by product
sales_by_product = données.groupby('produit')['qte'].sum().reset_index()

figure_products = px.bar(
    sales_by_product,
    x='produit',
    y='qte',
    color='produit',
    title='Total quantity sold by product'
)

figure_products.write_html('sales-by-product.html')

print('sales-by-product.html generated successfully!')

# Calculate revenue for each sale
données['revenue'] = données['prix'] * données['qte']

# Total revenue by product
revenue_by_product = données.groupby('produit')['revenue'].sum().reset_index()

figure_revenue = px.bar(
    revenue_by_product,
    x='produit',
    y='revenue',
    color='produit',
    title='Total revenue by product'
)

figure_revenue.write_html('revenue-by-product.html')

print('revenue-by-product.html generated successfully!')