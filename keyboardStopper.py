import _thread

# Function that detects a keyboard input and append True to a_list to confirm
# the keyboard input detection
def input_thread(a_list):
    input()
    a_list.append(True)

# Loop to execute strings of python code in args*
# stop when a keyboard input is detected
def do_stuff(*args):
    a_list = []
    _thread.start_new_thread(input_thread, (a_list,))
    while not a_list:
        for num in args:
            exec(num)
        pass
