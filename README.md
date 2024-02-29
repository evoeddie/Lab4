# Lab4: One Task is (almost) Never Enough

## Overview
For this lab, we will be making a real-time multitasking to control multiple motors simultaneously
using a closed-loop control. We will see how we can properly demonstrate the ability to schedule
tasks efficiently to still have proper control over multiple devices concurrently. 

We will then run our task on the motor with a flywheel while plotting the results to compare
step response, both at slow and slower rate to then compare the controller's performance.
Finally, we will make two tasks that run two motors under closed-loop control at the same time.


The following plots will be a function of time in ms vs position of encoder ticks.

![image](https://github.com/evoeddie/Lab4/assets/157066050/3e928d5e-cc20-4a41-af2d-8a17fa426b2b)
While looking at this first plot we analyzed one motor while changing Kp values and task time.
Doing this gave us the following plot. Where we saw our motor to be most precise while having
a task time of 10ms and a Kp value of 0.03. The following line shows our motor running at a 
task time of 25ms with the same Kp value. We can see that there is hardly any oscillation in
our motor. Finally, while setting our task time to 25ms and a Kp of 0.09 we see that at this
point the motor is away for too long causing our plot and the motor to have tons of 
oscillation.




![image](https://github.com/evoeddie/Lab4/assets/157066050/7d2729fd-2002-4f26-a57a-e06b2834160a)
Using the same results we had for the first plot and comparing the system when two motors are 
connected. We can see that it takes a longer time to reach our position and we also can see that
the second motor doesn't oscillate as much as our first motor did while having a task time of 25ms and a Kp of 0.03.


Looking at these results we can conclude that when adding more components to our system we can 
expect to reduce our task time so that our controller can go check on other tasks while trying
to also keep precision at an optimal range.

