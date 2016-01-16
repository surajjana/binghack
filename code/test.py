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

res_lst = []

for i in range(0, 4498):
	tpl0 = (0,)
	tpl1 = (1,)
	tpl2 = (2,)
	tpl3 = (3,)
	tpl4 = (4,)
	tpl5 = (5,)
	
	tpl0 += (fv[i][0],)
	tpl1 += (fv[i][1],)
	tpl2 += (fv[i][2],)
	tpl3 += (fv[i][3],)
	tpl4 += (fv[i][4],)
	tpl5 += (fv[i][5],)

	lst0 = []

	lst0.append(tpl0)
	lst0.append(tpl1)
	lst0.append(tpl2)
	lst0.append(tpl3)
	lst0.append(tpl4)
	lst0.append(tpl5)

	res_lst.append(lst0)



print res_lst
#tfidf = models.TfidfModel(corpus)
#print tfidf