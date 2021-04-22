#집합형 자료형 
#1.문자열_ str type    :    순서가 있고 수정 불가
# str
# 문자열 관련 함수 일부 수행

s = 'sequence'  # <class 'str'>
print(len(s))   # len() 변수문자 길이
print(s.count('e')) # s변수에 e가 몇개 나오니??
print(s.find('e'), s.find('e',3)  ,s.rfind('e'))    # 1 4 7
print(s.startswith('s'), s.startswith('a'))         # True False
#...

# 요소값 수정 불가
ss  = 'mbc'
print('mbc', id('mbc'),id(ss))  # mbc 1842631031728 1842631031728 : 주소가같다
print(ss)
ss='abc'
print(ss)
print(id(ss))       # 2433685824176 새로운 주소값

# 슬라이싱 (점프투파이썬 67p) : 집합형 자료의 값 일부 참조
''' ss = sequence 01234567 or ~-3-2-1 이런식으로 나온다.'''
    # 0부터 시작
print(s,' ', s[0], ' ', s[1],' ', s[7]) # sequence   s(0번쨰)   e(1번째)   e(7번째)

print(s,' ', s[-1], ' ', s[-2],' ', s[-8])  # sequence   e   c   s
# s[0] ='k'값변경불가능:  'str' object does not support item assignment  immutable

    #[시작:끝:간격]부분출력
print(s[1:5],' ',s[:4],' ',s[6:],' ',s[1:7:1],' ',s[1:7:2])   # eque   sequ   ce   equenc   eun
print(s[1:7:1], s[1:7])    # s[1:7:1]은 s[1:7]이랑 같다. equenc equenc
print(s[-4:-1],' ',s[-4:],' ',s[::2])   # enc   ence   sqec

print()
s2 = 'kbs mbc'
s2 = ' ' + s2[:4] + 'sbs ' +s2[4:] +' ' 
print(s2)       #  kbs sbs mbc
print()
    # 나누기
    # 변수.split(sep='구분자') 은 변수안에 문자열을 구분자로 나눠라
    # rsplip(), lsplip()
s3 = s2.split(sep = ' ')
print(s3)       # ['', 'kbs', 'sbs', 'mbc', '']

    # 합치기 : join
s4 = ';'.join(s3) 
print(s4)       # ;kbs;sbs;mbc;
    # 대체한다 : replace
a = 'life is too short'
b = a.replace('life','My leg')
print(id(a))    # 1968142623008
print(id(b))    # 1968142622928 위치정보는 둘이 다르다
print(b)        # My leg is too short




