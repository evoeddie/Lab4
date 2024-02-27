"""
Created on Fri Feb  9 13:40:38 2024
"""
import pyb
import time
from motor_driver import motordriver

class Encoder:
    """!
     This class represents an incremental encoder connected to our
     given microcontoller. Where we have the following attributes:
     
     enc_name : Is the name of the encoder
     pin1 (pyb.Pin): This pin is representing encoder channel A.
     
     pin2 (pyb.Pin): This pin is representing encoder channel B.
     
     Timer (pyb.Timer): The timer used for the encoder counting.
                        Using the manuel given for our board, we
                        set timer 4 and timer 8 for our encoders.
                        
     @author Alia Wolken, Eduardo Santos, Andrew Jwaideh
     """
    
    def __init__(self, enc_name, pin1, pin2, timer):
        """
        Here we initialize the Encoder Object. Where we have the
        following:
        
        enc_name: The name given to the encoder
        pin1 (int): The pin number for the first encoder channel.
        pin2 (int): The pin number for the second encoder channel.
        timer_num (int): The number of the timer to be used, in this
                         lab we combined both AB to the same timer.
        
        """   
        #initialize encoder pins
        self.pin1 = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.OUT_PP)
        
        #initialize encoder timer channels
        self.AR = int(0xFFFF)
        self.tim = pyb.Timer(timer, prescaler=0, period=self.AR) # period is AR, if just period w/out PS -> actual period in [s]
        self.ch1 = self.tim.channel(1, pyb.Timer.ENC_AB, pin=pin1) 
        self.ch2 = self.tim.channel(2, pyb.Timer.ENC_AB, pin=pin2)
        
        self.previous_counter_val = 0 # init previous counter value, starts at zero
        self.delta_summed = 0
        
       # print('init-ed')
        
    def read(self):
        """
         Reads the current count of the encoder.
         
         Returns:
         total delta value
        """
        # In the meantime
        # This code below returns both encoder vals
        self.current_counter_val = self.tim.counter()
        self.delta = self.current_counter_val - self.previous_counter_val
        
       # print('current counter val', self.current_counter_val)
       # print('prev counter val',self.previous_counter_val)
        #print('delta val', self.delta)
        
        if self.delta >= (self.AR+1)/2:
            self.delta -= self.AR # underflow
            
        elif self.delta <= -(self.AR+1)/2:
            self.delta += self.AR # overflow
        else:
            pass
        
        self.delta_summed += self.delta # keeps summing the deltas
        
        print('delta total',self.delta_summed)
        
        # save previous value
        self.previous_counter_val = self.current_counter_val
        
        return self.delta_summed
        

    def zero(self):
        """
         Resets the encoder back to zero.
         
         When it returns;
         
         int: The new count after resetting back to zero.
        """       
        self.tim.counter(0)
        

if __name__ == "__main__":

    enc1 = Encoder("enc1", pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
    enc2 = Encoder("enc2", pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
    
    #moe = motordriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    moe = motordriver (pyb.Pin.board.PC1, pyb.Pin.board.PA1, pyb.Pin.board.PA0, 5)
    count = 0
    
    # continues to read encoder values for testing until "Ctrl-C" is pressed
    while True:
        
        
        #not sure why these if stamements are here
        #would be advantages to keep reading the encoder while the motor is running
        
        try:
            if count <= 10: 
            # read encoder vals as turn manually
                enc1.read()
                print('------')
                enc2.read()
                print('count',count)
                print('------------------')
                time.sleep(0.1)
            
            elif count > 10 and count < 20:    
            # run motor and read encoder vals
                # init motor time channels init-ed in motor_driver class
                
                # Drive the motor
                moe.set_duty_cycle (50)
                
                enc1.read()
                print('------')
                enc2.read()
                print('count',count)
                print('------------------')
                time.sleep(0.1)
            
            elif count >= 20:
                # Drive the motor
                moe.set_duty_cycle (-50)
               
                enc1.read()
                print('------')
                enc2.read()
                print('count',count)
                print('------------------')
                time.sleep(0.1)
                if enc2.read() == 6000:
                    enc2.zero()
                    while True:
                        pass
            
            count += 1
            
        # Trying to catch the "Ctrl-C" keystroke to break out
        # of the program cleanly
        except KeyboardInterrupt:
            break
        