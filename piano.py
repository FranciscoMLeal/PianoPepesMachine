import pygame
import pygame.midi
import sys

# Initialize Pygame and the MIDI module
pygame.init()
pygame.midi.init()

# Get a list of all MIDI devices
device_info = [pygame.midi.get_device_info(i) for i in range(pygame.midi.get_count())]

# Print the list of MIDI devices
print("MIDI Devices:")
for i, info in enumerate(device_info):
    print(f"{i}: {info[1]}")

# Prompt the user to select a MIDI device
device_id = int(input("Enter the number of the MIDI device you want to use: "))

# Open an input stream to the MIDI device
input_stream = pygame.midi.Input(device_id)

# Run the game loop
while True:
    # Check if there are any MIDI events available to read
    if input_stream.poll():
        # Read the MIDI events
        events = input_stream.read(100)

        # Process the MIDI events
        for event in events:
            event_type = event[0][0]
            data = event[0][1:]
            print(f"Event type: {event_type}")
            print(f"Data: {data}")

    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close the input stream and MIDI module
            input_stream.close()
            pygame.midi.quit()
            pygame.quit()
            sys.exit()
