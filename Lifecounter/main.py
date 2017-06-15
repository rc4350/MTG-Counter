from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch

class LifeCounter(Widget):
    def __init__(self, **kwargs):
        super(LifeCounter, self).__init__(**kwargs)
        #define references for ids that work with timer
        self.startButton = self.ids['startBtn']
        self.stopButton = self.ids['stopBtn']
        self.resetButton = self.ids['resetBtn']
        self.timeLabel = self.ids['timeLabel']
        self.time = '50:00'

        #define references for ids that work with life counters
        #player 1
        self.p1UpButton = self.ids['p1up']
        self.p1DownButton = self.ids['p1down']
        self.p1LifeLabel = self.ids['p1life']
        self.p1LifeCount = 20;
        #player 2
        self.p2UpButton = self.ids['p2up']
        self.p2DownButton = self.ids['p2down']
        self.p2LifeLabel = self.ids['p2life']
        self.p2LifeCount = 20;
        

    def startTimer(self):
        Clock.schedule_interval(self.updateTime, 1)
        self.startButton.disabled = True
        self.stopButton.disabled = False
        self.resetButton.disabled = False

    def stopTimer(self):
        Clock.unschedule(self.updateTime)
        self.time = '50:00'
        self.timeLabel.color = (1,1.0,1.0,1)
        self.timeLabel.text = self.time
        self.startButton.disabled = False
        self.stopButton.disabled = True
        self.resetButton.disabled = False
        
    def updateTime(self, dt):
        minutes = int(self.time[:2])
        seconds = int(self.time[3:])
        minform = ''
        secform = ''
        if(minutes >0 or seconds >0):
            if (seconds >0):
                seconds -= 1
            elif(seconds == 0):
                seconds = 59
                minutes-= 1

        if (minutes == 0 and seconds == 0):
            self.timeLabel.color = (1,.0,.0,1)
            self.timeLabel.text = 'TIME'
            
        else:
            if(minutes < 10):
                minform =  '0'+str(minutes)
            else:
                minform = str(minutes)
            if(seconds <10):
                secform = '0'+str(seconds)
            else:
                secform = str(seconds)
            self.time = minform+':'+secform
            self.timeLabel.text = self.time
            
    #method executes when reset button is clicked
    def resetAction(self):
        self.p1LifeCount = 20;
        self.p2LifeCount = 20;
        self.updatePoneLife()
        self.updatePtwoLife()
        

    #call these methods to update life labels
    def updatePoneLife(self):
        self.p1LifeLabel.text = str(self.p1LifeCount)
    def updatePtwoLife(self):
        self.p2LifeLabel.text = str(self.p2LifeCount)

    #methods for up and down buttons on life totals
    def increasePoneLife(self):
        self.p1LifeCount +=1
        self.updatePoneLife()
    def decreasePoneLife(self):
        self.p1LifeCount-=1
        self.updatePoneLife()

    def increasePtwoLife(self):
        self.p2LifeCount +=1
        self.updatePtwoLife()
    def decreasePtwoLife(self):
        self.p2LifeCount-=1
        self.updatePtwoLife()
        
class LifeApp(App):
    def build(self):
        return LifeCounter()

if __name__ == '__main__':
    LifeApp().run()
    
