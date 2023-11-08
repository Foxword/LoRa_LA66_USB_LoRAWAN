from lora_library import LoRaLib

# %%

# Serial Port 설정
#    Window일 경우 : COMx
#    Linux일 경우 : /dev/ttyxxxx
serial = LoRaLib("COM5")
serial.open()

# %% 터미널에서 AT 명령어 입력 받기
user_input = input("명령어를 입력하세요 : ")
print("입력받은 명령어 : ", user_input)
response = serial.set_at_command(user_input)
print("Response : ", response)

# %% 업링크(node -> GW) 데이터 전송
response = serial.set_text_data(0, 32, 5, "Hello")

# %% 다운링크(GW -> node) 데이터 출력
response = serial.print_last_received_binary_data()

# %% 시리얼 포트 닫기
serial.close()
