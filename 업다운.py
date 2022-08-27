import os
정답 = 18

while True:
    입력한값 = int(input("정답 :"))
    if 입력한값 < 정답:
        print("업")
    if 입력한값 > 정답:
        print("다운")
    if 입력한값 == 정답:
        print("정답")
        break