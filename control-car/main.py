from machine import Pin, PWM
import utime

# Khởi tạo PWM cho module L9110
A_IA = PWM(Pin(5))
A_IB = PWM(Pin(4)) 
B_IA = PWM(Pin(3))
B_IB = PWM(Pin(2))

# Cấu hình tần số PWM
A_IA.freq(2000)
A_IB.freq(2000)
B_IA.freq(2000)
B_IB.freq(2000)

# Hàm điều khiển động cơ
def move_forward(speed=45000):
    A_IA.duty_u16(speed)
    A_IB.duty_u16(0)
    B_IA.duty_u16(speed)
    B_IB.duty_u16(0)

def move_backward(speed=45000):
    A_IA.duty_u16(0)
    A_IB.duty_u16(speed)
    B_IA.duty_u16(0)
    B_IB.duty_u16(speed)

def stop():
    A_IA.duty_u16(0)
    A_IB.duty_u16(0)
    B_IA.duty_u16(0)
    B_IB.duty_u16(0)

# Chạy thử tiến 3 giây, lùi 3 giây, rồi dừng
while True:
    move_forward(45000)
    utime.sleep(3)
    
    move_backward(45000)              
    utime.sleep(3)
    
    stop()
    utime.sleep(1)