#112p 4번
"""
#풀이1
숫자리스트 = []
while True:

    숫자 = input("0부터 9사이의 숫자를 입력하세요 >>>")
    if 숫자 in 숫자리스트:
     continue
    else:
     숫자리스트.append(숫자)
     if len(숫자리스트) == 5:
         break
print("모두 입력되었습니다.")
print("입력된 값은 {}입니다 ".format(숫자리스트))
#풀이 2
숫자리스트 = []
while True:

    숫자 = input("0부터 9사이의 숫자를 입력하세요 >>>")
    숫자리스트.append(숫자)

    if len(set(숫자리스트)) == 5:
         break
print("모두 입력되었습니다.")
print("입력된 값은 {}입니다 ".format(set(숫자리스트)))

#129번 1번
#배운 선에서만 1부터 5까지의 수를 역순으로
for i in range(1,6):
    print(6-i)
#우리 출력
#1     5
#2     4
#3     3
#4     2
#5     1
#책에서 원한 답

for i in range(5,0,-1):
    print(i)

#129p 4번
exam = [99,78,100,91,81,85,54,100,71,50]
scor = []
#1번쨰방법 : 점수를증가시킬때 if문을 거는거고
#for문을 이용한 iteration
for 점수 in exam:
    print(점수)
    #while문을 이용한 interatioin
idx = 0
while idx < len(exam):
      print(exam[idx])
      idx += 1
    #2번쪠 방법:출력을할때 알아서 100점 초과는 자르는거
score = []
for 점수 in exam:
    score.append(점수 + 5)

for 점수 in score:
    if 점수 > 100:
     print(100, end=' ')
    else:
        print(점수, end=' ')

#130p 5번
#출력 안됨
숫자 = 0
for 왼 in range(2,10):
    for 오 in range(1,10):
        숫자 = 숫자 + 1
        print(숫자, end=' ')
        if 숫자[0] and 숫자[1] == 3:
         print("짝")
    print()
"""
for 십의자리 in range(10):
        for 일의자리 in range(10):
          숫자 = (10*십의자리)+(일의자리+1)

          출력 = ''
          if 숫자 % 3 == 0:
              출력 = '짝'
          else:
              출력 = 숫자

          if 숫자 > 10 and 숫자 % 3 ==0:
              if(숫자//10) % 3 == 0:
                  출력 = 출력 + "짝"
          print(출력, end='\t')
        print("")