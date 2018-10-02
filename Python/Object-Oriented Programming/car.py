class Car:

	def __init__(self, vmax, seat):
		self.vmax = vmax
		self.seat = seat
		self.passenger = passenger
		self.v = 0
		self.engine = "off"

	def entrance(self, amount ):
		if self.v == 0 and self.passenger + amount <= self.seat:
			self.passenger += amount

	def leave(self, amount):
		if self.v = 0 and amount <= self.passenger:
			self.passenger -= amount

	def start(self):
		if self.engine == "off" and self.passenger > 0 :
			self.engine = "on"

	def stop(self):
	if self.vmax = 0 and self.engine == "on" and self.passenger > 0:
		self.engine = "off"

	def acceleration(self, dv):
		if self.engine == "on" and self.v + dv < self.vmax:
			self.v += dv

	def brake(self, dv):
		if self.engine == "on" and self.v - dv >= 0:
			self.v -= dv

	def show(self):
		print("{0} km/h with {1} passenger".format(self.v, self.passenger))