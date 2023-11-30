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

serial.close()
