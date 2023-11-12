# LoRa_LA66_USB_LoRAWAN

1. Port configuration

   The 'port' will be different according to user's computer OS.
   
   Change the port variable considering user's computer OS.
   
   If windos OS, the port will be 'COMx'. (ex. COM3)
   
   If Linux OS, the port will be '/dev/ttyxxxx'. (ex. /dev/ttyUSB0 or /dev/tty001...)

2. import

   The 'pyserial' packages need to be installed.

   Run
   <pre>
      ~$ pip install pyserial
   </pre>

3. USB Driver
   
   For using LA66 USB LoRaWAN Adapter, you need to install "CP210x USB to UART Bridge VCP Drivers".

   Follow the link and download the driver.

   <pre>https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads</pre>
