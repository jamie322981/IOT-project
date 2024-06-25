from machine import Pin, ADC
tmp36 = Pin(34, Pin.IN)
adc = ADC(tmp36)
prop = 1100 / 65535
v_out = adc.read_u16() * prop
temp = (v_out - 500) / 10
print(temp)