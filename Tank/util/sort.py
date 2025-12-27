def strength_sort(tanks):
	size = len(tanks)
	for i in range(size-1):
		for j in range(size-i-1):
			if tanks[j].strength() > tanks[j+1].strength():
				temp = tanks[j]
				tanks[j] = tanks[j+1]
				tanks[j+1] = temp

def price_sort(tanks):
	tanks.sort()

def print_bad_purchase(tank):
	print(f"- Bought a tank for {tank.getP()}\n")

def print_good_purchase(tank):
	print(f"+ Bought a tank for {tank.getP()}\n")

def buy_many(tanks, budget, bad_purchases):
	price_sort(tanks)
	i = len(tanks) - 1
	while budget >= 0 and i >= 0:
		if tanks[i].getP() <= budget:
			print_bad_purchase(tanks[i])
			budget -= tanks[i].getP()
			bad_purchases.append(tanks[i].getTID())
		i -= 1

def buy_good(tanks, budget, good_purchases):
	strength_sort(tanks)
	i = len(tanks) - 1
	while i >= 0 and budget >= 0:
		if tanks[i].getP() <= budget:
			print_good_purchase(tanks[i])
			budget -= tanks[i].getP()
			good_purchases.append(tanks[i].getTID())
		i -= 1