# 집합형 자료 형 중 set type : 순서x , 중복X

# 순서없어서 슬라이싱 불가 
a = {1, 2, 3, 1}
print(a, len(a))    # {1, 2, 3}>>중복제거 3 >>중복제거된 갯수
#print(a[0])         # 순서없어서 슬라이싱 불가 : 'set' object is not subscriptable

b= {3,4}

print(a.union(b))           # 합집합    {1, 2, 3, 4}
print(a.intersection(b))    # 교집합    {3}
print(a | b)                # 합집합    {1, 2, 3, 4}
print(a & b)                # 교집합    {3}
print(a - b)                # 차집합    {1, 2}

print()
b.update({6,7})
b.update({8,9})
b.update({10,11})
print(b)                     # {3, 4, 6, 7, 8, 9, 10, 11}

print()
# 해당값이 없으면 에러가 떨어진다. 있으면 삭제
b.discard(7)        # 값에 의한 삭제 !
b.remove(6)         # 값에 의한 삭제 !

print(b)                    # {3, 4, 8, 9, 10, 11}


#
c= set()
c = b
print(c)        # b랑 같은 값이 출력된다.
c.clear()
print(c)        # 비워짐 set()
print(b)        # 같은개체라 얘도 비워짐 

print()
 
li = [1,2,2,3,1]
s = set(li)# 중복제고 싶으면 set에 담가주면된다 ㅋㅋㅋㅋㅋ
li = list(s) 
print(li, type(li))     # [1, 2, 3] <class 'list'>
''' 물론 유니크 함수도 있지만 set도 있다는걸 알면된다. '''






