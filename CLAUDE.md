# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 이 저장소의 규칙

## 이 저장소는
생물정보학실험 수업의 실습 저장소이다. 주차별로 labNN 폴더가 있다.
빌드·테스트·린트 설정은 없다. 스크립트를 직접 실행해서 확인한다.

## 폴더 구조
- 새 주차 폴더는 `lab-template` 을 복사해서 만든다 (data/doc/src + .gitkeep).
  - `data`: 내려받거나 만든 데이터, `doc`: 보고서·결과·그림, `src`: 직접 쓴 .sh/.py
- `resources/` 는 실습용 예제 데이터(seqs.fasta 등)와 스크립트 원본이다.
- 스크립트는 lab 폴더 안에서 상대 경로로 실행한다.
  예) `cd lab07 && python3 src/countseq.py data/seqs.fasta`
  - `src/check_codespace.sh` 는 결과를 상대 경로 `doc/check_result.txt` 에 쓰므로
    반드시 lab 폴더에서 `bash src/check_codespace.sh` 로 실행한다.

## 실행 환경
- Codespaces 설정이 `.devcontainer/1-basic ~ 4-genome` 에 있고 주차마다 다른 것을 쓴다.
  - 02~07: python3 뿐 / 08~09, 12~14: seqkit, blastn, mafft, iqtree, fastqc, fastp
  - 10~11: 위 + shovill, prokka
- 필요한 도구가 없으면 설치하지 말고 알린다 (conda 실습 주차만 예외).
- `*.fastq`, `*.fq.gz`, `*.sra`, 조립/주석 결과 폴더, FastQC 보고서는 `.gitignore`
  대상이다. 저장소에 넣지 않고 필요할 때 wget 으로 다시 받는다.

## 코드를 쓸 때
- FASTA 파일은 lab07/src/fasta.py 의 read_fasta 로 읽는다.
  (`from fasta import read_fasta` 는 fasta.py 가 같은 폴더에 있어야 동작한다.
  다른 lab 에서는 스크립트 위치 기준으로 `../../lab07/src` 를 `sys.path` 에 추가한다.)
- 새 라이브러리(Biopython 등)를 쓰기 전에 먼저 물어본다.
- 주석은 한국어로 쓴다.
- 수강생이 읽는 코드이므로 기존 스크립트처럼 단순하게 쓴다:
  맨 위에 파일 설명·사용법 주석, `sys.argv` 로 인자를 받고 없으면 사용법 출력 후 `sys.exit(1)`.

## 하지 말 것
- rm 으로 파일을 지우지 않는다.
- pip install 로 무언가를 설치하지 않는다.
- git 명령어를 실행하지 않는다.
