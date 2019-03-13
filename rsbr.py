#! python3
# mouseNow.py - Automatic clicker, mouse location finder and other

#Display mouse position and RGB colours (works better in CMD)
#pyautogui.displayMousePosition()

import pyautogui, time, sys, pyttsx3
from datetime import datetime

#Fail-safe CTRL-ALT-DEL
print('\nPress Ctrl-C to quit.')
pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

#Print screen width and size
width, size = pyautogui.size()
print('\nScreen width: ' + str(width) + '\n' + 'Screen size:  ' + str(size) + '\n') 

#Measure of how long the whole script was working (beginning)
starttimet = datetime.now()

#TODO: Bag full check function (Experimental)
def bag_full():
    try:
        while True:
            q,w,e,r = pyautogui.locateOnScreen('full_bag.png')
            return True
    except:
        return False

#Go to the bank
def bank():
    try:
        #Text to speech cycle announcer
        engine = pyttsx3.init()
        #Measuring time, beginning measurement
        starttime = datetime.now()
        #Locate where the map is
        x,y,o,p = pyautogui.locateOnScreen('map.png')
        #Move mouse to the map icon
        pyautogui.moveTo(x, y, duration=0) 
        #Click the map
        pyautogui.moveRel(-65, -115, duration=0)
        pyautogui.click()
        print('Going to bank 1')
        time.sleep(15)
        pyautogui.click()
        print('Going to bank 2')
        time.sleep(14)
        pyautogui.click()
        print('Going to bank 3')
        time.sleep(14)
        pyautogui.moveRel(-40, 15, duration=0)
        pyautogui.click()
        print('Going to bank 4')
        time.sleep(15)
        pyautogui.click()
        print('Going to bank 5')
        time.sleep(15)
        pyautogui.moveRel(10, 40, duration=0)
        pyautogui.click()
        print('Going to bank 6')
        time.sleep(15)
        pyautogui.moveRel(0, -35, duration=0)
        pyautogui.click()
        print('Going to bank 7')
        time.sleep(18)
        #Click the rug to re-center
        g,h,j,k = pyautogui.locateOnScreen('rug.png')
        pyautogui.moveTo(g, h, duration=0)
        pyautogui.click()
        time.sleep(5)
        t,u,m,n = pyautogui.locateOnScreen('bank6.png')
        pyautogui.moveTo(t, u, duration=0)
        pyautogui.moveRel(-30, 110)
        pyautogui.click()
        print('Moved to bank booth')
        time.sleep(3.5)
        #click to depozit all items
        v,b,n,m = pyautogui.locateOnScreen('openbank1.png')
        pyautogui.moveTo(v, b, duration=0)
        pyautogui.click()
        time.sleep(1)
        print('Depozited all items')
        a,s,d,f = pyautogui.locateOnScreen('pickaxe1.png')
        pyautogui.moveTo(a, s, duration=0)
        pyautogui.moveRel(6, 6, duration=0)
        pyautogui.click()
        print('Took pickaxe')
        time.sleep(1)
        pyautogui.moveTo(x, y, duration=0) 
        pyautogui.moveRel(-15, 0, duration=0)
        pyautogui.click()
        time.sleep(0.5)
        engine.say("Returning to the mining area")
        engine.runAndWait()
        print('Going back 1')
        time.sleep(15)
        pyautogui.click()
        print('Going back 2')
        time.sleep(14)
        pyautogui.click()
        print('Going back 3')
        time.sleep(14.5)
        pyautogui.moveRel(-15, 0, duration=0)
        pyautogui.click()
        print('Going back 4')
        time.sleep(13.5)
        pyautogui.click()
        print('Going back 5')
        time.sleep(13.5)
        pyautogui.moveRel(-30, 25, duration=0)
        pyautogui.click()
        print('Going back 6')
        time.sleep(14.5)
        pyautogui.click()
        print('Going back 7')
        time.sleep(14.5)
        pyautogui.click()
        #Measuring cycle time
        endtime = datetime.now()
        print(str(endtime - starttime))
        print(' ***********  MINING CYCLE COMPLETE ***********')
        engine.say("Mining cycle complete")
        engine.runAndWait()
        #Re-initiate the cycle
        clicker()
        
    except KeyboardInterrupt:
        print('\nDone.\n')
        #pass
            
    
def clicker():
    try:
        cycle = 0
        while True:
            
            #Rock finder
            x,y,w,h = pyautogui.locateOnScreen('b_rock_in_rs.png')
            
            #Move the cursor to a certain position
            pyautogui.moveTo(x, y, duration=0.5) 
            
            #Click the rock
            pyautogui.click()
            time.sleep(0.5)
            
            #Timer
            cycle += 1
            a = ('Mining... : ' + str(cycle))
            sys.stdout.write(a)
            sys.stdout.write('\b' * len(a))
            sys.stdout.flush()
            
            #Bag full check function (cycle counter rn)
            if cycle > 60:
                bank()
            
    except KeyboardInterrupt:
        print('\nDone.')
        pass
    
    
#52 cycles , 7min
clicker()

endtimet = datetime.now()
print('\nTotal running time without interruption: ' + str(endtimet - starttimet))


#TODO: 1. Longer mining intervals 
#TODO: 3. Distance for going TO the bank
#TODO: 4. How to solve the issue of no blue rocks on the screen? 
#TODO: 5. Adjust cycle amount (how long does it take to mine full bag when compared)
#TODO:*6. Create version control































