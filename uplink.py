from lora_library import LoRaLib

# %%

# Serial Port 설정
#    Window일 경우 : COMx
#    Linux일 경우 : /dev/ttyxxxx
serial = LoRaLib("COM5")
serial.open()

# %% 업링크(node -> GW) 데이터 전송
response = serial.send_text_data(0, 32, 5, "Hello")
print(response)

serial.close()
