import math
import time
import machine

# Configure PWM
pwm_pin = machine.Pin(15)  
pwm = machine.PWM(pwm_pin)
pwm.freq(1000) 

def sine_wave(amplitude, offset, frequency, sample_rate, duration):
    """
    Generator that yields PWM duty cycle values to approximate a sine wave.
    
    :param amplitude: Maximum amplitude of the sine wave (0-1023 for 10-bit PWM).
    :param offset: Vertical offset of the sine wave.
    :param frequency: Frequency of the sine wave in Hertz.
    :param sample_rate: Number of samples per second.
    :param duration: Duration of the sine wave in seconds.
    :yield: None, but sets the PWM duty cycle to approximate a sine wave.
    """ 
    num_samples = int(sample_rate * duration)
    for i in range(num_samples):
        t = i / sample_rate  # time in seconds
        value = offset + amplitude * math.sin(2 * math.pi * frequency * t)
        duty = int((value / (offset + amplitude)) * 65535)
        yield duty
        
# Parameters for the sine wave
sample_rate = 1000      # samples per second
duration = 2            # duration in seconds
amplitude = 1.0         # amplitude (0-1)
offset = 1.0            # offset to ensure all values are positive
frequency = 2           # sine wave frequency in hz

# Generate the sine wave using PWM
for duty in sine_wave(amplitude, offset, frequency, sample_rate, duration):
    pwm.duty_u16(duty)
    time.sleep(1 / sample_rate) # wait for the next sample interval