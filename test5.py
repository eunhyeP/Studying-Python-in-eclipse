# 집합형 자료 형 중 tuple type : list 와 유사, 읽기 전용**(속도빠름)이라 수정불가 **, 중복허용

#t = 'a', 'b','c','a'
t =('a', 'b','c','a')   # 두개다 가능
print(t,type(t), len(t))
print(t.count('a'))
print(t.count('b'))
print(t.index('b'))


t2 = ('a',)  # tuple타입은 요소값이 하나만이면 뒤에 , 콤마를 꼭쳐줘야한다.
print(t2, type(t2), len(t2))

print()
p = (1,2,3)
#p[0] = 7    # 7로 변경 불가!!: 'tuple' object does not support item assignment
print(p,p[0])
    # 수정하구싶으면 list로 바꾸고 수정
    # 형변환 함수 list tuple
q = list(p) # 형변환 tuple -> list
q[0] = 7
p = tuple(q)# 형변환 list -> tuple
print(p,p[0], p[1:])

print()
t1 = (10,20)
print(t1)
    # 자리바꾸기
a,b = t1
b, a = a, b
t2 = a, b
print(t2)





