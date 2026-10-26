# Lab07 정리: 파이썬으로 FASTA 파일 다루기

> 이 문서는 `lab07/doc/lab07.md` 의 복사본이다. 아래 경로(`data/`, `src/`, `doc/`)는 모두 `lab07` 폴더 기준이다.

## 개요
파이썬 기초(문자열·반복문·함수·딕셔너리)부터 시작해서, 명령행 인자로 FASTA 파일을 받아
서열 개수·길이·GC 비율을 계산하고, 조건에 맞는 서열을 골라 새 파일로 저장하는 데까지 진행했다.
마지막에는 반복해서 쓰는 코드를 `fasta.py` 모듈로 묶어 다른 스크립트에서 불러 썼다.

모든 스크립트는 lab07 폴더에서 실행한다.

```bash
cd lab07
python3 src/countseq.py data/seqs.fasta
```

## 데이터 (`data/`)

| 파일 | 내용 |
|---|---|
| `seqs.fasta` | 엽록체 유전자 부분 서열 3개 (gene1 rbcL, gene2 matK, gene3 psbA). 한 서열이 여러 줄에 걸쳐 있음 |
| `seqs2.fasta` | 짧은 예제 서열 2개 (apple, banana) |
| `lower.fasta` | 소문자가 섞인 서열 2개 (low1, low2) — 대소문자 처리 확인용 |

## 스크립트 (`src/`) — 진행 순서대로

### 1. 파이썬 기초
| 파일 | 배운 것 |
|---|---|
| `seq.py` | 문자열 변수, `len()` 으로 서열 길이 구하기 |
| `gc.py` | `count()` 로 G·C 개수 세기, GC 비율 계산, `round()` 로 반올림 |
| `atgc.py` / `atgc.sh` | 같은 `for` 반복문을 파이썬과 bash 로 비교 |
| `fseqlen.py` | `print` 하는 함수와 `return` 하는 함수의 차이 (`print` 만 하면 결과는 `None`) |
| `fgc.py` | GC 비율을 계산하는 함수 `gc_content()` 정의하고 부르기 |

### 2. 명령행 인자로 FASTA 파일 읽기
| 파일 | 하는 일 |
|---|---|
| `countseq.py` | `>` 로 시작하는 줄을 세어 서열 개수 출력. 인자가 없으면 사용법 출력 후 `sys.exit(1)` |
| `seqlen.py` | 서열 이름별 길이를 딕셔너리에 모아 출력 (여러 줄 서열도 합산) |
| `fastainfo.py` | 파일 이름, 서열 개수, 서열 이름 목록, 총 염기 수 출력 |
| `batchinfo.py` | `glob` 으로 폴더 안의 모든 `.fasta` 파일을 돌며 서열 개수를 탭 구분 표로 출력 |
| `filter.py` | 길이 20~40, GC 0.4~0.6 인 서열만 골라 출력 |

서열 이름은 `line[1:].split()[0]` 으로 `>` 뒤 첫 단어만 쓴다.
(`>gene1 chloroplast rbcL partial` → `gene1`)

### 3. 모듈로 묶기: `fasta.py`
자주 쓰는 함수를 한 파일에 모았다.

| 함수 | 하는 일 |
|---|---|
| `read_fasta(filename)` | FASTA 파일을 읽어 `{이름: 서열}` 딕셔너리로 돌려준다 |
| `write_fasta(seqs, filename)` | `{이름: 서열}` 딕셔너리를 FASTA 파일로 저장한다 |
| `gc_content(seq)` | GC 비율(0~1)을 돌려준다. 빈 서열이면 0.0 |
| `len_fasta(filename)` | (작성 중) 현재는 `read_fasta` 와 같은 내용 |

`if __name__ == "__main__":` 아래 코드는 `fasta.py` 를 직접 실행할 때만 동작하고,
다른 스크립트에서 `import` 할 때는 실행되지 않는다.

모듈을 불러 쓰는 스크립트:

| 파일 | 하는 일 |
|---|---|
| `countseq2.py` | `read_fasta` 로 읽어 서열 개수 출력 (`countseq.py` 를 짧게 다시 쓴 것) |
| `filter_fasta.py` | 최소 길이 이상인 서열만 골라 새 FASTA 파일로 저장 |

`from fasta import ...` 는 `fasta.py` 가 같은 폴더에 있어야 하므로 `src` 폴더에서 실행한다.

```bash
cd src
python3 filter_fasta.py ../data/seqs.fasta 20 ../doc/long.fasta
```

### 4. 기타
- `check_codespace.sh`: Codespace 환경(저장소, 폴더, 도구 설치 여부)을 확인해
  `doc/check_result.txt` 에 저장한다. lab 폴더에서 `bash src/check_codespace.sh` 로 실행.

## 실행 결과

`data/seqs.fasta` 기준:

| 스크립트 | 결과 |
|---|---|
| `countseq.py` | `3` |
| `seqlen.py` | gene1 30, gene2 15, gene3 22 |
| `fastainfo.py` | 서열 3개, 총 염기 수 67 |
| `fasta.py` (이름·길이·GC) | gene1 30 0.5 / gene2 15 0.467 / gene3 22 0.545 |
| `filter.py` | gene1 30 0.5 / gene3 22 0.545 (gene2 는 길이 15 라 제외) |
| `filter_fasta.py` (최소 20) | 3개 중 2개(gene1, gene3)를 `doc/long.fasta` 에 저장 |

`batchinfo.py data`:

```
file	count
data/lower.fasta	2
data/seqs.fasta	3
data/seqs2.fasta	2
```

## 확인할 점
- **대소문자**: `gc_content` 는 대문자 `G`, `C` 만 센다. `lower.fasta` 에서
  low1(`atgcgatacg`)의 GC 비율이 0.0, low2(`GGCCggccAT`)가 0.4 로 나온다.
  `seq.upper()` 로 바꾼 뒤 세야 정확하다 (실제 값: low1 0.5, low2 0.8).
- **빈 서열**: `filter.py` 는 길이가 0 인 서열이 있으면 0 으로 나누기 오류가 난다.
  `fasta.py` 의 `gc_content` 는 이 경우를 따로 처리한다.
- **사용법 출력**: `countseq.py` 만 인자 확인을 하고, 나머지 스크립트는 인자 없이 실행하면
  `IndexError` 가 난다.
