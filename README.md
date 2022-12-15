# PID-drone
Controlling the hovering of a crazyflie drone using PID with a Z-ranger.

I wanted to try control the hover height of a crazyflie drone myself through a PID controller.

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

![alt text](https://github.com/keatinl1/PID-drone/blob/master/images/ziegler.png)
<p align="center">
Figure 3
</p>

It is clear that using a tuning method is superior to blindly tuning.

<p align="center">
  <img src="http://some_place.com/image.pn](https://raw.githubusercontent.com/keatinl1/PID-drone/master/images/drone_gif.gif" />
</p>

