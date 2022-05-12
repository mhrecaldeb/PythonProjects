total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
tupla = zip(total_sales, prod_cost)
#lista = list(tupla) # una vez que la convierto en lista se destruye?
print(tupla)
for sales, costs in tupla:
    profit = sales - costs
    print(f'Total profit: {profit}')
