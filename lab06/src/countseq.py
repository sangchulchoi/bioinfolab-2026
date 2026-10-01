#!/usr/bin/env python3
# countseq.py — FASTA 파일의 서열 개수를 출력한다
# 사용법: python3 countseq.py <FASTA파일>
 
import sys
import os
 
if len(sys.argv) < 2:
    print("사용법: python3 countseq.py <FASTA파일>")
    sys.exit(1)
 
filename = sys.argv[1]

 
n = 0
with open(filename) as f:
    for line in f:
        if line.startswith(">"):
            n = n + 1
 
print(n)
