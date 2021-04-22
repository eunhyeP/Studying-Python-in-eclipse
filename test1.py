
'''
여러줄
'''
# 한줄주석
print('환영합니다. 파이썬 세상에 오신것을!')
#''나 ""나 구분하지않음 단 짝을 맞춰야한다.
# 변수 : 객체(object,개체)의 주소를 기억하는 기억장소의 이름

'''지난시간'''
# 위도우 쇼뷰에가면 보이는거 만들수잇다.

# 프로젝트 다시만들기 name : pypron vision :3.8>pypron 오른쪽 >new >package >abc
#>adc 오른쪽 new>modual>asdf

#프로제그 지우기 pypron 오른쪽> 
#delete 체크안하면 주소(C:\work\psou\pypron)는 남는다>

#pack1을 지우고 다시만든다.

var1 = '안녕 파이썬'   # 문자열 객체의 주소를 변수 var1이 참조함(왼쪽을 오른쪽으로 치환함)
var1 =5             # 현재 tpye은 숫자

print(var1) #100번지가 참조하고있는 그 객체(object)가 가진 값을 출력
# 자바라는 언어는 포인터를 숨기지만 cpython은 포인터를 숨기지않음
# 인스턴스instance :메모리에 주소를 할당하는거
# 변수란 = 객체변수, 개체변수, 인스턴수 , 오브젝 variable 라 불린다.
# (타입) 이름 = 내용 처럼 타입을 적어주지만, 참조형 변수는 타입을 안적어도 된다.
# type은 입력자료에 의해 결정

a = 10      #10이 a에 주소장소에 있고 a의 주소를 가지고 10값을 찾아가는것
b = 77
c= b        # 변수를 변수에게 치환 :하나의 객체를 두개의 변수가 기억
d= 10

print(a,b,c,d)
# id() : 변수의 주소를 출력하는 함수
print('주소출력 : ',id(a),id(b),id(c),id(d))    #a,d의 주소가같고, b,c의주소가 같다.

# 주소 비교 명령어 is
print(a is b)   #a 와 b의 주소같니? False
print(a is d)   #a 와 d의 주소같니? True
# 값 비교 명령어 ==
print(a == b)   # False
print(a == d)   # True

print()
A = 1;a = 2;
print('A : ',A, ',a : ',a, '',id(A),id(a))  #python은 대소문자 구분함

aa=1
a11 =1
에이에이 =1     # 에러는 안나지만 한글은 권장하지 않는다.
_aa = 1
#-aa = 1   syntaxError : 문법오류 -하이퍼는 안돼~
# 11a = 1 숫자도 안돼~
# if = 1 :SyntaxError: invalid syntax 예약어 오류 밑에잇는걸 변수명으로 쓰지마라
print('예약어(기능이 부여된 명령어 이름) 보기')
import keyword  #외부모듈 , 필요시에만 import
# 명령덩어리.명령어 : 명령덩어리에서 명령어를 실행하라/ []은 집단을 나타내는것이다.
print(keyword.kwlist) # ['False', 'None', 'True', 'and', 'as', ...

# 변수선언 다 가능 (소대문자구분, _가능)
MY = 3.14   # 대문자로 된 변수명은 고정된값으로 된다. 파이값처럼
my = 1
My = 1
mY = 1
myKorexamScore =1       # 물결치면서 가독성 업!    
my_kor_exam_score=1     # 가독성업! 취향대로 하면 된다

# 참조하는 데이터의 성격을 이용해라 
kor = 100
irum ='tom'

# 어시스트 기능 ctrl + space
#print()
print(10,oct(10), hex(10),bin(10))  # 결과: 10(십진수) 0o12(8진수) 0xa(16진수) 0b1010(2진수)
print(10, 0o12, 0xa, 0b1010)        # 결과: 10 10 10 10


print('type(자료형) 확인')
print(3,type(3))        # int
print(3.1,type(3.1))    # float
print(3+4j,type(3+4j))  # complex
print(True,type(True))  # bool
print('3',type('3'))    # str
print('Kbs',type('kbs'))# str

print((1,),type((1,)))  # tuple
print([1],type([1]))    # list
print({1},type({1}))    # set
print({'key':1},type({'key':1}))        # dict
print({'key':'1'}, type({'key':'1'}))   # dict


