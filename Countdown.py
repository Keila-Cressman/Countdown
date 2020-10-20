from tkinter import *
#used for making the GUI
from PIL import Image, ImageTk
#from datetime import *
from datetime import datetime
from pytz import timezone
import time
root = Tk()


logo = Image.open("eagles_logo.jpg")
photo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image = photo)
logoLabel.pack()

def main():
    #layout of GUI
    root.title("TheBaldEagle4133")
    root.geometry("600x600")
    root.configure(bg = '#135252')
    #display of words
    dayLabels = Label(root, text = 'Days \t|\t Hours \t|\t Minutes |\t Seconds', 
                      width = '100', font = 'Arial 12 bold', bg = '#135252')
    dayLabels.pack()
    
def printtext():
    tz = timezone('US/Eastern')
    startDate = datetime.now(tz)
    
    newDate = userInput.get() 
    month = int(newDate[0:2])
    day = int(newDate[2:4])
    year = int(newDate[4:8])
    timeHour = int(newDate[8:10])
    #if minutes are/n't entered
    if (len(newDate) > 10):
        timeMinutes = int(newDate[10:12])
    else:
        timeMinutes = 0
    timeSeconds = 0
   
    endDate = datetime(year, month, day, timeHour, timeMinutes, timeSeconds)
    
    startDay = int(startDate.strftime("%d"))
    endDay = int(endDate.strftime("%d"))
    newDay = endDay - startDay
    currentMonth = int(startDate.strftime("%m"))
    currentYear = int(startDate.strftime("%Y"))
    
    if (currentYear < year):
        yearDifference = year - currentYear
        newYear = yearDifference * 365
        if (currentMonth < month):
            monthDifference = month - currentMonth
            newMonth = monthDifference * 30
            newDay += newMonth + newYear
        else:
            newDay += newYear
    else:
        if (currentMonth < month):
            monthDifference = month - currentMonth
            newMonth = monthDifference * 30
            newDay += newMonth
        
    
    startHour = int(startDate.strftime("%H"))
    endHour = int(endDate.strftime("%H"))
    newHour = endHour - startHour
    if (newHour < 0):
        newHour += 24
      
    startMinute = int(startDate.strftime("%M"))
    endMinute = int(endDate.strftime("%M"))
    newMinute = endMinute - startMinute
    if(newMinute < 0):
        newMinute += 60
    
    startSecond = int(startDate.strftime("%S"))
    endSecond = int(endDate.strftime("%S"))
    newSecond = endSecond - startSecond
    if (newSecond < 0):
        newSecond += 60
    
    setButton.destroy()
    userInput.destroy()    
    countdown(newDay, newHour, newMinute, newSecond)
    
   
#Set button
userInput = Entry(root)
userInput.pack()
userInput.focus_set()
    
setButton = Button(root, text = 'Set', width = '10', command = printtext)
setButton.pack(side = 'bottom')

placeHolder = Label(root, text = '', width = '600', font = 'Arial 80 bold',
                         fg = 'black')
placeHolder.pack()


def countdown(newDay,newHour,newMinute,newSecond):
    #display of numbers
    numbersLabel = placeHolder
    
    root.update()
    days = newDay
    hours = newHour
    minutes = newMinute 
    seconds = newSecond
    while(days>=0 and hours>=0 and minutes>=0 and seconds>=0):
        
        #track the length of numbers
        s = str(seconds)
        m = str(minutes)
        h = str(hours)
        
        #hours(2) , minutes(2) , seconds(1)
        if (len(h)!=1 and len(m)!=1 and len(s)==1):
            numbersLabel.configure(text="%d:%d:%d:%d%d"%(days,hours,minutes,0,seconds))
            
        #hours(1) , minutes(2) , seconds(1)
        elif (len(h)==1 and len(m)!=1 and len(s)==1):
            numbersLabel.configure(text="%d:%d%d:%d:%d%d"%(days,0,hours,minutes,0,seconds))
            
        #hours(2) , minutes(1) , seconds(2)   
        elif (len(h)!=1 and len(m)==1 and len(s)!=1):
            numbersLabel.configure(text="%d:%d:%d%d:%d"%(days,hours,0,minutes,seconds))
            
        #hours(2) , minutes(1) , seconds(1)   
        elif (len(h)!=1 and len(m)==1 and len(s)==1):
            numbersLabel.configure(text="%d:%d:%d%d:%d%d"%(days,hours,0,minutes,0,seconds))
            
        #hours(1) , minutes(1) , seconds(2)   
        elif (len(h)==1 and len(m)==1 and len(s)!=1):
            numbersLabel.configure(text="%d:%d%d:%d%d:%d"%(days,0,hours,0,minutes,seconds))
            
        #hours(1) , minutes(1) , seconds(1) 
        elif (len(h)==1 and len(m)==1 and len(s)==1):
            numbersLabel.configure(text="%d:%d%d:%d%d:%d%d"%(days,0,hours,0,minutes,0,seconds))
            
        #hours(1) , minutes(2) , seconds(2) 
        elif (len(h)==1 and len(m)!=1 and len(s)!=1):
            numbersLabel.configure(text="%d:%d%d:%d:%d"%(days,0,hours,minutes,seconds))
         
        #hours(2) , minutes(2) , seconds(2)
        else:
            numbersLabel.configure(text="%d:%d:%d:%d"%(days,hours,minutes,seconds))
            
        root.update()
        
        #minutes(01) , seconds(00)
        if (minutes!=0 and seconds==0):
            seconds = 60
            minutes -= 1
        #hours(01) , minutes(00) , seconds(00)
        if (hours!=0 and minutes==0 and seconds==0):
            seconds = 60
            minutes = 59
            hours -= 1
        #days(01) , hours(00) , minutes(00) , seconds(00)
        if (days!=0 and hours==0 and minutes==0 and seconds==0):
            seconds = 60
            minutes = 59
            hours = 23
            days -= 1
        seconds -= 1
        time.sleep(1)
    numbersLabel.configure(text="Game Time")
main()
root.mainloop()