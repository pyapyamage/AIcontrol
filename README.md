![header](https://capsule-render.vercel.app/api?type=slice&color=auto&height=300&section=header&text=My%20experience&fontSize=90)
# Hi, there!
#### Welcome to my page  
#### I'm Seung Woon Lee, college student from Changwon in South Korea XD
  
  
##  what I'm learning?
-Melsec plc  
-NX    
-Python

My current experience    
![image description](http://kldp.org/files/vi-vim-cheat-sheet-ko.png)
Click [the source of the image](https://kldp.org/node/102947)  

|`Sr.No.`|`Funtion & Description`|
|:--|--|
|1|int(x [,base]) - *Converts x to a integer. The base specifies the base if x is a string.*|
|2|float(x) - *Converts x to a floating-pointnumber.*|
|3|complex(real [,imag]) - *Creates a complex number.*|
|4|str(x) - *Converts object x to a string rreoresentation.*|
|5|repr(x) - *Convers object x to an expression string.*|
|6|eval(str) - *Evaluates a string and returns an object.*|
|7|tuple(s) - *Converts s to a tuple.*|
|8|list(s) - *Converts to a list.*|
|9|set(s) - *Converts to a set.*|
|10|dict(d) - *Converts a dictionary. d must be a sequence of (key,value) tuples.*|
|11|Frozenset(s) - *Converts s to a frozen set*|
|12|chr(x) - *Converts an integer to a character.*|
|13|unichr(x) - *Converts an integer to a Unicode character.*|
|14|ord(x) - *Converts a single character to its integer value*|
|15|hex(x) - *Converts an integer to a hexadecimal string.*|
|16|oct(x) - *Converts an integer to an octal string.*|


   
   손의 좌표를 [mediapipe](https://google.github.io/mediapipe/) 모듈로 손의 마디를 좌표로 인식한후  
인공지능(AI)으로 학습시켜서 램프를 키는 프로젝트입니다.

아래 유사 프로젝트들의 소스코드를 적극 활용하였습니다.

* [gesture-recognition by kairess](https://github.com/kairess/gesture-recognition)

# 프로젝트 실행 과정

학습
1. 데이터셋.py 를 실행시킨후 웹캠으로 0도 90도 180도에 대한 데이터셋을 만듭니다.
2. 머신러닝.ipynb를 순서대로 실행시켜 ai를 학습합니다.

실행
1. 웹캠과 아두이노를 연결한후 손가락 방향을 바꾸면서 각도가 바뀌면 램프가 바뀌는지 확인한다.
<img src="https://github.com/LETAUK/AIControlE/blob/main/img/0s.JPG" width="300" height="200">
<img src="https://github.com/LETAUK/AIControlE/blob/main/img/90s.JPG" width="300" height="200">
<img src="https://github.com/LETAUK/AIControlE/blob/main/img/180s.JPG" width="300" height="200">

# 각 구성파일의 역할

|파일명|설명|
|------|---|
|dataset폴더|데이터셋을 저장하는 폴더입니다|
|models.h5|학습시킨 AI 모델입니다|
|sketch_nov15a폴더|아두이노 파일입니다|
|데이터셋.py|데이터셋을 만드는 실행파일입니다|
|머신러닝.ipynb|AI학습을 시키는파일입니다|
|실행.py|AI를 실행시키는 파일입니다|

# 한계

* 손의 여러가지 각도는 인식이 되지 않는다  
* 검지손가락 이외의 손가락으로 가리킬시 손가락인식이 불가능하다

[![Video Label](https://www.youtube.com/watch?v=MV3SJdUArbw)

