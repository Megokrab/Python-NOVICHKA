data = []
print("Твой блокнот")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break
bloknot = '\n'.join(data)
print("\n")
print("Это все нужно сделать сегодня")
with open("Bloknot.txt", "w") as f:
    for word in bloknot:
        f.write(word)