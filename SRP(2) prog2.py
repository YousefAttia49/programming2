class Order:
    def __init__(self, items, customer_email):
        self.items = items
        self.customer_email = customer_email

    def is_valid(self):
        return bool(self.items)


class Validator:
    def validate(self, order):
        if not order.is_valid():
            raise Exception('No valid order found')


class InventoryUpdater:
    def update_inventory(self, order, inventory):
        for item in order.items:
            inventory.update(item)


class Notifier:
    def send_notification(self, message, recipient):
        print(f'Order for {recipient} and {message}')


class OrderProcessor:
    def __init__(self, order, inventory, validator, updater, notifier):
        self.order = order
        self.inventory = inventory
        self.validator = validator
        self.updater = updater
        self.notifier = notifier

    def process_order(self):
        self.validator.validate(self.order)
        self.updater.update_inventory(self.order, self.inventory)
        self.notifier.send_notification("Order processed", self.order.customer_email)
        print('Order has been processed successfully')






