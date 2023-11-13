string = ""
DNA = ""
DNA_list = []
mRNA = []
Amino_acid = []

def initialize():
  global string
  global DNA
  global DNA_list
  if len(DNA) != 0:
    DNA_list.append(DNA)
  string = str(input("DNA: "))

def string_to_DNA():
  global string
  global DNA
  for x in range(len(string)):
    if string[x] == "A":
      DNA += "A"
    elif string[x] == "T":
      DNA += "T"
    elif string[x] == "C":
      DNA += "C"
    elif string[x] == "G":
      DNA += "G"

def DNA_to_mRNA():
  global DNA
  global mRNA
  mRNA = []
  for x in range(len(DNA)):
    if DNA[x] == "A":
      mRNA.append("U")
    elif DNA[x] == "T":
      mRNA.append("A")
    elif DNA[x] == "G":
      mRNA.append("C")
    elif DNA[x] == "C":
      mRNA.append("G")

def mRNA_to_Amino_acid():
  global mRNA
  global Amino_acid
  Amino_acid = []
  for x in range(0, (len(mRNA) - (len(mRNA) % 3)), 3):
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
          Amino_acid.append("Leu")
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
        Amino_acid.append("Leu")
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

def print_mRNA():
  global mRNA
  print("mRNA: ", end="")
  for x in range(len(mRNA)):
    print(mRNA[x], sep="", end="")
    if x % 3 == 2 and x + 1 != len(mRNA):
      print("-", end="")

def print_Amino_acid():
  global Amino_acid
  print("\n", "Amino acid: ", sep="", end="")
  for x in range(len(Amino_acid)):
    print(Amino_acid[x], sep="", end="")
    if x + 1 != len(Amino_acid):
      print("-", end="")

  print("\n", "\n")

def action(thing_that_ate, action, thing_that_got_eaten):
  if thing_that_ate == 7 and action == "ate" and thing_that_got_eaten == 9:
    return True
while action(7, "ate", 9):

  initialize()
  string_to_DNA()
  DNA_to_mRNA()
  mRNA_to_Amino_acid()
  print_mRNA()
  print_Amino_acid()
  