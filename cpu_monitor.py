from lora_library import LoRaLib
import psutil
import time

serial = LoRaLib("COM5")
serial.open()


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU usage: {cpu_usage}%")
    cpu_usage_str = str(hex(int(cpu_usage * 100)))[2:]  # CPU 이용률을 16진수 String으로 변환

    if len(cpu_usage_str) % 2 != 0:
        return "0" + cpu_usage_str
    else:
        return cpu_usage_str


while True:
    data = get_cpu_usage()
    serial.send_text_binary_data(1, 2, int(len(data) / 2), data)
    time.sleep(5)
