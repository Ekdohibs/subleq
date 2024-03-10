import sys

filename = sys.argv[1]
f = open(filename, "rb")
data = list(f.read())
f.close()
pc = 0
while True:
  if pc < 0 or pc + 2 >= len(data):
    break
  a, b, c = data[pc], data[pc+1], data[pc+2]
  if a < 0 or a >= len(data) or b < 0 or b >= len(data):
    print("Access out of bounds:", a, b)
    break
  data[b] -= data[a]
  if data[b] <= 0:
    pc = c
  else:
    pc += 3
print(pc)