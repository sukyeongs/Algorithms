# map(적용시킬 함수, 리스트) : 리스트의 모든 요소들에 적용시킬 함수를 각각 실행하는 함수

a = ['1', '3', '2', '8']
a = list(map(int, a))
>> a = [1, 3, 2, 8]

# 띄어쓰기로 분리된 입력을 받아 정수형으로 변환시킬 때
n, m = map(int, input().split())
