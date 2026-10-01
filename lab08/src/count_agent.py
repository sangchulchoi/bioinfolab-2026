#!/usr/bin/env python3
# count_agent.py — FASTA 파일의 서열 개수를 출력한다
# 사용법: python3 count_agent.py <FASTA파일>

import sys
import os

# lab07/src/fasta.py 의 read_fasta 를 쓰기 위해 경로를 추가한다
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lab07", "src"))
from fasta import read_fasta

if len(sys.argv) < 2:
    print("사용법: python3 count_agent.py <FASTA파일>")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    print(f"오류: 파일을 찾을 수 없습니다: {filename}")
    sys.exit(1)

seqs = read_fasta(filename)
print(len(seqs))
