# NanoPI

[http://wiki.friendlyarm.com/wiki/index.php/WiringNP:_NanoPi_NEO/NEO2/Air_GPIO_Programming_with_C#Introduction_to_WiringPi](http://wiki.friendlyarm.com/wiki/index.php/WiringNP:_NanoPi_NEO/NEO2/Air_GPIO_Programming_with_C#Introduction_to_WiringPi)

[https://wiki.friendlyarm.com/wiki/index.php/NanoPi_NEO](https://wiki.friendlyarm.com/wiki/index.php/NanoPi_NEO)

[https://download.friendlyarm.com/nanopineo](https://download.friendlyarm.com/nanopineo)

## Pinout

[https://wiki.friendlyarm.com/wiki/index.php/NanoPi_NEO](https://wiki.friendlyarm.com/wiki/index.php/NanoPi_NEO)

## **GPIO Programming**

**Using this module: [https://pypi.org/project/NPi.GPIO/](https://pypi.org/project/NPi.GPIO/)**

**Example code (python2):**

```python
import NPi.GPIO as GPIO
import time
PIN_NUM = 3
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM,GPIO.OUT)
while True:
        GPIO.output(PIN_NUM,True)
        time.sleep(1)
        GPIO.output(PIN_NUM,False)
        time.sleep(1)
```

## **CPU Frequency**

**[link](http://www.friendlyarm.net/forum/topic/6521)**

### **Default values**

cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

```
ondemand
```

cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed

```
<unsupported>
```

cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies

```
480000 648000 816000 960000 1008000 1104000 1200000 1296000 1368000
```

### **Set new value**

```
echo userspace > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo 800000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed
```

you can check current frequency

```
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
```

## **Commands**

```shell
# debug GPIO
cat /sys/kernel/debug/gpio

# Read CPU Temperature
echo $((`cat /sys/class/thermal/thermal_zone0/temp` / 1000))
```

## **Preparing**

```shell
git clone https://github.com/friendlyarm/WiringNP
cd WiringNP/
chmod 755 build
./build
```

check it works by `gpio readall`

## Examples

### **ds18b20**

```
git clone https://github.com/Jacajack/avr-ds18b20
```

## **Power Consumption**

Temperature measurements were taken outdoors on a table. It was 23-24 degrees in the room.

At a frequency of 1368000 and 4 cores loaded at 100% - 0.5 Ampere, the temperature reaches 80 degrees (I didn’t torture it any further)

At a frequency of 480000 and 4 cores loaded at 100% - 0.27 Ampere, the temperature reaches 60 degrees and grows very slowly (I didn’t wait)