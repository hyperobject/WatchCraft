## Inspiration
For as long as PC games have been around, you have generally had two options for controlling them: a keyboard and mouse or a gamepad. Recently, control systems like the Microsoft Kinect have become increasingly popular, which inspired me to create a small-scale alternate control method for Minecraft.
## What it does
WatchCraft replaces keyboard and mouse input in Minecraft with a combination of a Leap Motion hand position and tilt tracking system, and a Pebble Time acting as extra input and a second screen.
## How I built it
I used pebble.js to build the watchapp, because of its WebSocket support. I used Python to interface with the Pebble and the Leap Motion, and to control Minecraft.
## How to run it
This is the fun part. ;) 
First, you need to create a new pebble.js app on [CloudPebble](http://cloudpebble.net) and copy the contents of app.js in this repository to app.js in CloudPebble. Next, find your IP address on the computer you'll be running the backend on (`ifconfig -a` on OS X and Linux, `ipconfig` for Windows IIRC). In CloudPebble, replace <your IP address here> with the IP you just found. Next, download the leapmotion.py and pebble.py files to your computer. You'll also need the Leap Motion Python library files (more information can be found on developer.leapmotion.com). Run `pip install PyUserInput` and `pip install tornado` in a terminal.  Next, open up another terminal window, and run `python pebble.py` and `python leapmotion.py` in two separate windows. If you open up the Pebble app now, it should display 'WatchCraft connected' on the Pebble's screen. Open up Minecraft and have fun! 
### Problems running the code?
File an issue and I'll see what I can do. I'm also trying to package this code up in a neater fashion (one python file, installable watchapp), but I haven't gotten around to that yet. Check here in a few weeks (or follow me on Twitter at [@technoboyIO](http://twitter.com/technoboyIO)) for progress updates. 
