# PID-drone
Controlling the hovering of a crazyflie drone using PID with a Z-ranger.

Watch the GIF for a demo and scroll down for methodology 🚁

$~~~~~~~~~~$

## Demo

<p align="center">
  <img width="512" height="512"  src="https://raw.githubusercontent.com/keatinl1/PID-drone/master/images/drone.gif">
</p>

$~~~~~~~~~~$

## Explanation
I wanted to try control the hover height of a crazyflie drone with a PID controller.

I tried it myself firstly, just tuning randomly until I found something that somewhat worked, see figure 1.

![alt text](https://raw.githubusercontent.com/keatinl1/PID-drone/master/images/unguided_tuning.png)
<p align="center">
Figure 1
</p>

Then I followed the Ziegler-Nichols method, here is a link to a short video (https://www.youtube.com/watch?v=dTZnZZ4ZT7I).

I forced the system into oscillation by slowly increasing the proportional gain (while leaving integral and differential as zero). The gain which this happened at was K_p = 2.2. See figure 2 for the response of the system.

![alt text](https://raw.githubusercontent.com/keatinl1/PID-drone/master/images/kmax.png)
<p align="center">
Figure 2
</p>

Using the equations and taking K_u as 2.2 and P_u as 2.2 seconds. An estimate could be made at the gains.

This estimate was then refined and yielded the response in Figure 3 from the system.

![alt text](https://raw.githubusercontent.com/keatinl1/PID-Drone/master/images/ziegler.png)
<p align="center">
Figure 3
</p>

It is clear that using a tuning method is superior to blindly tuning.

$~~~~~~~~~~$

## A note on figure 3

When figure 3 is analysed, it appears as though there is destabilisation occuring after steady state was achieved. In future, the proportional gain should be reduced to avoid the controller overreacting to small error signals and destabilising the system. This action would also reduce overshoot but the trade off is that the rise time would increase.
