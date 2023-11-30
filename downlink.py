from lora_library import LoRaLib

# %%

# Serial Port 설정
#    Window일 경우 : COMx
#    Linux일 경우 : /dev/ttyxxxx
serial = LoRaLib("COM5")
serial.open()

response = serial.send_text_data(0, 32, 5, "Hello")
response = serial.print_last_received_binary_data()
print(response)

serial.close()
