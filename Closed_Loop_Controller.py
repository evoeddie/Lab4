import utime
import cqueue

class Controller:
    def __init__(self, kp, set_point, queue_size):
         self.kp = float(kp)
         self.set_point = float(set_point)
         #self.measured_output = 0
         self.time_value = cqueue.IntQueue(queue_size)
         self.position = cqueue.IntQueue(queue_size)
         self.start = utime.ticks_ms()
         

    def run(self, measured_output):
         #actuation value is Kp*(theta_set - enc2.read() value
         self.measured_output = measured_output
         err = self.set_point - self.measured_output
         actuation = self.kp*err
         current_time = utime.ticks_ms()
         #if not self.time_value.full():
         self.time_passed = utime.ticks_diff(current_time, self.start)
         self.time_value.put(self.time_passed)
         self.position.put(self.measured_output)
         #utime.sleep_ms(10) # does this go in main or control?
         return actuation
        
    def set_setpoint(self, desired_set_point):
        self.set_point = desired_set_point
        
    def set_Kp(self, desired_Kp):
        self.kp = desired_Kp
        
    def data(self):
         x = self.time_value
         y = self.position
         return (x, y)
        
    
  # call .get on each one of the queues  