from ast import Delete
from ctypes.wintypes import tagMSG


I 입력모드 (수정가능)
입력모드 상태에서 esc 누르면 명령모드

종료옵션
:q 그냥 종료
:q! 강제종료
:w 저장
:w! 강제저장
:wq 저장하고 종료
:wq! 강제 저장하고 종션

명령모드에서
i 커서 앞 입력모드
a 커서 뒤 입력모드
I 문장 시작 입력모드
A 문장 끝 입력모끝

방향키
H 왼쪽
J 위
K 아레
L 오른쪽

네비게이션
0 문장 앞으로 이동
$ 문장 끝으로 이동
w word(단어)단위 앞으로 건어뛰기
b backward 단어단위 뒤로 건너뛰기
H 화면 위
M 화면 중간
L 화면 끝
gg 파일 앞
G 파일 끝
20G 20번째 줄로 이동
ctrl u 위로 스크롤링
ctrl d 아레로 스크롤링
{문단 시작
}문단 끝

명령어
x 커서 아래 글자 삭제
dd 문장 삭제
yy 문장 복사
p 붙여넣기
*p 클립보드 붙여넣기 (json 파일 설정에서 권한을 먼저 줘야함)

<명령어 + 목적어>
명령어
d delete(cut)
y yank(copy)
c change

목적어 (a는 포함 i는 미포함) ex) "I like chiken" 에서 da"라고 하면 "포함 삭제 di" 라고하면 " 제외 내부만 삭제
aw a word
at a tag
ap a paragraph
a sentence
it in tag
i" in "
ip in paragraph
