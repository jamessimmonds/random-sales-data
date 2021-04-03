import datetime
import json
import random

def read_config(filename):

    with open(filename, 'r') as config_file:
        config_data = json.load(config_file)
        return config_data

def initialiseProducts(number, minPrice, maxPrice):

    products = []

    for product in range(0, number):

        product_id = product
        price = random.randrange(minPrice, maxPrice)
        products.append((product_id, price))

    return products

def randomDate(startYear, startMonth, startDay, endYear, endMonth, endDay):

    if startYear == endYear:
        year = startYear
    else:
        year = random.randrange(startYear, endYear)

    month = random.randrange(startMonth, endMonth)
    day = random.randrange(startDay, endDay)

    return datetime.datetime(year, month, day)

def randomHex():

    randomInt = lambda: random.randrange(0, 255)
    return '{0:x}{1:x}{2:x}{3:x}{4:x}{5:x}{6:x}{7:x}{8:x}{9:x}{10:x}'.format(
        randomInt(), randomInt(), randomInt(), randomInt(), randomInt(), randomInt(), randomInt(), randomInt(), randomInt(), randomInt(), randomInt())

def main():

    CONFIG_FN = 'config.json'

    config_data = read_config(CONFIG_FN)

    sales_orders = [("document_id", "order_id", "order_date", "customer_id", "product_id", "qty", "price", "net_total", "vat", "gross_total")]
    sales_invoices = [("document_id", "sale_date", "order_id")]
    sales_deliveries = [("document_id", "delivery_date", "order_id", "invoice_id")]
    sales_receipts = [("document_id", "receipt_date", "customer_id", "amount", "order_id", "invoice_id")]

    number_of_orders = random.randrange(config_data['minOrders'], config_data['maxOrders'])

    products = initialiseProducts(config_data['numberOfProducts'], config_data['minPrice'], config_data['maxPrice'])

    for order in range(0, number_of_orders):

        # Generate order

        customer_id = random.randrange(0, config_data['numberOfCustomers'])
        
        order_date = randomDate(
            config_data['startDateYear'],
            config_data['startDateMonth'],
            config_data['startDateDay'],
            config_data['endDateYear'],
            config_data['endDateMonth'],
            config_data['endDateDay'])

        formatted_order_date = '{0}-{1}-{2}'.format(order_date.year, order_date.month, order_date.day)

        number_of_lines = random.randrange(config_data['minLinesPerOrder'], config_data['maxLinesPerOrder'])
        
        order_id = randomHex();

        # Generate each line of order

        order_total_net = 0
        order_total_vat = 0
        order_total_gross = 0
        
        for line in range(0, number_of_lines):
                
                order_line_id = randomHex()

                product_id, price = random.choice(products)
                qty = random.randrange(config_data['minQtyPerLine'], config_data['maxQtyPerLine'])

                net_total = qty * price
                vat = net_total * config_data['VATRate']
                gross_total = net_total + vat

                sales_orders.append(
                    (
                        order_line_id,
                        order_id,
                        formatted_order_date,
                        customer_id,
                        product_id,
                        qty,
                        price,
                        net_total,
                        vat,
                        gross_total
                    )
                )

    print(sales_orders)

if __name__ == '__main__':

    main()

