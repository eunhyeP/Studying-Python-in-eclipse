# 집합형 자료형 중 list type : 순서가 있고 요쇼값 수정이 가능, 중복 가능

    
a= [1,2,3]
print(a,type(a))        # [1, 2, 3] <class 'list'>
    # 리스트안에 리스트를 넣을수있다.
b = [10, a, 30.5, True, '컴퓨터']
print(b, type(b))       # [10, [1, 2, 3], 30.5, True, '컴퓨터'] <class 'list'>

    #진정한 배열은 numpy에서.. 아디오스
print()
family = ['엄마','아빠','나','여동생']
    # 리스트에 요소값 수정 추가
family.append('남동생')         # 남동생 추가 리스트
family.insert(0, '할아버지')    # 할아버지 엄마자리 [0]에 추가
family.extend(['삼촌','조카'])  # 삼촌조카 리스트로 뒤에 추가
family += ['이모','고모']       # 이모고모 리스트 뒤에 추가
    # 리스트에 요소값 수정 제거
family.remove('나')              # 나 제거
    # 리스트에 요소값 수정 변경
print(family)           
print(len(family))      
print(family, len(family))
print(family.index('남동생'))      # 남동생의 위치 : 4
print('엄마' in family, '마더' in family)   # True False
print(family[0], ' ', family[2:5])
print(family[-1], ' ', family[-4:])

print()
aa = [1,2,3,['a','kor','c'],4,5]
print(aa)
print(aa[0])
aa[0] = 100 # immutable 수정가능합니다.~~~
print(aa[0])
print(aa)
print(aa[3])
print(aa[3][1])
print(aa[3][:2])

print()
# 지우기
print(aa)
aa.remove(4)    #위치 4 삭제 [100, 2, 3, ['a', 'kor', 'c'], 5]
del aa[4]       #위치 4 삭제 [100, 2, 3, ['a', 'kor', 'c']]
print(aa)       #

aa[3].remove('c')   # [100, 2, 3, ['a', 'kor', 'c']]
print(aa[3][0]) # a
del aa[3][0]
print(aa)

print()
    # sort함수
aa2 = ['123','34','234']
print(aa2)
aa2.sort()
print(aa2)  # ['123', '234', '34'] 기본이 오름차순
aa2.sort(key= int)  # (숫자순으로)int형태로 정렬하라 
print(aa2)  # ['34', '123', '234']

print()
aaa = [3,1,5,2,4]
aaa.sort()
print(aaa)                  # [1, 2, 3, 4, 5] 오름
aaa.sort(reverse =True)     # [5, 4, 3, 2, 1] 내림
print(aaa)


# 얕은복사 깊은 복사
print('~~~'*10)
name = ['tom','james','oscar']
name2 = name    # 주소치환(복사), 얕은복사
print(name, id(name))
print(name2,id(name2))
name[0] = 'paul'    # 바꾸기
print(name,' ', name2)   # 둘다 바뀜

print()
import copy 
name3 = copy.deepcopy(name) # 깊은 복사 : 별도의 공간을 확보하고 새로운 객체 저장
print(name, id(name))
print(name3, id(name3))
name[1] = 'john'
print(name,' ', name3)      # ['paul', 'john', 'oscar']   ['paul', 'james', 'oscar']

# LiFO >> 스택구조
# FinRO >> 먼저들어온놈이 먼저나간다

print()
sbs = [10,20,30]
sbs.append(40)
print(sbs)
sbs.pop() # stack 구조 : LIFO
print(sbs)
sbs.pop()
print(sbs)

print()
sbs = [10,20,30]
sbs.append(40)
print(sbs)
sbs.pop(0) # queue 구조 : FIFO
print(sbs)
sbs.pop(0)
print(sbs)



