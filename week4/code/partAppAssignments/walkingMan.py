import os
import time

frames = [
    """
     o
   [ + ]
     - 
    | |
    """,
    """
     o
   < + ]
     -
    |  \.
    """,
    """
     o
   [ + ]
     - 
    | |
    """,
    """
     o
   [ + >
     -
  ./  |
    """
]

speed = int(input("Enter the speed: "))

# Animate the stick figure
while True:
    for frame in frames:
        # Clear the terminal screen
        os.system('clear')
        # Print the current frame
        print(frame)
        # Wait before printing the next frame
        time.sleep(1/speed)
        