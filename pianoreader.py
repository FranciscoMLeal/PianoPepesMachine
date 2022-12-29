import pygame
import pygame.midi
import sys

# Initialize Pygame and the MIDI module
pygame.init()
pygame.midi.init()

# Set up the window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("MIDI Piano Visualizer")

# Create a dictionary to map MIDI notes to colors
colors = {
    60: (255, 0, 0),  # C
    61: (255, 128, 0),  # C#
    62: (255, 255, 0),  # D
    63: (128, 255, 0),  # D#
    64: (0, 255, 0),  # E
    65: (0, 255, 128),  # F
    66: (0, 255, 255),  # F#
    67: (0, 128, 255),  # G
    68: (0, 0, 255),  # G#
    69: (128, 0, 255),  # A
    70: (255, 0, 255),  # A#
    71: (255, 0, 128),  # B
    
    72: (255, 0, 0),  # C
    73: (255, 128, 0),  # C#
    74: (255, 255, 0),  # D
    75: (128, 255, 0),  # D#
    76: (0, 255, 0),  # E
    77: (0, 255, 128),  # F
    78: (0, 255, 255),  # F#
    79: (0, 128, 255),  # G
    80: (0, 0, 255),  # G#
    81: (128, 0, 255),  # A
    82: (255, 0, 255),  # A#
    83: (255, 0, 128),  # B
}

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
        events = input_stream.read(10)

        # Process the MIDI events
        for event in events:
            event_type = event[0][0]
            data = event[0][1:]

            if event_type == 144:  # Note-on event
                note = data[0]
                velocity = data[1]
                print(f"Note-on: {note} with velocity {velocity}")

                # Draw a circle with the corresponding color for the note
                color = colors.get(note, (255, 255, 255))  # default to white if note is not in the dictionary
                pygame.draw.circle(screen, color, (200, 200), float(velocity))
                pygame.display.flip()
            elif event_type == 128:  # Note-off event
                note = data[0]
                velocity = data[1]
                print(f"Note-off: {note} with velocity {velocity}")

                # Clear the screen
                screen.fill((0, 0, 0))
                pygame.display.flip()
            elif event_type == 176:  # Control change event
                controller = data[0]
                value = data[1]
                print(f"Control change: controller {controller} with value {value}")

    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close the input stream and MIDI module, then quit Pygame
            input_stream.close()
            pygame.midi.quit()
            pygame.quit()
            sys.exit()

