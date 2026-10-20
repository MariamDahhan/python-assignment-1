class TransactionRecord:

    def __init__(self, branch_id, date, customer_tier, items, revenue):
        self.branch_id = branch_id
        self.date = date
        self.customer_tier = customer_tier
        self.items = items
        self.revenue = revenue
    def __str__(self):
        return f"{self.branch_id} | {self.customer_tier} | ${self.revenue}"
class Branch:

    def __init__(self, branch_id, city):
        self.branch_id = branch_id
        self.city = city

    def __str__(self):
        return f"{self.branch_id} - {self.city}"