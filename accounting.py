def print_underpaid(order_file):
    """
    Intakes file with customer number, name, melon amount, amount paid.
    Compares expected amount paid to actual amount paid.
    Prints out customers who underpaid.
    """
    orders = open(order_file)
    melon_cost = 1.0

    for line in orders:
        line = line.rstrip()
        words = line.split('|')

        cust_num, cust_name, melon_ordered, amt_paid = words
        melon_ordered = float(melon_ordered)
        amt_paid = float(amt_paid)

        exp_paid = melon_ordered * melon_cost

        if exp_paid != amt_paid:
            print(cust_name, "paid {:.2f}, expected {:.2f}".format(
                amt_paid, exp_paid))

    orders.close()


print_underpaid("customer-orders.txt")
