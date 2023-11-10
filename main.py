DNA = input("DNA: ")
mRNA = []
Amino_acid = []

for x in range(len(DNA)):
  if DNA[x] == "A":
    mRNA.append("U")
  elif DNA[x] == "T":
    mRNA.append("A")
  elif DNA[x] == "G":
    mRNA.append("C")
  elif DNA[x] == "C":
    mRNA.append("G")

for x in range(0, len(mRNA), 3):
  if mRNA[x] == "A":
    if mRNA[x + 1] == "A":
      if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
        Amino_acid.append("Lys")
      else:
        Amino_acid.append("Asn")
    elif mRNA[x + 1] == "U":
      if mRNA[x + 2] == "G":
        Amino_acid.append("Met")
      else:
        Amino_acid.append("Ile")
    elif mRNA[x + 1] == "C":
      Amino_acid.append("Thr")
    elif mRNA[x + 1] == "G":
      if mRNA[x + 2] == "G" or mRNA[x + 2] == "A":
        Amino_acid.append("Arg")
      else:
        Amino_acid.append("Ser")
  elif mRNA[x] == "U":
    if mRNA[x + 1] == "A":
      if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
        Amino_acid.append("Stop")
      else:
        Amino_acid.append("Tyr")
    elif mRNA[x + 1] == "U":
      if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
        Amino_acid.append("leu")
      else:
        Amino_acid.append("Phe")
    elif mRNA[x + 1] == "C":
      Amino_acid.append("Ser")
    elif mRNA[x + 1] == "G":
      if mRNA[x + 2] == "A":
        Amino_acid.append("Stop")
      elif mRNA[x + 2] == "U" or mRNA[x + 2] == "C":
        Amino_acid.append("Cys")
      else:
        Amino_acid.append("Trp")
  elif mRNA[x] == "C":
    if mRNA[x + 1] == "A":
      if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
        Amino_acid.append("Gln")
      else:
        Amino_acid.append("His")
    elif mRNA[x + 1] == "U":
      Amino_acid.append("leu")
    elif mRNA[x + 1] == "C":
      Amino_acid.append("Pro")
    elif mRNA[x + 1] == "G":
      Amino_acid.append("Arg")
  elif mRNA[x] == "G":
    if mRNA[x + 2] == "A":
      if mRNA[x + 2] == "A" or mRNA[x + 2] == "G":
        Amino_acid.append("Glu")
      else:
        Amino_acid.append("Asp")
    elif mRNA[x + 1] == "U":
      Amino_acid.append("Val")
    elif mRNA[x + 1] == "C":
      Amino_acid.append("Ala")
    elif mRNA[x + 1] == "G":
      Amino_acid.append("Gly")

print("mRNA: ", end="")
for x in range(0, len(mRNA), 3):
  print(mRNA[x], mRNA[x + 1], mRNA[x + 2], sep="", end="-")
print(" ")
print("Amino acid: ", end="")
for x in range(len(Amino_acid)):
  print(Amino_acid[x], end="-")