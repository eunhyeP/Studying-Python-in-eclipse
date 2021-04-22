# 집합형 자료 형 중 dic type : {키 : 값} 쌍으로 이루어짐. 순서X 
''' josn데이터를 파이썬에서 사용하려면 dic로 받아야한다.'''

mydic = dict(k1 =1, k2= 'abc' , k3 = 2.3)
print(mydic, type(mydic))

print()
dic= {'파이썬':'뱀','자바':'커피','컴퓨터':'AI'}
print(dic, type(dic))
print(dic['자바'])
#print(dic[0])***딕셔너리는 인덱스 안댐
        # 추가
dic['오라클'] = '예언자'
print(dic)
        # 수정
dic['자바'] = '프로그래밍 언어' 
print(dic)

        # 삭제
del dic['오라클']
print(dic)
        # clear 전체 비우기
dic.clear()
print(dic)

print()
friend = {'boy':'한국인','girl':'한송이','guy':'손오공'}
print(friend)
print(friend['girl'])
print(friend.keys())
print(friend.values())
print('boy' in friend)      # boy가 firend에 있냐없냐
print('baby' in friend)     # baby가 friend에 있냐없냐

print()
print( friend['boy'])       # 한국인
print(friend.get('boy'))    # 한국인




