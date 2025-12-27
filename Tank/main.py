from input_handler import input_handler
from output_handler import output_handler
from util.tank import Tank
from util.sort import *
from threading import *

def main():
	attribute = input_handler("data/input.txt")
	tanks = []
	good_purchases = []
	bad_purchases = []
	for i in range(len(attribute)):
		tanks.append(Tank(attribute[i], i+1))

	t1 = Thread(target=buy_many, args=(tanks, 75, good_purchases))
	t2 = Thread(target=buy_good, args=(tanks, 75, bad_purchases))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	output_handler(good_purchases, bad_purchases)

if __name__ == "__main__":
	main()