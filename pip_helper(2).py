import os
import time
import random

#thx name
Dev_name = '무가린'
tester = None


#dev_code active
dev_mode = 0
ran_dev_code = random.randint(1,10)
dev_code = ''

if ran_dev_code == 1:
    dev_code = '3524'
if ran_dev_code == 2:
    dev_code = '1003'
if ran_dev_code == 3:
    dev_code = '4920'
if ran_dev_code == 4:
    dev_code = '0517'
if ran_dev_code == 5:
    dev_code = '5912'
if ran_dev_code == 6:
    dev_code = '1231'
if ran_dev_code == 7:
    dev_code = '3004'
if ran_dev_code == 8:
    dev_code = 'error 205'
if ran_dev_code == 9:
    dev_code = '0000'
if ran_dev_code == 10:
    dev_code = '6999'


#Project info
Project_name = 'pip new user little helper'
Project_version = '0.0.1'
Project_PON = '초기 개발 단계'
pip_version = 'pip --version'

#Project Pro set
over = 0
english = 0
go = ""
install = 0
now_color = '일반[White]'
lang_v = 0
now_lang = ''
color_value = 0

clear = "cls"
shoort_tack = "--"
short_tack = "----------"
long_tack = "--------------------"
loong_tack = "----------------------------------------"
looong_tack = "------------------------------------------------------------"
tack = "> "
typing = "입력하기 : "
en_typing = "type here : "
choose_typing = "[예/아니요] : "
en_choose_typing = "[y/n] : "

#편리 기능으로 만들기

def s(str):
    os.system(str)

def lse():
    global english
    global typing
    global choose_typing
    global now_lang
    global Dev_name
    global tester
    global Project_PON
    global color_value
    global now_color
#한글/영어 패치
    if english == 0:
        typing = '입력하기 : '
        choose_typing = '[예/아니요] : '
        now_lang = '한국어'
        Dev_name = '무가린'
        tester = None
        Project_PON = '개발 초기 단계'
    if english == 1:
        typing = 'typing here : '
        choose_typing = '[y/n] : '
        now_lang = 'English'
        Dev_name = 'MuGaLin'
        tester = None

#색깔
    if color_value == 0:
        now_color = '일반[White]'
        s('color f')
    if color_value == 1:
        now_color = '초록색[Green]'
        s('color a')
    if color_value == 2:
        now_color = '빨간색[Red]'
        s('color c')
    if color_value == 3:
        now_color = '노랑색[Yellow]'
        s('color e')
    if color_value == 4:
        now_color = '푸른색[Blue]'
        s('color 9')
    if color_value == 5:
        now_color = '분홍색[Pink]'
        s('color d')

def t():
    global go
    global english
    if english == 0:
        go = input(typing)
    if english >= 1:
        go = input(en_typing)

def ct():
    global go
    global english
    if english == 0:
        go = input(choose_typing)
    if english >= 1:
        go = input(en_choose_typing)

#메뉴얼 txt
def package_iod_txt():
    global english
    if english == 0:
        print(short_tack, '패키지 다운로드 및 삭제.txt', short_tack)
        print()
        print('pip 패키지를 다운받거나 삭제하고 싶을떄는')
        print('명령어 > 패키지 설치 및 제거에 들어가면 현재 패키지 리스트와 패키지들에 버전들을')
        print('확인 할수 있습니다. 패키지를 다운로드 하고 싶을때는 [패키지 설치]라고 입력하고,')
        print('패키지 삭제를 원할때는 [패키지 삭제]라고 입력하면 됩니다.')
        print('이제 거기에서 원하는 pip 패키지를 입력하면 패키지를 다운/업데이트를 하거나 삭제할수')
        print('있습니다^^')
        print()
        print(long_tack)

def hello_world_txt():
    global english
    if english == 0:
        print(short_tack, '헬로우 월드', short_tack)
        print()
        print('안녕 세상. 이곳은 당신이 좀 더 원할한 pip 사용을 하기 위해 만들어진 프로그램입니다.')
        print('아직도 불편한 점이 많겠지만, 그래도 직접 입력보단 간접적인 입력을 선호하겠나요?')
        print()
        print(long_tack)
    if english == 1:
        print(short_tack, 'Hello World', short_tack)
        print()
        print('Hello world. This is')
        print('아직도 불편한 점이 많겠지만, 그래도 직접 입력보단 간접적인 입력을 선호하겠나요?')
        print()
        print(long_tack)

#UI_First
def open_setting():
    print(loong_tack)
    print()
    print('시작하기 전에 언어 설정은 필수 입니다. 설정 후에도 변경할수 있습니다.')
    print('you been start this before...you need this setting. you can set language in start after')
    print()
    print(shoort_tack)
    print('[한국어]')
    print('[English]')
    print(shoort_tack)

#UI
def stopping():
    global english
    if english == 0:
        print('종료 하시겠습니까?')

def s_version():
    global english
    if english == 0:
        print(long_tack, '버전' , long_tack)
        print()
        print('현재 버전 : ',Project_version,'(',Project_PON,')')
        print()
        print('(pip 버전)')
        s(pip_version)
        print(loong_tack)

def s_lang():
    global english
    if english == 0:
        print(long_tack, '언어 설정 : ', now_lang , long_tack)
        print()
        print('[대한민국]')
        print('[English]')
        print()
        print(loong_tack)
    if english == 1:
        print(long_tack, 'Langauge : ',now_lang, long_tack)
        print()
        print('[한국어]')
        print('[English]')
        print()
        print(loong_tack)

def s_color():
    global english
    if english == 0:
        print(long_tack, '글자색', long_tack)
        print()
        print('[초록색]')
        print('[빨간색]')
        print('[노랑색]')
        print('[푸른색]')
        print('[자주색]')
        print('[초기화]')
        print()
        print('[돌아가기]')
        print()
        print(loong_tack)

def setting():
    global english
    if english ==0:
        print(long_tack, '설정', long_tack)
        print()
        print('[글자색] : ', now_color)
        print('[버전]')
        print('[언어] : ', now_lang)
        print('[돌아가기]')
        print()
        print(loong_tack)
    if english ==1:
        print(long_tack, 'Setting', long_tack)
        print()
        print('[color] : ', now_color)
        print('[version]')
        print('[language] : ', now_lang)
        print('[back]')
        print()
        print(loong_tack)

def credits():
    global english
    if english == 0:
        print(long_tack, '크레딧', long_tack)
        print()
        print(shoort_tack, '개발자', shoort_tack)
        print(Dev_name)
        print()
    if english == 1:
        print(long_tack, 'Credits', long_tack)
        print()
        print(shoort_tack, 'Dev', shoort_tack)
        print(Dev_name)
        print()

def manual():
    global english
    if english == 0:
        print(long_tack, '메뉴얼', long_tack , dev_code)
        print()
        print('[패캐지 다운로드 및 삭제]')
        print('[헬로우 월드]')
    if english == 1:
        print(long_tack, 'Manaul', long_tack)
        print()
        print('[Package Download or Delete]')
        print('[Hello World!]')

def pip_check():
    global english
    if english == 0:
        print(long_tack, '체크', long_tack)
        print()
        

def install_or_delete():
    global english
    if english == 0:
        print(long_tack, '설치 및 제거', long_tack)
        print()
        print(short_tack, '현재 설치된 패키지', short_tack)
        s('pip list')
        print(long_tack)
        print('[패키지 설치/제거]')
        print('[돌아가기]')
        print(short_tack)
    if english == 1:
        print(long_tack, 'Install or Delete', long_tack)
        print()
        print(short_tack, 'Now Use Package', short_tack)
        s('pip list')
        print(long_tack)
        print('[package install/delete]')
        print('[back]')
        print(short_tack)


def command_u():
    global english
    global go
    if english == 0:
        print(long_tack, '명령어 사용',long_tack)
        print()
        print('[설치 및 제거]')
        print('[체크]')
        print()
        print(loong_tack)
    if english == 1:
        print(long_tack, 'Using command',long_tack)
        print()
        print('[install or Delete]')
        print('[Check]')
        print()
        print(loong_tack)

def home_u():
    global english       #UI setting
    global dev_mode
    if english == 0:
        if dev_mode == 0:
            print(long_tack + '메인 메뉴' + long_tack)
        if dev_mode == 1:
            print(long_tack, '메인 메뉴', long_tack , '(개발자 모드)')
        print()
        print('[명령어]')
        print('[메뉴얼]')
        if dev_mode == 1:
            print('[핵?]')
        print('[설정]')
        print('[크레딧]')
        print('[그만하기]')
        print()
        print(looong_tack)
    if english == 1:
        print(long_tack + 'Main Menu' + long_tack)
        print()
        print('[command]')
        print('[manual]')
        if dev_mode == 1:
            print('[hack?]')
        print('[setting]')
        print('[credits]')
        print('[exit]')
        print()
        print(looong_tack)    

#UI에 덮어 씌워야 하는 기능

def main():
    global go
    global english
    global over
    global dev_mode
    global now_color
    global now_lang
    global color_value
    while True:
        if over >= 1:
            break
        s(clear)
        lse()
        home_u()
        go = input(typing)
        if go == "명령어" or go == 'command':
            while True:
                s(clear)
                lse()
                command_u()
                go = input(typing)
                if go == '설치 및 제거' or go == 'install or delete':
                    while True:
                        s(clear)
                        install_or_delete()
                        go = input(typing)
                        if go == '패키지 설치':
                            while True:
                                global install
                                install = 1
                                s(clear)
                                if install == 1:
                                    print('다운 및 업데이트를 원하는 pip 패키지 이름을 입력하세요.')
                                if install == 0:
                                    print('삭제를 원하는 pip 패키지 이름을 입력하세요.')
                                print('이전 화면 [돌아가기]')
                                if install == 0:
                                    print('[모드 설치] : 삭제')
                                if install == 1:
                                    print('[모드 삭제] : 설치/업데이트')
                                print()
                                pip = input("입력하기 : ")
                                if pip == '돌아가기':
                                    break
                                
                                else:
                                    if install == 1:
                                        s("pip install " + pip + ' --upgrade')
                                        s('pause')
                                    if install == 0:
                                        s("pip uninstall " + pip)
                                        s('pause')
                                    
                        if go == '패키지 삭제':
                            while True:
                                install = 0
                                s(clear)
                                if install == 1:
                                    print('다운 및 업데이트를 원하는 pip 패키지 이름을 입력하세요.')
                                if install == 0:
                                    print('삭제를 원하는 pip 패키지 이름을 입력하세요.')
                                print('이전 화면 [돌아가기]')
                                if install == 0:
                                    print('[모드 설치] : 삭제')
                                if install == 1:
                                    print('[모드 삭제] : 설치/업데이트')
                                print()
                                pip = input("입력하기 : ")
                                if pip == '돌아가기':
                                    break

                                else:
                                    if install == 1:
                                        s("pip install " + pip + ' --upgrade')
                                        s('pause')
                                    if install == 0:
                                        s("pip uninstall " + pip)
                                        s('pause')
                        if go == '돌아가기':
                            break
                if go == '체크' or go == 'check':
                    while True:
                        s(clear)
                        pip_check()
                        go = input(typing)    
                        if go == '돌아가기' or go == 'back':
                            break 
                        
                if go == '돌아가기' or go == 'back':
                    break
        if go == '메뉴얼' or go == 'manual':
            while True:
                s(clear)
                lse()
                manual()
                go = input(typing)
                if go == '패키지 다운로드 및 삭제' or go == 'package dod':
                    while True:
                        s(clear)
                        package_iod_txt()
                        go = input(typing)
                        if go == '돌아가기' or go == 'back':
                            break
                if go == '헬로우 월드' or go == 'Hello World':
                    s(clear)
                    hello_world_txt()
                    go = input(typing)
                    if go == '돌아가기' or go == 'back':
                        break
                if go == '돌아가기' or go == 'back':
                    break

        if go == '설정' or go == 'setting':
            while True:
                s(clear)
                lse()
                setting()
                go = input(typing)
                if go == '글자색' or go == 'color':
                    while True:
                        s(clear)
                        lse()
                        s_color()
                        go = input(typing)
                        if go == '초록색' or go == 'green':
                            color_value = 1
                            lse()
                        if go == '빨간색' or go == 'red':
                            color_value = 2
                            lse()
                        if go == '노랑색' or go == 'yellow':
                            color_value = 3
                            lse()
                        if go == '푸른색' or go == 'blue':
                            color_value = 4
                            lse()
                        if go == '자주색' or go == 'pink':
                            color_value = 5
                            lse()
                        if go == '초기화' or go == 'reset':
                            color_value = 0
                            lse()
                        if go == '돌아가기' or go == 'back':
                            break

                if go == '버전' or go == 'version':
                    while True:
                        s(clear)
                        lse()
                        s_version()
                        go = input(typing)
                        if go == '돌아가기' or go == 'back':
                            break


                #오류 : ChatGPT가 해결 해줌[error : i love ChatGPT]
                if go == '언어' or go == 'language':
                    while True:
                        lse()
                        s(clear)
                        s_lang()
                        global english
                        go = input(typing)
                        if go == '한국어' or go == 'korean':
                            english = 0
                        if go == '영어' or go == 'English':
                            english = 1
                        if go == '돌아가기':
                            break

                if go == '돌아가기' or go == 'back':
                    break


        if go == '크레딧' or go == 'credits':
            while True:
                s(clear)
                lse()
                #UI
                go = input(typing)
                if go == '돌아가기' or go == 'back':
                    break

        if go == '그만하기' or go == 'exit':
            while True:
                lse()
                s(clear)
                stopping()
                go = input(choose_typing)
                if go == '예' or go == 'y':
                    over += 150
                    break
                if go == '아니요' or go == 'n':
                    break
            
        if go == 'dev_mod_active 1' or go == 'dev_mod_active' or go == 'dev_mod':
            while True:
                s(clear)
                lse()
                print('코드를 입력하세요.')
                print()
                go = input(typing)
                if go == dev_code:
                    dev_mode = 1


#실행
while True:
    s(clear)
    lse()
    open_setting()
    go = input('입력하기(typing here) : ')
    if go == '한국어' or go == 'Korean':
        english = 0
        break
    if go == 'English' or go == '영어':
        english = 1
        break
    else:
        print('다시 입력하세요.')
        print('try again')
main()
if over >= 1:
    s('exit')