import random as rd

n = 100

between = [0 for _ in range(n)]
unload = [0 for _ in range(n)]
arrive = [0 for _ in range(n)]
finish = [0 for _ in range(n)]
idle = [0 for _ in range(n)]
wait = [0 for _ in range(n)]
start = [0 for _ in range(n)]
habor = [0 for _ in range(n)]

between[0] = rd.uniform(15, 145)
unload[0] = rd.uniform(45, 90)

arrive[0] = between[0]
hart_time = unload[0]
max_har = unload[0]
wait_time = 0
max_wait = 0
idle_time = arrive[0]

finish[0] = arrive[0] + unload[0]

for i in range(1, n):
	between[i] = rd.uniform(15, 145)
	unload[i] = rd.uniform(45, 90)

	arrive[i] = arrive[i-1] + between[i]
	time_diff = arrive[i] - finish[i-1]

	if time_diff >= 0:
		idle[i] = time_diff
		wait[i] = 0
	else:
		wait[i] = -time_diff
		idle[i] = 0

	start[i] = arrive[i] + wait[i]
	finish[i] = start[i] + unload[i]
	habor[i] = wait[i] + unload[i]

	hart_time += habor[i]
	wait_time += wait[i]
	idle_time += idle[i]

	if habor[i] > max_har:
		max_har = habor[i]

	if wait[i] > max_wait:
		max_wait = wait[i]

hart_time = hart_time/n
wait_time = wait_time/n
idle_time = idle_time/finish[n-1]

print(hart_time)
print(max_har)
print(wait_time)
print(max_wait)
print(idle_time)
