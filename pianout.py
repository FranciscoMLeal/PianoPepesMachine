import pygame
import pygame.midi
import threading
import sys
import RLBB as pepesmachine
import time
import random

# Initialize Pygame and the MIDI module
pygame.init()
pygame.midi.init()

looper_on = False
#firstimepressed = True

def chg_looper(looper):
    global looper_on
    if looper == True:
        looper_on = False
    else :
        looper_on = True
    print(f"global looper_on : {looper_on}, local looper : {looper}")

tempo = 2

def chg_tempo(temporale):
    if temporale < 50:
        temporale = temporale * 0.1
    elif temporale < 100:
        temporale = temporale * 0.001
    else:
        temporale = temporale * 0.00001
    global tempo
    tempo = temporale
## Get a list of all MIDI devices
#device_info = [pygame.midi.get_device_info(i) for i in range(pygame.midi.get_count())]
#
## Print the list of MIDI devices
#print("MIDI Devices:")
#for i, info in enumerate(device_info):
#    print(f"{i}: {info[1]}")
#
## Prompt the user to select a MIDI device
#device_id = int(input("Enter the number of the MIDI device you want to use: "))
#
# Open an input stream to the MIDI device
input_stream = pygame.midi.Input(1)
    ## START PEPEWINDOW HERE
PepesMachina = pepesmachine
PepesMachina2 = pepesmachine
PepesMachina2.StartPepeFunction()

def startlooping():
    if looper_on:
        PepesMachina2.StartPepeFunction()
    loopPepe = threading.Timer(tempo, startlooping)
    loopPepe.start()
    
firstimepressed = True
def chg_press():
    global firstimepressed
    firstimepressed = False

# Run the game loop
while True:
    # Check if there are any MIDI events available to read
    if input_stream.poll():
        # Read the MIDI events
        events = input_stream.read(10)

        # Process the MIDI events
        for event in events:
            event_type = event[0][0]
            data = event[0][1:]
            timestamper = event[1]
            print(f"Event type: {event_type}")
            print(f"Data: {data}")
            if event_type == 153:
                chg_tempo(data[1])
                chg_looper(looper_on)
                if firstimepressed == True:
                    chg_press()
                    startlooping()
            if event_type == 144:
                x = random.randrange(0,500)
                y = random.randrange(0,500)
                PepesMachina.ClicktoChangePP(x,y)
                
            ## UPDATE PEPEWINDOW HERE
            
    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close the input stream and MIDI module
            input_stream.close()
            pygame.midi.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            chg_looper(looper_on)
