## 해결해야할 작업: 4일 동안 메뉴 전체 판매량 / 하루 평균 판매량
## 작업 순서
### 1. 파일 열기
### 2. 파일 한 줄 읽기/ 리스트로 반환(제목 리스트)/ 제목별 리스트 생성
### 3. 데이터 읽기(반복문) 데이터를 리스트로 반환 (데이터리스트)(제목 데이터 다음부터 [1]번 인덱스 부터)
### 4. 제목 리스트에 append [1]인덱스 부터
### 5. 파일 닫기
### 6. 변수에 데이터 할당 
### 7. sum 리스트, avg 리스트 생성 (날짜별)
### 8. 합계구하기(4일)(반복문) format 으로 작업 출력

#### 1
f=open("coffeeShopSales.txt",'r',encoding="utf8")
#### 2
header=f.readline()
headerList=header.split()

espresso=[]
americano=[]
cafelatte=[]
cappucino=[]

#### 3 + 4
for line in f:
  dataList=line.split()

# 연산을 위해 숫자로 변환 잊지말기
  espresso.append(int(dataList[1]))
  americano.append(int(dataList[2]))
  cafelatte.append(int(dataList[3]))
  cappucino.append(int(dataList[4]))

#### 5
f.close()

#### 6
print("{}:{}".format(headerList[1],espresso))
print("{}:{}".format(headerList[2],americano))
print('{}:{}'.format(headerList[3],cafelatte))
print('{}:{}'.format(headerList[4],cappucino))

#### 7
total_sum=[sum(espresso),sum(americano),sum(cafelatte),sum(cappucino)]
total_avg=[sum(espresso)/len(espresso),sum(americano)/len(americano),sum(cafelatte)/len(cafelatte),sum(cappucino)/len(cappucino)]

#### 8
for k in range(len(total_sum)):
  print("[{}] 판매량(잔)".format(headerList[k+1])) #### 날짜[k] 다음부터
  print("-4일 동안:{}, 하루 평균:{}".format(total_sum[k],total_avg[k]))
