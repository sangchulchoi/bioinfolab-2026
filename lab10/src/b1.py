from Bio import SeqIO
 
# 파일에 레코드가 여러 개일 때
for rec in SeqIO.parse("data/all.fasta", "fasta"):
    print(rec.id, len(rec.seq))
 
# 레코드가 하나뿐일 때
rec = SeqIO.read("data/rbcL_arabidopsis.gb", "genbank")

