import time

# 1
start_time = time.time()
i = 0
while time.time() - start_time < 1:
    i += 1
print(i)

# 2
for_start_time = time.time()
k = 0
for _ in range(i):
    k += 1
for_time = time.time() - for_start_time
print(for_time)

# 3
if for_time < 1:
    print("For is faster. It takes {}s".format(for_time))
else:
    print("For is slower. It takes {}s".format(for_time))

# 4 test
assert for_time > 1, "For is faster. It takes {}s".format(for_time)
