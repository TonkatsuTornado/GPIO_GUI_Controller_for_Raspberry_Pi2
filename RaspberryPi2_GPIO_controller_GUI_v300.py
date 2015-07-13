#
# GPIO GUI Contoroller for Raspberry Pi 2
# Ver.3.0
#
# 2015/July/9
# T2: Tonkatsu Tornado
#
#
######################################
############ CHANGE LOG ##############
######################################
#Ver.3.0
# - Keybord shotcuts are available.
#   Please see the Table below.
#
# - Active button indication is available.
#   The button of GPIO-High state becomes Red color.
#
######################################
#Ver.2.0 
# Finally, "Momentary mode" is UNVEILED!!!!
# 
#
######################################
#Ver.1.0 the First Release
#
# Beacuse Of my burnout,
# "Momentary mode" function is disabled in this
#  version... sorry sir...
#
######################################



########## Keybord Shortcuts #########
#
#IO21	a		IO26	q
#IO20	s		IO19	w
#IO16	d		IO13	e
#IO12	f		IO6		r
#IO7	g		IO5		t
#IO8	h		IO11	y
#IO25	j		IO9		u
#IO24	k		IO10	i
#IO23	l		IO22	o		
#IO18	b		IO27	p
#IO15	n		IO17	@
#IO14	m		IO4		7
#				IO3		8
#				IO2		9	
#
# Mode change: Shift + each key
#			
#######################################





#======================================
#======================================
#!/usr/bin/env python
# -*- coding: utf8 -*-#
import Tkinter
import RPi.GPIO as GPIO
import time
import sys


#=========variables declaring===========

GPIO_BCM_channels = 	[2,3,4,17,27,22,10,9,11,5,6,13,19,26,
			21,20,16,12,7,8,25,24,23,18,15,14]
GPIO_BCM_ONOFFflag = [0] * 30 #0=off, 1= on
toggle_flag = False;

GPIO_BCM_modeflag = [1] * 30 #0 = M mode, 1 = A mode

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_BCM_channels, GPIO.OUT)

RB = [1] * 30		#RadioButton's states.  #0 = M mode marked, 1 = A mode marked

Button = [0] * 30


#=======================================


#===============FUNCTIONS==================
def LED_ON_ALL():
	GPIO.output(GPIO_BCM_channels, True)
	return 0;

def LED_OFF_ALL():
	GPIO.output(GPIO_BCM_channels, False)
	return 0;

def Mode_select(channel, flag):
	GPIO_BCM_modeflag[channel] = flag  # 0 = M mode, 1 = A mode 
	return 0;

def Mode_select_by_keyboard(channel): # 0 = M mode, 1 = A mode
	
	if RB[channel].get() == 0:
		RB[channel].set(1) 
		GPIO_BCM_modeflag[channel] = 1 # 1 = A mode
	elif RB[channel].get() ==1: 
		RB[channel].set(0)
		GPIO_BCM_modeflag[channel] = 0 # 0 = M mode
		
	return 0;


def Toggle_LED(channel):

	if GPIO_BCM_modeflag[channel] == 0: # M mode
		GPIO.output(channel, True)
		Button[channel].configure(relief = 'sunken' )
		Button[channel].configure(background = 'red')

	else: # A mode
		GPIO_BCM_ONOFFflag[channel] =  (not GPIO_BCM_ONOFFflag[channel])
		toggle_flag = GPIO_BCM_ONOFFflag[channel]
		if toggle_flag == 0:
			GPIO.output(channel, False)
			Button[channel].configure(relief = 'raised' )
			Button[channel].configure(background = 'lightgray')

		else: 	
			GPIO.output(channel, True)	
			Button[channel].configure(relief = 'sunken' )
			Button[channel].configure(background = 'red')

	return 0;


def Button_released(channel): #for M mode, this func will turned OFF the LED by releasing the Button.

	if GPIO_BCM_modeflag[channel] == 0: # M mode only
		GPIO.output(channel, False)
		Button[channel].configure(relief = 'raised' )
		Button[channel].configure(background = 'lightgray')


	return 0;



def init(): #initializing function
	LED_OFF_ALL()
	toggle_flag = False
	return 0;


def finalize():#Finalize function (this will be called when EXIT button is pressed. )
	LED_OFF_ALL()
	GPIO.cleanup()
	sys.exit()

#=========================================

 
#===========Initialize===============
init()

#=====================================

#=========GUI===========================
root = Tkinter.Tk()
root.title(u"Raspberry Pi 2 GPIO Controller")
root.geometry("1024x380")

x_origin = 60;
y_origin = 20;

x_origin_lower = 10;
y_origin_lower = 200;

x_space = 50;
y_space = 30;


#=======================================
#==========Buttons===================

#----------GPIO26------------------
RB[26] = Tkinter.IntVar()
RB[26].set(1) 

RadioButton26_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[26], value = 0, command = lambda : Mode_select(26, RB[26].get() ))
RadioButton26_M.place(x = x_origin, y = y_origin + y_space)

RadioButton26_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[26], value = 1, command = lambda : Mode_select(26, RB[26].get() ))
RadioButton26_A.place(x = x_origin, y = y_origin + y_space * 2)

Button[26] = Tkinter.Button(root, text=u'26', background = 'lightgray'  )
Button[26].bind("<ButtonPress-1>", lambda X : Toggle_LED(26) )
Button[26].bind("<ButtonRelease-1>",  lambda X : Button_released(26)  )
root.bind("<KeyPress-q>", lambda X : Toggle_LED(26) )
root.bind("<KeyRelease-q>",  lambda X : Button_released(26)  )
root.bind("<KeyPress-Q>", lambda X : Mode_select_by_keyboard(26) )
Button[26].place(x= x_origin, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO19------------------
RB[19] = Tkinter.IntVar()
RB[19].set(1) 

RadioButton19_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[19], value = 0, command = lambda : Mode_select(19, RB[19].get() ))
RadioButton19_M.place(x = x_origin + x_space, y = y_origin + y_space)

RadioButton19_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[19], value = 1, command = lambda : Mode_select(19, RB[19].get() ))
RadioButton19_A.place(x = x_origin + x_space, y = y_origin + y_space * 2)

Button[19] = Tkinter.Button(root, text=u'19' , background = 'lightgray')
Button[19].bind("<ButtonPress-1>", lambda X : Toggle_LED(19) )
Button[19].bind("ButtonRelease-1>",  lambda X : Button_released(19)  )
root.bind("<KeyPress-w>", lambda X : Toggle_LED(19) )
root.bind("<KeyRelease-w>",  lambda X : Button_released(19)  )
root.bind("<KeyPress-W>", lambda X : Mode_select_by_keyboard(19) )
Button[19].place(x = x_origin + x_space, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO13------------------
RB[13] = Tkinter.IntVar()
RB[13].set(1) 

RadioButton13_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[13], value = 0, command = lambda : Mode_select(13, RB[13].get() ))
RadioButton13_M.place(x = x_origin + x_space * 2, y = y_origin + y_space)

RadioButton13_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[13], value = 1, command = lambda : Mode_select(13, RB[13].get() ))
RadioButton13_A.place(x = x_origin + x_space * 2, y = y_origin + y_space * 2)

Button[13] = Tkinter.Button(root, text=u'13' , background = 'lightgray')
Button[13].bind("<ButtonPress-1>", lambda X : Toggle_LED(13) )
Button[13].bind("<ButtonRelease-1>",  lambda X : Button_released(13)  )
root.bind("<KeyPress-e>", lambda X : Toggle_LED(13) )
root.bind("<KeyRelease-e>",  lambda X : Button_released(13)  )
root.bind("<KeyPress-E>", lambda X : Mode_select_by_keyboard(13) )
Button[13].place(x = x_origin + x_space * 2, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO6------------------
RB[6] = Tkinter.IntVar()
RB[6].set(1) 

RadioButton6_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[6], value = 0, command = lambda : Mode_select([6], RB6.get() ))
RadioButton6_M.place(x = x_origin + x_space * 3, y = y_origin + y_space)

RadioButton6_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[6], value = 1, command = lambda : Mode_select([6], RB6.get() ))
RadioButton6_A.place(x = x_origin + x_space * 3, y = y_origin + y_space * 2)

Button[6] = Tkinter.Button(root, text=u'6' , background = 'lightgray')
Button[6].bind("<ButtonPress-1>", lambda X : Toggle_LED(6) )
Button[6].bind("<ButtonRelease-1>",  lambda X : Button_released(6)  )
root.bind("<KeyPress-r>", lambda X : Toggle_LED(6) )
root.bind("<KeyRelease-r>",  lambda X : Button_released(6)  )
root.bind("<KeyPress-R>", lambda X : Mode_select_by_keyboard(6) )
Button[6].place(x = x_origin + x_space * 3, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO5------------------
RB[5] = Tkinter.IntVar()
RB[5].set(1) 

RadioButton5_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[5], value = 0, command = lambda : Mode_select(5, RB[5].get() ))
RadioButton5_M.place(x = x_origin + x_space * 4, y = y_origin + y_space)

RadioButton5_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[5], value = 1, command = lambda : Mode_select(5, RB[5].get() ))
RadioButton5_A.place(x = x_origin + x_space * 4, y = y_origin + y_space * 2)

Button[5] = Tkinter.Button(root, text=u'5' , background = 'lightgray')
Button[5].bind("<ButtonPress-1>", lambda X : Toggle_LED(5) )
Button[5].bind("<ButtonRelease-1>",  lambda X : Button_released(5)  )
root.bind("<KeyPress-t>", lambda X : Toggle_LED(5) )
root.bind("<KeyRelease-t>",  lambda X : Button_released(5)  )
root.bind("<KeyPress-T>", lambda X : Mode_select_by_keyboard(5) )
Button[5].place(x = x_origin + x_space * 4, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO11------------------
RB[11] = Tkinter.IntVar()
RB[11].set(1) 

RadioButton11_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[11], value = 0, command = lambda : Mode_select(11, RB[11].get() ))
RadioButton11_M.place(x = x_origin + x_space * 7, y = y_origin + y_space)

RadioButton11_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[11], value = 1, command = lambda : Mode_select(11, RB[11].get() ))
RadioButton11_A.place(x = x_origin + x_space * 7, y = y_origin + y_space * 2)

Button[11] = Tkinter.Button(root, text=u'11' , background = 'lightgray')
Button[11].bind("<ButtonPress-1>", lambda X : Toggle_LED(11) )
Button[11].bind("<ButtonRelease-1>",  lambda X : Button_released(11)  )
root.bind("<KeyPress-y>", lambda X : Toggle_LED(11) )
root.bind("<KeyRelease-y>",  lambda X : Button_released(11)  )
root.bind("<KeyPress-Y>", lambda X : Mode_select_by_keyboard(11) )
Button[11].place(x = x_origin + x_space * 7, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO9------------------
RB[9] = Tkinter.IntVar()
RB[9].set(1) 

RadioButton9_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[9], value = 0, command = lambda : Mode_select(9, RB[9].get() ))
RadioButton9_M.place(x = x_origin + x_space * 8, y = y_origin + y_space)

RadioButton9_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[9], value = 1, command = lambda : Mode_select(9, RB[9].get() ))
RadioButton9_A.place(x = x_origin + x_space * 8, y = y_origin + y_space * 2)

Button[9] = Tkinter.Button(root, text=u'9' , background = 'lightgray')
Button[9].bind("<ButtonPress-1>", lambda X : Toggle_LED(9) )
Button[9].bind("<ButtonRelease-1>",  lambda X : Button_released(9)  )
root.bind("<KeyPress-u>", lambda X : Toggle_LED(9) )
root.bind("<KeyRelease-u>",  lambda X : Button_released(9)  )
root.bind("<KeyPress-U>", lambda X : Mode_select_by_keyboard(9) )
Button[9].place(x = x_origin + x_space * 8, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPI10------------------
RB[10] = Tkinter.IntVar()
RB[10].set(1) 

RadioButton10_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[10], value = 0, command = lambda : Mode_select(10, RB[10].get() ))
RadioButton10_M.place(x = x_origin + x_space * 9, y = y_origin + y_space)

RadioButton10_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[10], value = 1, command = lambda : Mode_select(10, RB[10].get() ))
RadioButton10_A.place(x = x_origin + x_space * 9, y = y_origin + y_space * 2)

Button[10] = Tkinter.Button(root, text=u'10' , background = 'lightgray')
Button[10].bind("<ButtonPress-1>", lambda X : Toggle_LED(10) )
Button[10].bind("<ButtonRelease-1>",  lambda X : Button_released(10)  )
root.bind("<KeyPress-i>", lambda X : Toggle_LED(10) )
root.bind("<KeyRelease-i>",  lambda X : Button_released(10)  )
root.bind("<KeyPress-I>", lambda X : Mode_select_by_keyboard(10) )
Button[10].place(x = x_origin + x_space * 9, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO22------------------
RB[22] = Tkinter.IntVar()
RB[22].set(1) 

RadioButton22_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[22], value = 0, command = lambda : Mode_select(22, RB[22].get() ))
RadioButton22_M.place(x = x_origin + x_space * 11, y = y_origin + y_space)

RadioButton22_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[22], value = 1, command = lambda : Mode_select(22, RB[22].get() ))
RadioButton22_A.place(x = x_origin + x_space * 11, y = y_origin + y_space * 2)

Button[22] = Tkinter.Button(root, text=u'22' , background = 'lightgray')
Button[22].bind("<ButtonPress-1>", lambda X : Toggle_LED(22) )
Button[22].bind("<ButtonRelease-1>",  lambda X : Button_released(22)  )
root.bind("<KeyPress-o>", lambda X : Toggle_LED(22) )
root.bind("<KeyRelease-o>",  lambda X : Button_released(22)  )
root.bind("<KeyPress-O>", lambda X : Mode_select_by_keyboard(22) )
Button[22].place(x = x_origin + x_space * 11, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO27------------------
RB[27] = Tkinter.IntVar()
RB[27].set(1) 
RadioButton27_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[27], value = 0, command = lambda : Mode_select(27, RB[27].get() ))
RadioButton27_M.place(x = x_origin + x_space * 12, y = y_origin + y_space)

RadioButton27_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[27], value = 1, command = lambda : Mode_select(27, RB[27].get() ))
RadioButton27_A.place(x = x_origin + x_space * 12, y = y_origin + y_space * 2)

Button[27] = Tkinter.Button(root, text=u'27' , background = 'lightgray')
Button[27].bind("<ButtonPress-1>", lambda X : Toggle_LED(27) )
Button[27].bind("<ButtonRelease-1>",  lambda X : Button_released(27)  )
root.bind("<KeyPress-p>", lambda X : Toggle_LED(27) )
root.bind("<KeyRelease-p>",  lambda X : Button_released(27)  )
root.bind("<KeyPress-P>", lambda X : Mode_select_by_keyboard(27) )
Button[27].place(x = x_origin + x_space * 12, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO17------------------
RB[17] = Tkinter.IntVar()
RB[17].set(1) 

RadioButton17_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[17], value = 0, command = lambda : Mode_select(17, RB[17].get() ))
RadioButton17_M.place(x = x_origin + x_space * 13, y = y_origin + y_space)

RadioButton17_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[17], value = 1, command = lambda : Mode_select(17, RB[17].get() ))
RadioButton17_A.place(x = x_origin + x_space * 13, y = y_origin + y_space * 2)

Button[17] = Tkinter.Button(root, text=u'17' , background = 'lightgray')
Button[17].bind("<ButtonPress-1>", lambda X : Toggle_LED(17) )
Button[17].bind("<ButtonRelease-1>",  lambda X : Button_released(17)  )
root.bind("<KeyPress-at>", lambda X : Toggle_LED(17) )				# at means @
root.bind("<KeyRelease-at>",  lambda X : Button_released(17)  )		# at means @
root.bind("<quoteleft>", lambda X : Mode_select_by_keyboard(17) ) 	# Shift + @ = ` <-quoteleft
Button[17].place(x = x_origin + x_space * 13, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO4------------------
RB[4] = Tkinter.IntVar()
RB[4].set(1) 

RadioButton4_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[4], value = 0, command = lambda : Mode_select(4, RB[4].get() ))
RadioButton4_M.place(x = x_origin + x_space * 15, y = y_origin + y_space)

RadioButton4_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[4], value = 1, command = lambda : Mode_select(4, RB[4].get() ))
RadioButton4_A.place(x = x_origin + x_space * 15, y = y_origin + y_space * 2)

Button[4] = Tkinter.Button(root, text=u'4' , background = 'lightgray')
Button[4].bind("<ButtonPress-1>", lambda X : Toggle_LED(4) )
Button[4].bind("<ButtonRelease-1>",  lambda X : Button_released(4)  )
root.bind("<KeyPress-7>", lambda X : Toggle_LED(4) )
root.bind("<KeyRelease-7>",  lambda X : Button_released(4)  )
root.bind("<quoteright>", lambda X : Mode_select_by_keyboard(4) )	# Shift + 7 = ' <-quoteright
Button[4].place(x = x_origin + x_space * 15, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO3------------------
RB[3] = Tkinter.IntVar()
RB[3].set(1) 

RadioButton3_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[3], value = 0, command = lambda : Mode_select(3, RB[3].get() ))
RadioButton3_M.place(x = x_origin + x_space * 16, y = y_origin + y_space)

RadioButton3_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[3], value = 1, command = lambda : Mode_select(3, RB[3].get() ))
RadioButton3_A.place(x = x_origin + x_space * 16, y = y_origin + y_space * 2)

Button[3] = Tkinter.Button(root, text=u'3' , background = 'lightgray')
Button[3].bind("<ButtonPress-1>", lambda X : Toggle_LED(3) )
Button[3].bind("<ButtonRelease-1>",  lambda X : Button_released(3)  )
root.bind("<KeyPress-8>", lambda X : Toggle_LED(3) )
root.bind("<KeyRelease-8>",  lambda X : Button_released(3)  )
root.bind("<parenleft>", lambda X : Mode_select_by_keyboard(3) )	# Shift + 8 = ( <-parenleft
Button[3].place(x = x_origin + x_space * 16, y= y_origin + y_space * 3)
#-----------------------------------
#----------GPIO2------------------
RB[2] = Tkinter.IntVar()
RB[2].set(1) 

RadioButton2_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[2], value = 0, command = lambda : Mode_select(2, RB[2].get() ))
RadioButton2_M.place(x = x_origin + x_space * 17, y = y_origin + y_space)

RadioButton2_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[2], value = 1, command = lambda : Mode_select(2, RB[2].get() ))
RadioButton2_A.place(x = x_origin + x_space * 17, y = y_origin + y_space * 2)

Button[2] = Tkinter.Button(root, text=u'2' , background = 'lightgray')
Button[2].bind("<ButtonPress-1>", lambda X : Toggle_LED(2) )
Button[2].bind("<ButtonRelease-1>",  lambda X : Button_released(2)  )
root.bind("<KeyPress-9>", lambda X : Toggle_LED(2) )
root.bind("<KeyRelease-9>",  lambda X : Button_released(2)  )
root.bind("<parenright>", lambda X : Mode_select_by_keyboard(2) )	# Shift + 9 = ) <-parenright
Button[2].place(x = x_origin + x_space * 17, y= y_origin + y_space * 3)
#-----------------------------------
#########################################################################
#########################################################################
#----------GPIO21------------------
RB[21] = Tkinter.IntVar()
RB[21].set(1) 

Button[21] = Tkinter.Button(root, text=u'21' , background = 'lightgray' )
Button[21].bind("<ButtonPress-1>", lambda X : Toggle_LED(21) )
Button[21].bind("<ButtonRelease-1>",  lambda X : Button_released(21)  )
root.bind("<KeyPress-a>", lambda X : Toggle_LED(21) )
root.bind("<KeyRelease-a>",  lambda X : Button_released(21)  )
root.bind("<KeyPress-A>", lambda X : Mode_select_by_keyboard(21) )
Button[21].place(x=x_origin_lower, y= y_origin_lower + y_space)

RadioButton21_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[21], value = 1, command = lambda : Mode_select(21, RB[21].get() ))
RadioButton21_A.place(x = x_origin_lower, y = y_origin_lower + y_space * 2)

RadioButton21_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[21], value = 0, command = lambda : Mode_select(21, RB[21].get() ))
RadioButton21_M.place(x = x_origin_lower, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO20------------------
RB[20] = Tkinter.IntVar()
RB[20].set(1) 

Button[20] = Tkinter.Button(root, text=u'20'  , background = 'lightgray')
Button[20].bind("<ButtonPress-1>", lambda X : Toggle_LED(20) )
Button[20].bind("<ButtonRelease-1>",  lambda X : Button_released(20)  )
root.bind("<KeyPress-s>", lambda X : Toggle_LED(20) )
root.bind("<KeyRelease-s>",  lambda X : Button_released(20)  )
root.bind("<KeyPress-S>", lambda X : Mode_select_by_keyboard(20) )
Button[20].place(x=x_origin_lower + x_space, y= y_origin_lower + y_space)

RadioButton20_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[20], value = 1, command = lambda : Mode_select(20, RB[20].get() ))
RadioButton20_A.place(x = x_origin_lower + x_space, y = y_origin_lower + y_space * 2)

RadioButton20_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[20], value = 0, command = lambda : Mode_select(20, RB[20].get() ))
RadioButton20_M.place(x = x_origin_lower + x_space, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO16------------------
RB[16] = Tkinter.IntVar()
RB[16].set(1) 

Button[16] = Tkinter.Button(root, text=u'16' , background = 'lightgray')
Button[16].bind("<ButtonPress-1>", lambda X : Toggle_LED(16) )
Button[16].bind("<ButtonRelease-1>",  lambda X : Button_released(16)  )
root.bind("<KeyPress-d>", lambda X : Toggle_LED(16) )
root.bind("<KeyRelease-d>",  lambda X : Button_released(16)  )
root.bind("<KeyPress-D>", lambda X : Mode_select_by_keyboard(16) )
Button[16].place(x=x_origin_lower + x_space * 2, y= y_origin_lower + y_space)

RadioButton16_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[16], value = 1, command = lambda : Mode_select(16, RB[16].get() ))
RadioButton16_A.place(x = x_origin_lower + x_space * 2, y = y_origin_lower + y_space * 2)

RadioButton16_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[16], value = 0, command = lambda : Mode_select(16, RB[16].get() ))
RadioButton16_M.place(x = x_origin_lower + x_space * 2, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO12------------------
RB[12] = Tkinter.IntVar()
RB[12].set(1) 

Button[12] = Tkinter.Button(root, text=u'12' , background = 'lightgray')
Button[12].bind("<ButtonPress-1>", lambda X : Toggle_LED(12) )
Button[12].bind("<ButtonRelease-1>",  lambda X : Button_released(12)  )
root.bind("<KeyPress-f>", lambda X : Toggle_LED(12) )
root.bind("<KeyRelease-f>",  lambda X : Button_released(12)  )
root.bind("<KeyPress-F>", lambda X : Mode_select_by_keyboard(12) )
Button[12].place(x=x_origin_lower + x_space * 4, y= y_origin_lower + y_space)

RadioButton12_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[12], value = 1, command = lambda : Mode_select(12, RB[12].get() ))
RadioButton12_A.place(x = x_origin_lower + x_space * 4, y = y_origin_lower + y_space * 2)

RadioButton12_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[12], value = 0, command = lambda : Mode_select(12, RB[12].get() ))
RadioButton12_M.place(x = x_origin_lower + x_space * 4, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO7------------------
RB[7] = Tkinter.IntVar()
RB[7].set(1) 

Button[7] = Tkinter.Button(root, text=u'7' , background = 'lightgray')
Button[7].bind("<ButtonPress-1>", lambda X : Toggle_LED(7) )
Button[7].bind("<ButtonRelease-1>",  lambda X : Button_released(7)  )
root.bind("<KeyPress-g>", lambda X : Toggle_LED(7) )
root.bind("<KeyRelease-g>",  lambda X : Button_released(7)  )
root.bind("<KeyPress-G>", lambda X : Mode_select_by_keyboard(7) )
Button[7].place(x=x_origin_lower + x_space * 7, y= y_origin_lower + y_space)

RadioButton7_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[7], value = 1, command = lambda : Mode_select(7, RB[7].get() ))
RadioButton7_A.place(x = x_origin_lower + x_space * 7, y = y_origin_lower + y_space * 2)

RadioButton7_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[7], value = 0, command = lambda : Mode_select(7, RB[7].get() ))
RadioButton7_M.place(x = x_origin_lower + x_space * 7, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO8------------------
RB[8] = Tkinter.IntVar()
RB[8].set(1) 

Button[8] = Tkinter.Button(root, text=u'8' , background = 'lightgray')
Button[8].bind("<ButtonPress-1>", lambda X : Toggle_LED(8) )
Button[8].bind("<ButtonRelease-1>",  lambda X : Button_released(8)  )
root.bind("<KeyPress-h>", lambda X : Toggle_LED(8) )
root.bind("<KeyRelease-h>",  lambda X : Button_released(8)  )
root.bind("<KeyPress-H>", lambda X : Mode_select_by_keyboard(8) )
Button[8].place(x=x_origin_lower + x_space * 8, y= y_origin_lower + y_space)

RadioButton8_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[8], value = 1, command = lambda : Mode_select(8, RB[8].get() ))
RadioButton8_A.place(x = x_origin_lower + x_space * 8, y = y_origin_lower + y_space * 2)

RadioButton8_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[8], value = 0, command = lambda : Mode_select(8, RB[8].get() ))
RadioButton8_M.place(x = x_origin_lower + x_space * 8, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO25------------------
RB[25] = Tkinter.IntVar()
RB[25].set(1) 

Button[25] = Tkinter.Button(root, text=u'25', background = 'lightgray' )
Button[25].bind("<ButtonPress-1>", lambda X : Toggle_LED(25) )
Button[25].bind("<ButtonRelease-1>",  lambda X : Button_released(25)  )
root.bind("<KeyPress-j>", lambda X : Toggle_LED(25) )
root.bind("<KeyRelease-j>",  lambda X : Button_released(25)  )
root.bind("<KeyPress-J>", lambda X : Mode_select_by_keyboard(25) )
Button[25].place(x=x_origin_lower + x_space * 9, y= y_origin_lower + y_space)

RadioButton25_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[25], value = 1, command = lambda : Mode_select(25, RB[25].get() ))
RadioButton25_A.place(x = x_origin_lower + x_space * 9, y = y_origin_lower + y_space * 2)

RadioButton25_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[25], value = 0, command = lambda : Mode_select(25, RB[25].get() ))
RadioButton25_M.place(x = x_origin_lower + x_space * 9, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO24------------------
RB[24] = Tkinter.IntVar()
RB[24].set(1) 

Button[24] = Tkinter.Button(root, text=u'24' , background = 'lightgray')
Button[24].bind("<ButtonPress-1>", lambda X : Toggle_LED(24) )
Button[24].bind("<ButtonRelease-1>",  lambda X : Button_released(24)  )
root.bind("<KeyPress-k>", lambda X : Toggle_LED(24) )
root.bind("<KeyRelease-k>",  lambda X : Button_released(24)  )
root.bind("<KeyPress-K>", lambda X : Mode_select_by_keyboard(24) )
Button[24].place(x=x_origin_lower + x_space * 11, y= y_origin_lower + y_space)

RadioButton24_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[24], value = 1, command = lambda : Mode_select(24, RB[24].get() ))
RadioButton24_A.place(x = x_origin_lower + x_space * 11, y = y_origin_lower + y_space * 2)

RadioButton24_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[24], value = 0, command = lambda : Mode_select(24, RB[24].get() ))
RadioButton24_M.place(x = x_origin_lower + x_space * 11, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO23------------------
RB[23] = Tkinter.IntVar()
RB[23].set(1) 

Button[23] = Tkinter.Button(root, text=u'23' , background = 'lightgray')
Button[23].bind("<ButtonPress-1>", lambda X : Toggle_LED(23) )
Button[23].bind("<ButtonRelease-1>",  lambda X : Button_released(23)  )
root.bind("<KeyPress-l>", lambda X : Toggle_LED(23) )
root.bind("<KeyRelease-l>",  lambda X : Button_released(23)  )
root.bind("<KeyPress-L>", lambda X : Mode_select_by_keyboard(23) )
Button[23].place(x=x_origin_lower + x_space * 12, y= y_origin_lower + y_space)

RadioButton23_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[23], value = 1, command = lambda : Mode_select(23, RB[23].get() ))
RadioButton23_A.place(x = x_origin_lower + x_space * 12, y = y_origin_lower + y_space * 2)

RadioButton23_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[23], value = 0, command = lambda : Mode_select(23, RB[23].get() ))
RadioButton23_M.place(x = x_origin_lower + x_space * 12, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO18------------------
RB[18] = Tkinter.IntVar()
RB[18].set(1) 

Button[18] = Tkinter.Button(root, text=u'18' , background = 'lightgray')
Button[18].bind("<ButtonPress-1>", lambda X : Toggle_LED(18) )
Button[18].bind("<ButtonRelease-1>",  lambda X : Button_released(18)  )
root.bind("<KeyPress-b>", lambda X : Toggle_LED(18) )
root.bind("<KeyRelease-b>",  lambda X : Button_released(18)  )
root.bind("<KeyPress-B>", lambda X : Mode_select_by_keyboard(18) )
Button[18].place(x=x_origin_lower + x_space * 14, y= y_origin_lower + y_space)

RadioButton18_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[18], value = 1, command = lambda : Mode_select(18, RB[18].get() ))
RadioButton18_A.place(x = x_origin_lower + x_space * 14, y = y_origin_lower + y_space * 2)

RadioButton18_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[18], value = 0, command = lambda : Mode_select(18, RB[18].get() ))
RadioButton18_M.place(x = x_origin_lower + x_space * 14, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO15------------------
RB[15] = Tkinter.IntVar()
RB[15].set(1) 

Button[15] = Tkinter.Button(root, text=u'15' , background = 'lightgray')
Button[15].bind("<ButtonPress-1>", lambda X : Toggle_LED(15) )
Button[15].bind("<ButtonRelease-1>",  lambda X : Button_released(15)  )
root.bind("<KeyPress-n>", lambda X : Toggle_LED(15) )
root.bind("<KeyRelease-n>",  lambda X : Button_released(15)  )
root.bind("<KeyPress-N>", lambda X : Mode_select_by_keyboard(15) )
Button[15].place(x=x_origin_lower + x_space * 15, y= y_origin_lower + y_space)

RadioButton15_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[15], value = 1, command = lambda : Mode_select(15, RB[15].get() ))
RadioButton15_A.place(x = x_origin_lower + x_space * 15, y = y_origin_lower + y_space * 2)

RadioButton15_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[15], value = 0, command = lambda : Mode_select(15, RB[15].get() ))
RadioButton15_M.place(x = x_origin_lower + x_space * 15, y = y_origin_lower + y_space * 3)
#-----------------------------------
#----------GPIO14------------------
RB[14] = Tkinter.IntVar()
RB[14].set(1) 

Button[14] = Tkinter.Button(root, text=u'14' , background = 'lightgray')
Button[14].bind("<ButtonPress-1>", lambda X : Toggle_LED(14) )
Button[14].bind("<ButtonRelease-1>",  lambda X : Button_released(14)  )
root.bind("<KeyPress-m>", lambda X : Toggle_LED(14) )
root.bind("<KeyRelease-m>",  lambda X : Button_released(14)  )
root.bind("<KeyPress-M>", lambda X : Mode_select_by_keyboard(14) )
Button[14].place(x=x_origin_lower + x_space * 16, y= y_origin_lower + y_space)

RadioButton14_A = Tkinter.Radiobutton(root, text=u"A", variable = RB[14], value = 1, command = lambda : Mode_select(14, RB[14].get() ))
RadioButton14_A.place(x = x_origin_lower + x_space * 16, y = y_origin_lower + y_space * 2)

RadioButton14_M = Tkinter.Radiobutton(root, text=u"M", variable = RB[14], value = 0, command = lambda : Mode_select(14, RB[14].get() ))
RadioButton14_M.place(x = x_origin_lower + x_space * 16, y = y_origin_lower + y_space * 3)
#-----------------------------------
#-------------------------------------
########################################################################
#########################################################################
#------------EXIT Button-----------
Button_Exit = Tkinter.Button(root, text=u'EXIT', width = 5, height = 5, command = finalize)
root.bind("<Escape>", lambda X :finalize() )
Button_Exit.place(x = 900, y = 250)
#-------------------------------------
#########################################################################
#########################################################################
#----------Credit and Discriptions------
program_title = Tkinter.StringVar()
program_title.set("GPIO GUI Controller for Raspberry Pi 2")
lable_program_title = Tkinter.Label(root, textvariable = program_title, font=('ArialBold', 24))
lable_program_title.place(x = 220, y = 140)

program_ver = Tkinter.StringVar()
program_ver.set("ver.3.0")
lable_program_ver = Tkinter.Label(root, textvariable = program_ver)
lable_program_ver.place(x = 820, y = 180)

discription_M = Tkinter.StringVar()
discription_M.set("M: Momentary mode")
lable_discription_M = Tkinter.Label(root, textvariable = discription_M, font=('Arial', 12))
lable_discription_M.place(x = 230, y = 190)

discription_A = Tkinter.StringVar()
discription_A.set("A: Alternate mode")
lable_discription_A = Tkinter.Label(root, textvariable = discription_A, font=('Arial', 12))
lable_discription_A.place(x = 400, y = 190)

company_credit = Tkinter.StringVar()
company_credit.set("T2: Tonkatsu Tornado")
lable_company_credit = Tkinter.Label(root, textvariable = company_credit, font=('ArialBold', 20))
lable_company_credit.place(x = 20, y = 320)



webshop_adress = Tkinter.StringVar()
webshop_adress.set("http://tonkatsutornado.shop-pro.jp/")
lable_webshop_adress = Tkinter.Label(root, textvariable = webshop_adress, font=('Arial',12) )
lable_webshop_adress.place(x = 22, y = 355)


#---------------------------------------
#====================================
root.mainloop()



#===================================



######################################
######################################
########## E O F #####################
######################################
######################################
