import psutil
from speakFun import *

def batteryLife():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percentage = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    speak(percentage + '% and charger ' + plugged)

def memory():
    speak("Talking about virtual memory ! ")
    obj=psutil.virtual_memory()
    speak("total is " + str(obj.total) + "whereas available is only " +str(obj.available) +" out of which " + str(obj.used) + " is used that is " + str(obj.percent) + " percent.")

    speak("Talking about swap memory ! ")
    obj = psutil.swap_memory()
    speak("total is " + str(obj.total) + " out of which " + str(obj.used) + " is used that is " + str(obj.percent) + " percent.")

def ip():
    speak("Your IP address is ")
    obj=psutil.net_connections()
    speak(str(obj.raddr.ip))


