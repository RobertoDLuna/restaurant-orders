from collections import Counter


class TrackOrders:

    def __init__(self):
        self.array_orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.array_orders)

    def add_new_order(self, customer, order, day):
        self.array_orders.append({
            'customer': customer,
            'order': order,
            'day': day
        })
        return self.array_orders

    def get_most_ordered_dish_per_customer(self, customer):
        customers = []
        for orders in self.array_orders:
            if orders['customer'] == customer:
                customers.append(orders['order'])

        counter_orders = Counter(customers)

        the_most_commom = counter_orders.most_common()

        return the_most_commom

    def get_never_ordered_per_customer(self, customer):
        customer_list = []  # pedidos do cliente
        all_orders = []  # todos os pedidos

        for orders in self.array_orders:
            all_orders.append(orders['order'])

            if orders['customer'] == customer:
                customer_list.append(orders['order'])

        all_unique_orders = set(all_orders)
        customer_unique_orders = set(customer_list)

        # difference usado para retornar os pedidos que existem em
        # all_unique_orders mas não existem em custome_unique_orders
        # fonte:
        # https://www.pythontutorial.net/python-basics/python-set-difference/
        return all_unique_orders.difference(customer_unique_orders)

    def get_days_never_visited_per_customer(self, customer):
        customer_days = []
        all_days = []

        for orders in self.array_orders:
            all_days.append(orders['day'])

            if orders['customer'] == customer:
                customer_days.append[orders['day']]

        all_unique_days = set(all_days)
        customer_unique_days = set(customer_days)

        return all_unique_days.difference(customer_unique_days)

    def get_all_days(self):
        all_days = []
        for orders in self.array_orders:
            all_days.append(orders['day'])
        return all_days

    def get_busiest_day(self):
        all_days = self.get_all_days()
        all_unique_days = Counter(all_days)
        most_commom_day = all_unique_days.most_common()

        return most_commom_day[0][0]

    def get_least_busy_day(self):
        all_days = self.get_all_days()
        all_unique_days = Counter(all_days)
        most_commom_day = all_unique_days.most_common()

        # -1 pegando ultimo elemento da lista
        return most_commom_day[-1][0]
