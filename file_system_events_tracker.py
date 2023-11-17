import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/k_bab/Downloads'

class FileSystemEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Someone created {event.src_path}.")

    def on_deleted(self, event):
        print(f"Someone deleted {event.src_path}.")

    def on_moved(self, event):
        print(f"Someone moved {event.src_path}.")

    def on_modified(self, event):
        print(f"Someone moved {event.src_path}.")

event_handler = FileSystemEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    print('Running')
    while True:
        time.sleep(2)
        print('...')
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()