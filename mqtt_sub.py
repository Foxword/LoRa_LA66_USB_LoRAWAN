import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import json
import time


def blink_led(pin):
    GPIO.output(pin, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)  # led off
    time.sleep(1)


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed: {mid} {granted_qos}")


def on_message(client, userdata, msg):
    json_str = json.loads(msg.payload.decode("ascii"))
    # print(json.dumps(json_str, indent=4))
    data = json_str["uplink_message"]["decoded_payload"]["bytes"]
    cpu_usage = data[0] / 100
    if len(data) > 1:
        cpu_usage = (data[0] * 256 + data[1]) / 100

    print(f"CPU usage: {cpu_usage}%")

    if cpu_usage < 10:
        blink_led(18)
    else:
        blink_led(15)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)  # 핀 번호 = 18, 출력

broker_address = "au1.cloud.thethings.network"
client = paho.Client()
client.username_pw_set(
    "wine",
    "NNSXS.6WLMZP5IKYX7GTZ2TAWXZLK2R5CVW2SBGXEQPSI.7UVE3OBIOCLC37MEMU2TPB52AWVE2K6X35O5FJTHLRA3KLNV76BQ",
)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(broker_address, 1883)
client.subscribe("#", qos=1)

client.loop_forever()
