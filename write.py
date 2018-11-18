#dosyaya yazma

iterator=0
words = [None] * 1000 ;

for c in content:
	words[iterator]= c.split(" ")[0]
	iterator = iterator+1

#words listesinde kelimeler mevcuttur.
for w in words:
	with open("kelimeler.txt", "a") as f:
		f.write(w + "\n")
