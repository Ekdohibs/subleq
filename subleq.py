import sys

filename = sys.argv[1]
f = open(filename, "rb")
data = list(f.read())
f.close()
print(data)
pc = 0
while True:
  if pc < 0 or pc + 2 >= len(data):
    break
  a, b, c = data[pc], data[pc+1], data[pc+2]
  if a < 0 or a >= len(data) or b < 0 or b >= len(data):
    print("Access out of bounds:", a, b)
    break
  #print(pc, a, b, c, data[a], data[b])
  #if pc in [55, 100, 103, 106, 109, 112]:
  #  print("pc =", pc, "Z = ", data[32], "U =", data[36], "V =", data[37])
  #if pc == 100: print(data[a])
  #  print(a, b, data[a], data[b])
  #if a >= 124:
  #  print("READ", data[a], "AT", a)
  data[b] -= data[a]
  if b >= 124:
    print("WRITE", data[b], "AT", b)
  if data[b] <= 0:
    pc = c
  else:
    pc += 3
print(pc)