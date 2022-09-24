import pynput.keyboard
from pynput import keyboard  

list= []

# print key input
def process_keys(key):
    print(key)
    with open("log.txt","a") as fin:
        fin.write(str(key))
        list.append(key)
        if key == keyboard.Key.enter:
            print(str(list))
            if "Key.space" in list:
                print("list contains \"Key.space\"")
            else:
                print("list does not contain \"Key.space\"")
                

             
        
        

# record key input from keyboard
keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
    keyboard_listener.join()
    
# print("\"test\"")
# ideen
# detect words
# split words in txt (+space, +backspace)