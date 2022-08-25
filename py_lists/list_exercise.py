total = 0
count = 0
average = None

while True:
    inp = input('Enter number ')
    if inp == 'x':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count

print("Average", average)

# Done with list functions
int_list = []
while True:
    inp = input('Enter number ')
    if inp == 'x':
        break
    int_list.append(float(inp))
    average = sum(int_list) / len(int_list)

print("Average", average)
