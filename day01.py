WINDOW_SIZE = 3

with open('day01.txt', 'r') as input_file:
    measurements = list(map(lambda m: int(m), input_file.readlines()))

increments = 0

i = 0
while i < len(measurements):
    if i < WINDOW_SIZE:
        i += 1
        continue

    current_window_start = i - WINDOW_SIZE + 1
    current_window_end = i + 1

    previous_window = measurements[current_window_start - 1:current_window_end - 1]
    current_window = measurements[current_window_start:current_window_end]

    print(i, previous_window, sum(previous_window))
    print(i, current_window, sum(current_window))

    if sum(current_window) > sum(previous_window):
        increments += 1

    i += 1

print(increments)
