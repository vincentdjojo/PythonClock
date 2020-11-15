from graphics import *
import math
import time
import random
import winsound
import datetime

#========\/Initialize Time\/==========
currentTime=time.strftime("%H:%M:%S")
initializedTime=currentTime.split(":")
hour=initializedTime[0]
minute=initializedTime[1]
currentSecond=int(initializedTime[2])
currentMinute=int(initializedTime[1])

#========/\Initialize Time/\==========

win=GraphWin("TimeBud",300,350)
win.setBackground("pink")


#Only used in the functin draw_clock-circles()
pi_2=2*3.142#360 degress in pi.
fiveMinutes=pi_2/12#Radians required for 5 minutes.
second=pi_2/(12*5)#Radians required for a second.
hypotenuse=110 #Standard length of all the hands in the clock: second, minute, hour, timer.

#=========================/\Initialize Measurments (Radians and pi)/\========================

#===========================================\/Functions\/=================================================================

def random_colors():
    """random_colors(): Generates random colors."""
    for i in range(75):
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        color = color_rgb(r, g, b)
        return color

def draw_clock_circles():
    """draw_clock_circles(): Creates the circles that represent the numbers on an analogue clock."""
    
    timeCount, i=0, 0
    circles=[]
    
    while i<=pi_2+1:
        i=i+second
        timeCount=timeCount+second
        
        if timeCount==fiveMinutes:
            timeCount=0
            opposite=math.sin((0.25*pi_2-i))*(hypotenuse+7)
            adjacent=math.cos((0.25*pi_2-i))*(hypotenuse+7)
            Circ=Circle(Point(adjacent+150,opposite+150),8)
            Circ.setFill(random_colors())
            Circ.draw(win)
            circles.append(Circ)
        
    rec=Rectangle(Point(90,325),Point(210,350))
    rec.setFill(color_rgb(196, 42, 87))
    rec.draw(win)
    rec2=Rectangle(Point(90,300),Point(210,325))
    rec2.setFill(color_rgb(196, 42, 87))
    rec2.draw(win)    

def draw_seconds_hand_and_digital_clock_and_date(testCurrentTime):
    """draw_seconds_hand_and_digital_clock_and_date(): Creates and updates the seconds
    hand as well as create and update a digital clock everytime the function is called."""


    #========================================================================
    #Creates and updates the second_hand everytime the function is called.

    #==============================================================================
    #Formula for finding the position of the minute_hand during any minute.
    #Important! Formula used in second_hand, minute_hand, hour_hand and timer_hand.
    
    second=testCurrentTime[2]
    angle=180-(6*int(second)) #Formula for getting angle for any hand
    radian_form=math.radians(angle)
    x=150+hypotenuse*math.sin(radian_form)#Gets the height of coordinate
    y=150+hypotenuse*math.cos(radian_form)#Gets the width of the coordinate

    #==============================================================================
    
    second_hand=Line(Point(150,150),Point(x,y))
    second_hand.setFill("red")
    second_hand.draw(win)
    
    #========================================================================

    #========================================================================
    #Creates a digital clock and updates it everytime the function is called.
        
    digitalTime=Text(Point(150,340), testCurrentTime) #Define the current
                                                      #time in Text form.
    digitalTime.setFill("white")
    digitalTime.setSize(15)
    digitalTime.draw(win)

    date = datetime.date.today()                      #Define the current
                                                      #date in Text form.
    
    digitalDate=Text(Point(150,315), date)
    digitalDate.setFill("white")
    digitalDate.setSize(15)
    digitalDate.draw(win)
     
    time.sleep(1)
                                                        
    digitalTime.undraw()                              #undraws digitalTime, 
    second_hand.undraw()                              #second_hand,
    digitalDate.undraw()                              #and digitalDate.
    
    #========================================================================
    
def draw_minute_hand(testCurrentTime):
    """draw_minute_hand(): Creates and updates the minute hand everytime the function is called."""
    
    second=testCurrentTime[2]
    minute=testCurrentTime[1]

    #==============================================================================
    #Formula for finding the position of the minute_hand during any minute.
    #Important! Formula used in second_hand, minute_hand, hour_hand and timer_hand.

    angle=180-(6*int(minute)) #Formula for getting angle for any hand
    radian_form=math.radians(angle)
    x=150+(hypotenuse-5)*math.sin(radian_form)#Gets the height of coordinate
    y=150+(hypotenuse-5)*math.cos(radian_form)#Gets the width of the coordinate
    
    #==============================================================================
    
    global minute_hand #minute_hand needs to be global so that it can be undrawn.
                       #It will be undrawn in the analogue_clock() module.
    
    minute_hand=Line(Point(150,150),Point(x,y))
    minute_hand.setFill('white')
    minute_hand.setWidth(2)
    minute_hand.draw(win)

def draw_hour_hand(testCurrentTime):
    """draw_hour_hand(): Creates and updates the hour hand everytime the function is called."""
    
    hour=testCurrentTime[0]
    second=testCurrentTime[2]
    minute=testCurrentTime[1]
    
    #==============================================================================
    #Formula for finding the position of the minute_hand during any minute.
    #Important! Formula used in second_hand, minute_hand, hour_hand and timer_hand.
    #Slightly different for hour_hand because testCurrentTime is in 24h format.
    
    if int(hour)>12:
        angle=180-(30*((int(hour)+int(minute)/60)-12)) #Dedeuct 12 from the 24 hour
                                                       #hour format so that it will
                                                       #work on the analogue_clock
                                                       #which is in 12h format.
        
    elif int(hour)<=12:                                
        angle=180-(30*((int(hour)+int(minute)/60)))    #If hour<=12, then use the
                                                       #the angle normally
                                                       #because it's still in 12h
                                                       #format.
        
    radian_form=math.radians(angle)
    x=150+(hypotenuse-30)*math.sin(radian_form)
    y=150+(hypotenuse-30)*math.cos(radian_form)

    #==============================================================================
    
    global hour_hand #hour_hand needs to be global so that it can be undrawn

    hour_hand=Line(Point(150,150),Point(x,y))          #Define the current
                                                       #hour using a
                                                       #line graphic.

    hour_hand.setFill('white')
    hour_hand.setWidth(2)
    hour_hand.draw(win)



def second_sound():
    """second_sound(): Plays a sound every second (Not used)."""
    
    myImage = Image(Point(150,150), 'cute-anime-face2.png')
    myImage.draw(win)
    winsound.Beep(3000,100)
    myImage.undraw()
    
def minute_sound():
    """minute_sound(): Plays a sound every minute."""
    
    #=======================================================
    #Plays a sound everytime second_hand reaches 60 seconds.
    #TimeBud's face moves as well.
    
    myImage = Image(Point(150,150), 'cute-anime-face.png')
    myImage.draw(win)
    winsound.Beep(3000,100)
    myImage.undraw()
    myImage = Image(Point(150,150), 'cute-anime-face1.png')
    myImage.draw(win)  
    winsound.Beep(2500,100)
    myImage.undraw()
    myImage = Image(Point(150,150), 'cute-anime-face2.png')
    myImage.draw(win)    
    winsound.Beep(2000,100)
    myImage.undraw()
    myImage = Image(Point(150,150), 'cute-anime-face1.png')
    myImage.draw(win)    
    winsound.Beep(1000,100)
    myImage.undraw()    
    winsound.Beep(500,100)

    #=======================================================
    
def drawTimeBud():
    """drawTimeBud(): Draws the background character 'TimeBud'. It includes its shirt and his face in the background."""
    
    global myImage #myImage needs to be global so that it can be updated (drawn or undrawn) when animating the face.
    myImage = Image(Point(150,150), 'cute-anime-face.png')
    myImage.draw(win)
    shirt = Image(Point(150,175), 'shirt.png') #Draws TimeBud's hoodie.
    shirt.draw(win)

def drawButtons():
    """drawButtons(): Draws the buttons for the UI: 'Alarm' button and 'Stop Watch' button."""

    #===========================================================================
    #Draws the UI for the alarm. This will be used in the module called alarm().
    
    alarm=Rectangle(Point(210,325),Point(300,350))
    alarm.setFill("dark red")
    alarm.draw(win)
    alarmText=Text(Point(255,340), "Alarm")
    alarmText.setSize(15)
    alarmText.setFill("white")
    alarmText.draw(win)
    
    global alarmSet #alarmSet needs to be global so that it can be updated in
                    #other modules: setFill, undraw, draw.
    
    alarmSet=Rectangle(Point(210,300),Point(300,325))
    alarmSet.setFill("grey")
    alarmSet.draw(win)

    #===========================================================================

    #=====================================================================================
    #Draws the UI for the Stop Watch. This will be used in the module called stop_watch().
    
    global stopWatch #stopWatch needs to be global so that it can be updated in
                     #other modules: setFill, undraw, draw.
    
    stopWatch=Rectangle(Point(0,325),Point(90,350))
    stopWatch.setFill("dark red")
    stopWatch.draw(win)
    stopWatchText=Text(Point(45,340), "Stop Watch")
    stopWatchText.setSize(15)
    stopWatchText.setFill("white")
    stopWatchText.setSize(13)
    stopWatchText.draw(win)
    
    global digitalStopwatch #digitalStopwatch needs to be global so that it can be updated 
                            #in other modules: setFill, undraw, draw.
    
    digitalStopwatch=Rectangle(Point(0,300),Point(90,325))
    digitalStopwatch.setFill("grey")
    digitalStopwatch.draw(win)
    
    #=====================================================================================
   
    
def stop_watch(testCurrentTime,firstPress,temp,loop):
    """stop_watch(): Creates the green hand for the Stop Watch. Changes 'myImage', the face', everytime a second goes by."""

    #========================================================================================
    #Creates a Stop Watch:
    #   *Updates timer_hand (The timer in terms of the analogue_clock).
    #   *Updates digtalStopWatchText (The timer in terms of seconds).
    #   *Three Parameters:
    #       1.testCurrentTime: Get the current time from another module.
    #       2.firstPress: Check if the user pressed the alarm already
    #         or not.
    #       3.temp: Stores the time the 'Stop Watch' button was pressed.
    #       4.loop: Checks if the Stop Watch should continue counting
    #               the time elapsed.
    
    if loop==True:

            #===============================
            #Gets the difference between
            #the current time (now) and
            #the stored time the Stop Watch
            #button was pressed (temp).
        
            now = datetime.datetime.now()
            timeElapsed=(now - temp).seconds
            
            #===============================
            
            #==============================================================================
            #Formula for finding the position of the timer_hand during any second elapsed.
            #Important! Formula used in second_hand, minute_hand, hour_hand and timer_hand.

            angle=180-(6*int(timeElapsed))            
            radian_form=math.radians(angle)
            x=150+hypotenuse*math.sin(radian_form)
            y=150+hypotenuse*math.cos(radian_form)

            #==============================================================================
            
            global timer_hand               #timer_hand needs to be global
                                            #so that it can be updated 
                                            #in other modules: undraw, draw.
            
            timer_hand=Line(Point(150,150),Point(x,y))
            timer_hand.setFill("green")
            myImage.undraw()
            timer_hand.draw(win)
            second_sound()
            myImage.draw(win)
                
            global digtalStopwatchText      #digtalStopwatchText needs to be global
                                            #so that it can be updated 
                                            #in other modules: setFill, undraw, draw.
                       
            digtalStopwatchText=Text(Point(45,315), str(timeElapsed))
                                            #Shows the time elapsed in number form
                                            #using Text graphics.
                                            #Shown on the bottom left of the window.

            digtalStopwatchText.setSize(15)
            digtalStopwatchText.setFill("white")
            digtalStopwatchText.draw(win)
            
    #========================================================================================
                  
def alarm():
    """alarm(): Setup an alarm and rings at the time specified."""
    
    checkMouse=None
    while checkMouse==None:
        myImage = Image(Point(150,150), 'cute-anime-face1.png')
        myImage.draw(win)
        winsound.Beep(3000,100)
        myImage.undraw()
        myImage = Image(Point(150,150), 'cute-anime-face2.png')
        myImage.draw(win)
        winsound.Beep(2500,100)
        myImage.undraw()
        myImage.draw(win)
        winsound.Beep(2000,100)
        myImage.undraw()
        
        winsound.Beep(3000,100)
        myImage.draw(win)
        winsound.Beep(2500,100)
        myImage.undraw()
        myImage = Image(Point(150,150), 'cute-anime-face2.png')        
        winsound.Beep(2000,100)
        myImage.undraw()
        checkMouse=win.checkMouse()
                    
def analogue_clock():
    """analogue_clock(): Draw and update hour, minute and seconds hand. Calls the alarm module when needed. Calls the Stop Watch module when needed."""


#========\/Draw Layout\/==========
    
    drawTimeBud()
    draw_clock_circles()
    drawButtons()

#========/\Draw Layout/\==========
    
    minuteCount=0
    hourCount=0
    testHour=0
    
#=======\/Stop Watch Variable Initialization\/========
    
    loop=True
    firstPress=True
    stop=True
    timerCount=0
    drawn=False
    InputBool=False #Checks if the user has set an
                    #alarm:
                    #   *False means not set.
                    #   *True means set. 

#=======/\Stop Watch Variable Initialization/\========

    #Clock:
    while loop==True:
                    
        currentTime=time.strftime("%H:%M:%S")
    
        testCurrentTime=currentTime.split(":")
        testSecond=testCurrentTime[2]
        testMinute=testCurrentTime[1]
        testHour=testCurrentTime[0]

        draw_seconds_hand_and_digital_clock_and_date(testCurrentTime)
        
        checkMouse=win.checkMouse()
        
#============================================\/  Alarm  \/===================================================         
        #Alarm:
        
        if checkMouse!=None:
            if 210<checkMouse.x<300:                                
                if 325<checkMouse.y<350:                    #When pressed within these coordinates,
                                                            #start the Stop Watch.
                    
                    if InputBool==False:                    #Stop Watch button only works when
                                                            #alarm is not set so InputBool==False.
                        
                        alarmWin=GraphWin("Alarm",250,100)
                       
                        prompt = Text(Point(180, 35), "1.Enter time.\n 2.Click anywhere \nto submit.")
                        prompt.draw(alarmWin)               #Prompt the user to enter the time the
                                                            #the alarm should set off.
                        
                        while InputBool==False:
                            
                            try:                            #Validate the input.
                                
                                hourText=Text(Point(30, 20),"Hour:")
                                hourText.draw(alarmWin)
                                
                                Hour = Entry(Point(85, 20),5)
                                Hour.draw(alarmWin)
                                

                                minuteText=Text(Point(30, 50),"Minute:")
                                minuteText.draw(alarmWin)
                                
                                Minute = Entry(Point(85, 50),5)
                                Minute.draw(alarmWin)
                                

                                secondText=Text(Point(30, 80),"Second:")
                                secondText.draw(alarmWin)
                                
                                Second = Entry(Point(85, 80),5)
                                Second.draw(alarmWin)
                                

                                
                                alarmWin.getMouse()
                                timerHour= Hour.getText()
                                timerMinute=Minute.getText()
                                timerSecond=Second.getText()

              
                                if timerHour=='' or timerMinute=='' or timerSecond=='':
                                    raise ValueError("Error: All fields \n must be filled.")
                                if int(timerHour)>24 or int(timerHour)<0:
                                    raise ValueError("Error: There is no\n such time.")
                                if int(timerMinute)<0 or int(timerMinute)>60:
                                    raise ValueError("Error: There is no\n such time.")
                                
                                if int(timerSecond)<0 or int(timerSecond)>60:
                                    raise ValueError("Error: There is no\n such time.")
                                
                                InputBool=True              #Set InputBool to True once input is valid.
                                prompt.undraw()
                                prompt = Text(Point(180, 35), "Input Valid")#Prompt to the user input is valid.
                                prompt.draw(alarmWin)
                                alarmWin.close()            #Close the window.
                                
                            except GraphicsError:
                                InputBool=False #Initialize InputBool.
                                break
                                alarmWin.close()#Close window as if nothing has happened.
                            except ValueError:
                                prompt.undraw()
                                prompt = Text(Point(180, 35), "Failure with \ninput value")
                                prompt.draw(alarmWin)                            
                            except ValueError as err_msg:
                                prompt.undraw()
                                prompt = Text(Point(180, 35), err_msg)
                                prompt.draw(alarmWin)
                            except TypeError:
                                raise TypeError("Error: Input needs to be an integer.")
                                prompt.undraw()
                                prompt = Text(Point(180, 35), err_msg)
                                prompt.draw(alarmWin)
                            except NameError:
                                raise NameError("Error: Input needs to be an integer.")

        elif InputBool==True: #Checks if user already inputted the time.
            alarmSet.setFill('green')

            if drawn==False: #If alarmText not drawn, draw it.
                alarmTime=timerHour+" "+timerMinute+" "+timerSecond
                alarmText=Text(Point(255,312.5),alarmTime)
                alarmText.setFill("white")
                alarmText.draw(win)
                drawn=True #Set drawn to True as it is already drawn.
                
            if timerHour==testHour: #If it's time for the alarm to ring, produce sound.
                if timerMinute==testMinute:
                    if timerSecond==testSecond:
                        myImage.undraw()
                        alarm()
                        myImage.draw(win)
                        InputBool=False
                        drawn=False
                        alarmSet.setFill('grey')
                        alarmText.undraw()
                        
#===================================/\  Alarm  /\=========================================
                        
#===================================\/Stop Watch\/========================================         
        #Stop Watch:
                        
        #Destroy timer:
        if checkMouse!=None and timerCount==1: #If timerCount==1 meaning it's counting
                                               #the time elapsed, do the following:
            if 0<checkMouse.x<90:
                if 325<checkMouse.y<350:
                    if firstPress==False and loopTimer==True :
                        
                        timerCount=0
                        loopTimer=False
                        digtalStopwatchText.undraw()
                        timer_hand.undraw()
                        stop_watch(testCurrentTime,firstPress,tempDate,loopTimer)
                        stop=True
                        
        #Create timer:              
        if checkMouse!=None and timerCount==0: #If timerCount==0 meaning it's not counting
                                               #the time elapsed, do the following:
            if 0<checkMouse.x<90:
                if 325<checkMouse.y<350:
                    if timerCount==0:
                        digitalStopwatch.setFill("green")
                        stopWatch.setFill("green")
                        timerCount=1

        
                        loopTimer=True
                        if firstPress==True:
                            tempDate=datetime.datetime.now()
                            stop_watch(testCurrentTime,firstPress,tempDate,loopTimer)
                       
                            firstPress=False             
                            stop=False          #Set stop to False so that it continues
                                                #counting the time elapsed.
                            
        if stop==True:                          #If stop==True, set the UI to look
                                                #as follows:
            
            digitalStopwatch.setFill("grey")
            stopWatch.setFill("dark red")
            
        #Refresh timer:
        if firstPress==False and stop==False and timerCount==1: #Every second elapsed,
                                                                #do the following:
            
            timer_hand.undraw()
            digtalStopwatchText.undraw()
            stop_watch(testCurrentTime,firstPress,tempDate,loopTimer)
            
        checkMouse=None
        
#===================================/\Stop Watch/\========================================          

#===================================\/Initialize the variables\/=======================================
        
        if int(testSecond)<59 and minuteCount==0:
            draw_minute_hand(testCurrentTime)
            minuteCount=1
        if testSecond=="59":
            minute_hand.undraw()
            myImage.undraw()
            minute_sound()
            myImage.draw(win)
            minuteCount=0
        if int(testMinute)<=59 and hourCount==0:
            draw_hour_hand(testCurrentTime)
            hourCount=1
        if testSecond=="59":
            hour_hand.undraw()
            hourCount=0
            
        #Initialize timer values:
        if stop==True:
            loopTimer=True
            firstPress=True
            timerCount=0

#===================================/\Initialize the variables/\=======================================
            
#===========================================/\Functions/\=================================================================
            
def main():
    analogue_clock()
    
main()
