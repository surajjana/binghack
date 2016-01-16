import csv
from gensim import corpora, models, similarities

fv = []
corpus = []
i = 0
with open("train_data.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        fv.append(line[0:6])

while(i<=1):
	corpus.append(fv[i])
	i = i + 1

tpl0 = (0,)
tpl1 = (1,)
tpl2 = (2,)
tpl3 = (3,)
tpl4 = (4,)
tpl5 = (5,)



tpl0 += (fv[0][0],)
tpl1 += (fv[0][1],)
tpl2 += (fv[0][2],)
tpl3 += (fv[0][3],)
tpl4 += (fv[0][4],)
tpl5 += (fv[0][5],)

lst0 = []

lst0.append(tpl0)
lst0.append(tpl1)
lst0.append(tpl2)
lst0.append(tpl3)
lst0.append(tpl4)
lst0.append(tpl5)



print lst0
#tfidf = models.TfidfModel(corpus)
#print tfidf