class Category:
	def __init__(self, name):
		self.class_name = name
		self.ledger = []
		self.balance = 0

	def deposit(self, amount, description=""):
		self.ledger.append({"amount":amount, "description":description})
		self.balance += amount


	def check_funds(self, amount):
		if amount > self.balance:
			return False

		return True

	def withdraw(self, amount, description=""):
		if self.check_funds(amount) == False:
			return False

		self.ledger.append({"amount":-amount, "description": description})
		self.balance -= amount

		return True

	def get_balance(self):
		return self.balance


	def transfer(self, amount, cls):
		check_fund = self.withdraw(amount, f"Transfer to {cls.class_name}")

		if check_fund == False:
			return False

		cls.deposit(amount, f"Transfer from {self.class_name}")
		return True

	def __repr__(self):
		output = []
		final_string = ""

		output.append("")

		border = (30-len(self.class_name))//2

		for i in range(border):
			output[0] += "*"

		output[0] += self.class_name

		for i in range(border):
			output[0] += "*"

		for i in range(len(self.ledger)):
			string = ""

			if len(self.ledger[i]["description"]) > 23:
				self.ledger[i]["description"] = self.ledger[i]["description"][0:23]

			string += self.ledger[i]['description']

			amount = self.ledger[i]["amount"]
			amount = float(amount)
			amount = "{:.2f}".format(amount)

			spaces = 30 - (len(self.ledger[i]["description"]) + len(amount))

			for i in range(spaces):
				string += " "

			string += amount
			output.append(string)

		output.append(f"Total: {self.balance}")

		for i in range(len(output)):
			if i != len(output)-1:
				final_string += output[i] + "\n"
			else:
				final_string += output[i]


		return final_string

def create_spend_chart(categories):
	pass


# Testing Code
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(10, "test")
clothing.withdraw(1, "hi")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)