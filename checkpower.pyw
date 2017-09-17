
import power
import os
import easygui
import time

# charging wire connected or not 
def checkpower():
	ans = power.PowerManagement().get_providing_power_source_type()
	if  ans:
		easygui.msgbox("Greetings,idiot. Looks like you have the power cord disconnected from your laptop. Don't forget it again. KTHNXBAI ", title="CHECK IF POWER CORD IS SAFE")

# open dialogue box 
def keeprunning():
    checkpower()
    # check if power cord is connected or not every sixty seconds 
    time.sleep(60)

while True:
    keeprunning()
