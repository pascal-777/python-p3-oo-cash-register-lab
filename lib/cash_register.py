#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = []

  def add_item(self, item, cost, amount=1):
    self.total += (cost * amount)
    self.last_transaction = [item, cost, amount]
    i=0
    while i < amount:
      self.items.append(item)
      i += 1

  def apply_discount(self):
    if(self.discount == 0):
      print("There is no discount to apply.")
    else:
      self.total *= ((100-self.discount)/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= (self.last_transaction[1] * self.last_transaction[2])