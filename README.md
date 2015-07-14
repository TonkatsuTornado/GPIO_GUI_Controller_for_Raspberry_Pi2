# GPIO_GUI_Controller_for_Raspberry_Pi2
Python and Tkinter based GPIO GUI Controller for Raspberry Pi2


![Overview](http://livedoor.blogimg.jp/tonkatsutornado/imgs/6/e/6e4e5df8.png)

## SUMMARY 
This python program allows you to controll your RasPi2's GPIO with a mouseclick! 

## How to Run
1. Download the python file [ RaspberryPi2_GPIO_controller_GUI_vXX.py ] into your Raspberry Pi2. ( XX means version number. please refer to the file name which you just downloaded.）
2. Move into the folder that you downloaded the file in step 1, then type the following.
'$ sudo python RaspberryPi2_GPIO_controller_GUI_vXX.py'

Since this program is made from Python and Tkinter, We think Raspbian can run it without further  libraries importing or settings up.

## DESCRIPTIONS
![descriptions](http://livedoor.blogimg.jp/tonkatsutornado/imgs/a/2/a28e0163.png)

**Output Button** - outputs the GPIO channel.  
**Mode select**  - changes the operation mode. A mode or M mode.  
  * A mode - Output state will be toggled every time you click the button.
  * M mode - Output state will go to High while you are pressing the button.  
**Exit Button** - exits this program.  

**Keyboard Shortcut**  

    IO21	a		IO26	q  
    IO20	s		IO19	w  
    IO16	d		IO13	e  
    IO12	f		IO6		r  
    IO7   g   IO5   t
    IO8 	h		IO11	y  
    IO25	j		IO9		u  
    IO24	k		IO10	i  
    IO23	l		IO22	o	  	
    IO18	b		IO27	p  
    IO15	n		IO17	@  
    IO14	m		IO4		7  
              IO3   8  
              IO2   9	  
    Mode change : Shift + each key  
    Quite       : ESC  



