import csv

fv = []
i = 0
with open("test1.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        fv.append(line[0:6])

print fv[0][2]