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
  if a < -1 or a >= len(data) or b < -1 or b >= len(data):
    print("Access out of bounds:", a, b)
    break
  if a == -1:
    dataa = ord(sys.stdin.read(1))
  else:
    dataa = data[a]
  if b == -1:
    sys.stdout.write(chr(dataa & 255))
    sys.stdout.flush()
    jmp = True
  else:
    data[b] -= dataa
    jmp = data[b] <= 0
  if jmp:
    pc = c
  else:
    pc += 3

LABEL_ADDR = 218
LABEL_LEN = 70
LABEL_START = '<'

print("Global vars:", data[:32])
labels = {}
for i in range(LABEL_LEN):
  if data[LABEL_ADDR+i] != 0:
    labels[chr(ord(LABEL_START)+i)] = data[LABEL_ADDR+i]

print("Labels:", labels)
print("Stack:", data[labels["S"]:labels["S"]+256])
#print("Return stack:", data[labels["R"]:labels["R"]+256])