
N = int(input())

if N == 1:
    print("1")
    quit()

layer = 1
max_num_in_layer = 1

while max_num_in_layer < N:
    max_num_in_layer += 6 * layer
    layer += 1

print(layer)
