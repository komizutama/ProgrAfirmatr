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
import yaml

nssp = NSSpeechSynthesizer
voice="com.apple.speech.synthesis.voice.Alex"
ve = nssp.alloc().init()
ve.setVoice_(voice)
recentSay = ["blank1", "blank2", "blank3", "blank4", "blank5"]
say=""
voices = [
"com.apple.speech.synthesis.voice.Alex", 
"com.apple.speech.synthesis.voice.Agnes",
"com.apple.speech.synthesis.voice.Vicki",
"com.apple.speech.synthesis.voice.Victoria",
"com.apple.speech.synthesis.voice.Zarvox" 
]

with open("CodeAffirmations.yaml") as f:
    affirmations=yaml.load(f.read())


class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def affChoice():
    return affirmations[random.randrange(len(affirmations))]


def handler(event):
    shouldExit=False
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
        shouldExit=True

    if shouldExit:
        sys.exit(0)

def main():

    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    
    main()