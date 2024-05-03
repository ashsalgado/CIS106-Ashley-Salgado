class car:
  def __init__(self, model, make, sticker_price):
    self.model = model
    self.make = make
    self.sticker_price = sticker_price

  def discount_price(self):
    return self.sticker_price * 0.9

class sports(car):
  def __init__(self, model, make, sticker_price, sport_wheels="N", sport_engine="N", sport_interior="N"):

    super().__init__(model, make, sticker_price)
    self.sport_wheels = sport_wheels
    self.sport_engine = sport_engine
    self.sport_interior = sport_interior


  def sport_wheels_option(self):
    if self.sport_wheels == "Y":
      return 1000.00
    else:
      return 0.00

  def sport_engine_option(self):
    if self.sport_engine == "Y":
      return 3000.00
    else:
      return 0.00

  def sport_interior_option(self):
    if self.sport_interior == "Y":
      return 2000.00
    else:
      return 0.00

  def pricewithoptions(self):
    total_price = self.discount_price() + self.sport_wheels_option() + self.sport_engine_option() + self.sport_interior_option()
    return total_price

sport_car = sport("Nissan","GTR", 100000, sport_wheels="Y", sport_engine="Y", sport_interior="Y")

print(f"original sticker price: ${sport_car.sticker_price:.2f}")
print(sport_car.discount_price())
print(sport_car.pricewithoption())