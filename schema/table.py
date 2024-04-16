# table.py

class Table_Schema:
    def __init__(self, number=None, status=False, bill_id=""):
        self.number = number
        self.status = status
        self.bill_id = bill_id
    def __str__(self):
        return f"Table(number={self.number}, status={self.status}, bill_id='{self.bill_id}')"

    # You can add more methods here as needed
