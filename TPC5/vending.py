import re
import json

class LexicalAnalyzer:
    def __init__(self):
        self.tokens = [
            ('LISTAR', r'listar'),
            ('MOEDA', r'moeda\s+(\d+e)?(\d+c)?'),
            ('SELECIONAR', r'selecionar\s+(\d+)'),
            ('SAIR', r'sair')
        ]
        self.pattern = re.compile('|'.join('(?P<%s>%s)' % pair for pair in self.tokens))

    def analyze(self, command):
        matches = self.pattern.finditer(command)
        for match in matches:
            token_type = match.lastgroup
            value = match.group(token_type)
            if token_type == 'MOEDA':
                value = value.replace(' ', '')
            yield token_type, value

class VendingMachine:
    def __init__(self, products_file):
        self.products = self.load_products(products_file)
        self.balance = 0
        self.lexical_analyzer = LexicalAnalyzer()

    def load_products(self, file_path):
        with open(file_path, 'r') as file:
            products_data = json.load(file)

        products = {}
        for product in products_data:
            id = product['id']
            name = product['name']
            price = product['price']
            products[id] = {'name': name, 'price': price}

        return products

    def list_products(self):
        for id, product in self.products.items():
            print(f"ID: {id}, {product['name']}; {product['price']}")

    def add_coins(self, coins):
        euros, cents = 0, 0
        match_euro = re.search(r'(\d+)e', coins)
        match_cent = re.search(r'(\d+)c', coins)

        if match_euro:
            euros = int(match_euro.group(1))
        if match_cent:
            cents = int(match_cent.group(1))

        total_cents = euros * 100 + cents
        self.balance += total_cents

    def parse_coins(self, coins_str):
        euros, cents = 0, 0
        match = re.match(r'(\d+)e', coins_str)
        if match:
            euros = int(match.group(1))
        match = re.search(r'(\d+)c', coins_str)
        if match:
            cents = int(match.group(1))
        return euros * 100 + cents

    def select_product(self, product_id):
        product = self.products.get(product_id)
        if product:
            price = self.parse_coins(product['price'])
            if price <= self.balance:
                self.balance -= price
                print(f"Balance = {self.balance//100}e{self.balance%100:02d}c")
            else:
                print("Insufficient balance.")
        else:
            print("Product not found.")

    def return_change(self):
        if self.balance > 0:
            print(f"Change: {self.balance//100}e{self.balance%100}c")
            self.balance = 0

    def run(self):
        while True:
            command = input(">> ").strip().lower() 
            tokens = self.lexical_analyzer.analyze(command)
            found_valid_token = False
            for token_type, value in tokens:
                found_valid_token = True
                if token_type == 'LISTAR':
                    self.list_products()
                elif token_type == 'MOEDA':
                    self.add_coins(value)
                elif token_type == 'SELECIONAR':
                    numeric_value = ''.join(filter(str.isdigit, value))  
                    if numeric_value:
                        self.select_product(int(numeric_value))
                    else:
                        print("Invalid product ID.")
                elif token_type == 'SAIR':
                    self.return_change()
                    return
            if not found_valid_token:
                print("Comando inválido.")

if __name__ == "__main__":
    vending_machine = VendingMachine('products.json')
    vending_machine.run()
