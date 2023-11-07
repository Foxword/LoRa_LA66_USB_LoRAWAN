from AT_Command_Library import ATDevice

#%%

# Serial Port 설정
#    Window일 경우 : COMx
#    Linux일 경우 : /dev/ttyxxxx
port = 'COM8'

# 클래스 생성자 실행
Serial_Port = ATDevice(port)

# 시리얼 포트 열기
Serial_Port.open()

#%%

# 터미널에서 AT 명령어 입력 받기
user_input = input("명령어를 입력하세요 : ")
print("입력받은 명령어 : ", user_input)
response = Serial_Port.Send_Command(user_input)
print("Response : ", response)

#%%

# 터미널에서 입력받은 함수 실행
try:
    user_input = input("함수 이름을 입력하세요 : ")
    if hasattr(Serial_Port, user_input):
        if user_input[:3] == 'set':
            method = getattr(Serial_Port, user_input)
            parameter = input("매개변수를 입력하세요 : ")
            if callable(method):
                method(parameter)
            else:
                print("입력받은 함수를 실행할 수 없습니다.")
        else:
            method = getattr(Serial_Port, user_input)
            if callable(method):
                method()
            else:
                print("입력받은 함수를 실행할 수 없습니다.")
    else:
        print("입력받은 함수는 라이브러리에 없습니다.")
except Exception:
    print("Error")
                
#%%

# End Serial_Port 설정값 불러오기
response = Serial_Port.Check_Config()
print('Response from Serial_Port:', response)

#%%

# 네트워크 가입 상태 확인
response = Serial_Port.Check_Network_Join_Status()
print('Response from Serial_Port:', response)

#%%

# 게이트웨이에 업링크 메시지 보내기
response = Serial_Port.Send_Uplink_Message(0,32,5,'HAPPY',5)

#%%

# 다운링크 메시지가 있는 경우 수신하여 확인
response = Serial_Port.Print_Downlink_Message()


#%%

# 시리얼 포트 닫기
Serial_Port.close()