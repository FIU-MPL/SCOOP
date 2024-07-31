import customtkinter
import subprocess
from gpiozero import LED
from time import sleep
from gpiozero import DistanceSensor
from threading import Thread
from picamera2 import Picamera2, Preview


led = LED(16)
ultrasonic = DistanceSensor(echo=17, trigger=4)

# Window Appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

on_off = True
root = customtkinter.CTk()
root.geometry("500x350")

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.start()

def Interactive():
    # LED Function
    def led_on_off():
        if switch_LED.get() == "On":
            led.on()
        else:
            led.off()
            

    # Distance Sensor Code
    def dis():
        Sum = 0
        count = 0
        while count != 10000:
            Sum += ultrasonic.distance
            count += 1
        Sum /= 100
        distext = str(round(Sum, 2)), "cm"
        Dis_Pre.configure(text= distext)
        
    def Manual_Focus(value):
        val = int(value)
        picam2.set_controls({"AfMode": 0, "LensPosition": val})
        print(val)
        Man_Cam_Label.configure(text=val)
        
        
        

    # Frame
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # Page Name
    label = customtkinter.CTkLabel(master=frame, text = "SCOOP V2")
    label.pack(pady=12, padx=10)

    # LED Switch
    switch_LED=customtkinter.StringVar(value="Off")
    LEDSwitch = customtkinter.CTkSwitch(master=frame, text="LED", command=led_on_off, variable= switch_LED, onvalue="On", offvalue="Off")
    LEDSwitch.pack(pady=12, padx=10)

    # Projector Switch
    switch_pro=customtkinter.StringVar(value="Off")
    LEDSwitch = customtkinter.CTkSwitch(master=frame, text="Projector", command=led_on_off, variable= switch_pro, onvalue="On", offvalue="Off")
    LEDSwitch.pack(pady=12, padx=10)

    # Distance Outputted by Distance Sensor
    Dis_Pre=customtkinter.CTkButton(master=frame, text="", command=dis)
    Dis_Pre.pack(pady=12, padx=10)

    # Distance Outputted by Distance Sensor
    Man_Cam=customtkinter.CTkSlider(master=frame, from_=0, to=15, command=Manual_Focus)
    Man_Cam.pack(pady=12, padx=10)
    
    Man_Cam_Label=customtkinter.CTkLabel(master=frame, text="")
    Man_Cam_Label.pack(pady=12, padx=10)



def camera():
    print("test")



    
if __name__ == '__main__':
    Thread(target = Interactive).start()
#   Thread(target = camera).start()
root.mainloop()
