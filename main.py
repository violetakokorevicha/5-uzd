saraksts = [int(sk) for sk in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]
for i in range(len(saraksts)+1):
   if saraksts[i] == saraksts[i + 1]:
     print(saraksts[i], saraksts[i + 1])