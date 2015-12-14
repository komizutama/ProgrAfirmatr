# cocoa_keypress_monitor.py by Bjarte Johansen is licensed under a 
# License: http://ljos.mit-license.org/
# https://gist.github.com/ljos/3019549

from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
from  AppKit import NSSpeechSynthesizer
import time
import sys
import random

nssp = NSSpeechSynthesizer
voice="com.apple.speech.synthesis.voice.Alex"
ve = nssp.alloc().init()
ve.setVoice_(voice)
recentSay = ["blank1", "blank2", "blank3", "blank4", "blank5"]
say=""

affirmations=[
"You are being highly productive. ",
"You are a great programmer. ", 
"How did you get so good at coding so fast? ", 
"I love what you're doing there. ",
"You are awesome. ", 
"You are a programming God. ", 
"This is amazing! ", 
"You are a star programmer.  ", 
"Guido Van Rossum wishes he was you. ", 
"Ken Thompson dreams of coding as well as you are right now. ", 
"I can't believe I get to be your computer. ", 
"I'm going to tell all the other computers on the network how awesome you are. ", 
"Don't stop Hopper! ", 
"You're gonna get a Turing Award for this! ", 
" I used to think John Skeet was cool, until now! ", 
"Based off of what I'm seeing, you probably can explain N=NP. ", 
"You type so fast! ",
"I bet Bruce Schneier is tweeting about you right now. ",
"You possess the qualities needed to be extremely successful. ",
"You are conquering all bugs; you are defeating them steadily each moment. ",
"You radiate beauty, charm, and grace. ",
"Your work is supported by the universe; your genius manifests into reality before your eyes. ",
"You are a powerhouse; Your code is indestructible. ", 
"You are goign to be extremely successful! ",

]

voices = ["com.apple.speech.synthesis.voice.Alex", "com.apple.speech.synthesis.voice.Agnes",
"com.apple.speech.synthesis.voice.Vicki",
"com.apple.speech.synthesis.voice.Victoria",
"com.apple.speech.synthesis.voice.Zarvox" ]


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def affChoice():
    return affirmations[random.randrange(len(affirmations))]


def handler(event):
    try:
        if not ve.isSpeaking():

            global say
            global recentSay

            say=affChoice()
            while say in recentSay:
                say=affChoice()
            ve.startSpeakingString_(say)
            recentSay.pop(0)
            recentSay.append(say)
            

    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
        sys.exit()

def main():

    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    
    main()