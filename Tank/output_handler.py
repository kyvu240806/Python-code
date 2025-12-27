def output_handler(good_purchases, bad_purchases):
	g = "["
	b = "["
	for i in range(len(good_purchases)):
		if i < len(good_purchases) - 1:
			g += str(good_purchases[i]) + ", "
		else:
			g += str(good_purchases[i]) + "]\n"
	for i in range (len(bad_purchases)):
		if i < len(bad_purchases) - 1:
			b += str(bad_purchases[i]) + ", "
		else:
			b += str(bad_purchases[i]) + "]"
	with open("data/output.txt", "w") as out:
		out.write(g)
		out.write(b)