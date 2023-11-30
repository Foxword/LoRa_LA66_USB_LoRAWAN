import serial
import time

# %% Basic command methods


class LoRaLib:
    def __init__(
        self,
        port,
        baudrate=9600,
        bytesize=8,
        parity="N",
        stopbits=1,
        timeout=None,
        xonxoff=0,
        rtscts=0,
    ):
        self.serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=bytesize,
            parity=parity,
            stopbits=stopbits,
            timeout=timeout,
            xonxoff=xonxoff,
            rtscts=rtscts,
        )

    def open(self):
        if self.serial.is_open:
            self.serial.close()
        self.serial.open()

    def close(self):
        if self.serial and self.serial.is_open:
            self.serial.close()

    def is_open(self):
        self.serial.is_open

    def reboot(self):
        print("reboot")
        time.sleep(1)
        self.serial.write(("ATZ" + "\r\n").encode())

    def set_at_command(self, command, waitDuration=0.5):
        self.serial.write((command + "\r\n").encode())
        time.sleep(waitDuration)
        return self.serial.read(self.serial.inWaiting()).decode("utf-8", "ignore")

    ### get
    def get_frequency(self):
        return self.set_at_command(command="AT+CHS=?")

    def get_data_rate(self):
        return self.set_at_command(command="AT+DR=?")

    def get_adr_status(self):
        return self.set_at_command(command="AT+ADR=?")

    def get_tx_power(self):
        return self.set_at_command(command="AT+TXP=?")

    def get_join_status(self):
        return self.set_at_command("AT+NJS=?")

    ### set
    # freq: in HZ
    def set_frequency(self, freq):
        return self.set_at_command(command=f"AT+CHS={freq}")

    # dataRate: Min 0 ~ Max 7
    def set_data_rate(self, dataRate):
        self.set_at_command(command=f"AT+DR={dataRate}")
        print(f"Automatically reboot to apply data rate {dataRate}")
        self.Reboot()

    # Disable: 0 // Enable: 1
    def set_adr(self, adr):
        self.set_at_command(command=f"AT+ADR={adr}")

    # dataRate: Min 0 ~ Max 5
    def set_tx_power(self, txPower):
        self.set_at_command(command=f"AT+TXP={txPower}")

    ### print
    def print_config(self):
        return self.set_at_command("AT+CFG")

    def print_last_received_data(self):
        return self.set_at_command("AT+RECV=?")

    def print_last_received_binary_data(self):
        return self.set_at_command("AT+RECVB=?")

    ### send
    def send_text_data(self, confirmStatus, fPort, payloadLength, payload):
        return self.set_at_command(
            f"AT+SEND={confirmStatus},{fPort},{payloadLength},{payload}",
            waitDuration=2,
        )

    def send_text_binary_data(self, confirmStatus, fPort, payloadLength, payload):
        return self.set_at_command(
            f"AT+SENDB={confirmStatus},{fPort},{payloadLength},{payload}",
            waitDuration=2,
        )
