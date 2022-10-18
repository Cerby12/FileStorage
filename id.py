import time
import random 
import string


class generate_id:
    def __init__(self) -> None:
        pass
        
    def generate_id(self):
        current_time = int(time.time())
        random_str = "".join(random.choice(string.ascii_letters) for _ in range(10))

        return f"{current_time}{random_str}"