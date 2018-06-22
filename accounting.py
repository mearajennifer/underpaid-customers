def print_melon_payment_status(order_file):
    """
    Intakes file with customer number, name, melon amount, amount paid.
    Compares expected amount paid to actual amount paid.
    Prints out customers who underpaid.
    """
    # open file set cost for melons
    orders = open(order_file)
    melon_cost = 1.0

    # iterate through each line in the file, strip, and split data into a list
    for line in orders:
        line = line.rstrip()
        words = line.split('|')

        # Unpack list into 4 variables, turn nums into floats
        cust_num, cust_name, melon_ordered, amt_paid = words
        melon_ordered = float(melon_ordered)
        amt_paid = float(amt_paid)
        cust_first_name = cust_name.split(" ")[0]

        # calculate expected payment
        exp_paid = melon_ordered * melon_cost

        # if expected payment doesn't equal amount paid, print notification
        if exp_paid > amt_paid:
            print("{} paid {:.2f}, expected {:.2f}".format(
                cust_name, amt_paid, exp_paid))
            print("{} has UNDERPAID for melons! Issue invoice\n".format(
                cust_first_name))
        elif exp_paid < amt_paid:
            print("{} paid {:.2f}, expected {:.2f}".format(
                cust_name, amt_paid, exp_paid))
            print("{} has OVERPAID for melons! Issue refund.\n".format(
                cust_first_name))

    # close the file after consumed
    orders.close()


# call function on the file
print_melon_payment_status("customer-orders.txt")
