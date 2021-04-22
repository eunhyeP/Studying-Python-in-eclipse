# 연산자

v1 = 3 # 치환
v1= v2 = v3 = 5
print(v1,v2,v3)

                            #파이썬은 빈칸추천
print('출력1', end= ',')     # end : 줄바꿈을 막는다.구분자는 빈칸 
print('출력2')
print('출력1', \
      end= ' ')          # \ 소스를 읽기좋게 가독성**좋게
print('출력2')


v1 =1,2,3
print(v1)               # (1, 2, 3) 함께 출력

v1 , v2 = 10,20
print(v1,v2)            # 10 20
v2, v1 = v1,v2          # 코드를 위치를 바꾼것이다.
print(v1,v2)            # 20 10 

print()
v1, *v2 = 1,2,3,4,5      # paking 연산 : *를 달아주면됨 v1에 1을 받고 나머지는 v2에 넣어라
print(v1)               # 1
print(v2)               # [2, 3, 4, 5]

*v1, v2 = 1,2,3,4,5 
print(v1)               # [1, 2, 3, 4]
print(v2)               # 5

*v1, v2, v3 = 1,2,3,4,5
print(v1)               # [1, 2, 3]
print(v2)               # 4
print(v3)               # 5

print('---------------')

#연산자
print(5+3,5-3,5/3)      # 8 2 1.6666666666666667
print(5/3,5//3,5%3, divmod(5,3))     # 전부, 몫만, 나머지만 ,divmod(몫,나머지)
print(3+4*5,(3+4)*5)    # 연산자 우선순위 (), 산술(*,/  >> +,-), 관계(==,>,<,>=,,=!=), 논리(and, or, not), =
a= 3+4*5

print()
print(5>3,5==3,5!=3,5<=3)   # True False True False

print()
print(5>3 and 4<3, 5>3 and 4>=3)    # False True
print(5>3 or 4<3, 5>3 or 4>=3)      # True True
print(not(5>=3))                    # False

# 나동빈 파이썬 코딩테스트 책 많이 본다.
#*** 프로그래머는 알고리즘 로직의 대한 이해가 중요하다

print()
# 문자열 더하기 가능
print('문자열 데이터에 대하 연산 +,*')
print('한' +'국' +'인')
mbc = '문화방송' +'11'          # 문자열 + 가능
print(mbc)
print('한국' +'한국' +'한국')
print('한국'*3)               # 곱하기도 가능
print('**'*20)

# 누적 : 차곡차고 쌓아나가는것 
a= 10
a=a+1           # 누적했따~
a += 1          # 같은 형식이다. 근데 컴은 += 이게 더편함[-=,*=,/=]
print(a)        # 11

print()
# 부호변경
print('부호변경 : ' ,a, a * -1 , -a, --a, +a )  # 부호변경 :  12 -12 -12 12 12

# 불린 처리
print('불린 처리 : ', True, False, bool(True),bool(False))  # True False True False
print('불린 처리 : ', bool(1), bool(1.5), bool(-1))         # True True True
print('불린 처리 : ', bool(0), bool(0.0), bool(None), \
      bool(''), bool([]),bool({}))                        # 다 False

print()
# tab 키 : \t\ 이스케이프문자 : \
print('aa\t\bb')    # aa    b
print('aa\\t\bb')   # aa\tb
print('aa\\t\\bb')  # aa\t\bb

# raw string r을 선행 ,문자앞에 r''를 씌워주면 이스케이프 기능 상실
print(r'aa\t\bb')   # aa\t\bb
print('c:\nbc\bbc\tbs.txt')
'''c:
bcbc    bs.txt
'''
print(r'c:\nbc\bbc\tbs.txt')    # c:\nbc\bbc\tbs.txt
print('참고 : print 함수의 서식 사용')
print()
print(1.5678)
print(format(1.5678,'10.2f'))   # 1.57 : 셋째자리에서 반올림,둘째자리까지 표기

# 숫자, 문자 소수 넣기
print('냥이의 나이는 %d' %3)       # ('%d' %숫자)3
print('냥이의 나이는 %s이다.' %'세살')    # ('%s' %'문자')
print('냥이의 나이는 %d이며 장난감은 %s %s' %(2,'공','마우스'))
print('냥이의 나이는 %f이다.' %3.5)     # ('%f' %'소수')
# format 형식'{}'.format(,) >> 위치로 표현가능
print('이름은 {}, 나이는 {}이다. ' .format('tom',22))
print('이름은 {0}, 나이는 {1}이다. ' .format('tom',22))
print('이름은 {1}, 나이는 {0}살 이름 한번더 {1} ' .format(22,'tom'))






