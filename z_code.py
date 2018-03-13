import ImageGrab, Image, ImageOps
import os
import time
import win32api, win32con

#sys.setrecursionlimit(100000)

#from numpy import *

# win32
def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
##    time.sleep(.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
##    print "Click."
##    time.sleep(.01)

def mousePos(cord=(0,0)):
	win32api.SetCursorPos(cord)

# CORDS
class Cord:
	# larger real picture for mouse movement and clicking
	#black_diamond = (390, 460)
	#fifty_coin = (280, 710)
	#one_hundred_coin = (340, 710)
	#five_hundred_coin = (400, 710)
	#clear_btn = (100,845)
	#spin_btn = (500,845)
	
	# smaller cropped picture (for reading image)
	#black_diamond = (385, 75)
	#fifty_coin = (270, 320)
	#one_hundred_coin = (390, 320)
	#five_hundred_coin = (410, 320)
	#clear_btn = (100,450)
	#spin_btn = (500,450)
	
	black_diamond = (395, 76)
	black_diamond_click = (300, 395)
	red_diamond = (495, 76)
	red_diamond_click = (400, 395)
	#fifty_coin = (270, 320)
	#one_hundred_coin = (390, 320)
	#five_hundred_coin = (410, 320)
	clear_btn = (50,675)
	spin_btn = (400,675)
 
def screenGrab():
	box = (0,400,800,900)
	im = ImageGrab.grab(box)
	im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
	return im
 
# GLOBALS
double_times = 1;

def main(double_times):
	time.sleep(2)
	screen = screenGrab()
	time.sleep(3)
	print screen.getpixel(Cord.red_diamond)
	
	#if screen.getpixel(Cord.black_diamond) != (0,0,0):
	if screen.getpixel(Cord.red_diamond) != (153,0,0):
		# we won! staring over
		print "STARTING OVER"
		time.sleep(1)
		double_times = 1
		mousePos(Cord.clear_btn)
		leftClick()
		time.sleep(1)
		mousePos(Cord.clear_btn)
		leftClick()
		time.sleep(1)
		mousePos(Cord.clear_btn)
		leftClick()
		time.sleep(1)
		playAgain(screen, 2)
		
	else:
		print "double times:"
		print double_times
		# we won so lets clear and play again
		double_times = (double_times * 2) + 1
		playAgain(screen, double_times)
		
def playAgain(screen, double_times):
	
	for x in xrange((double_times - 1)):
		print x
		mousePos(Cord.red_diamond_click)
		leftClick()
		time.sleep(.2)
		
	time.sleep(1)
	mousePos(Cord.spin_btn)
	leftClick()
	time.sleep(12)
	main(double_times)
	
if __name__ == '__main__':
    main(double_times)