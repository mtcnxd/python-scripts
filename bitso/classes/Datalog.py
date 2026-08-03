from datetime import datetime
import os

class Datalog:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def write(self, line):
        try:
            self.file = open(self.filename,'a')
            now = datetime.now()
            text = f"{now} - {line}"
            self.file.write(text +"\n")
        
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return False

    def read(self):
        try:
            self.file = open(self.filename,'r')
            content = self.file.read().rstrip()
            return content
        
        except FileNotFoundError as e: 
            print(f"File not found! {e}")
            return False

    def close(self):
        if self.file is not None:
            self.file.close()

    def delete(self) -> bool:
        try:
            os.remove(self.filename)
            return True

        except FileNotFoundError as e:
            print(f"File not found! {e}")
            return False

