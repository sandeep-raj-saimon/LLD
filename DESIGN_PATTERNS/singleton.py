# class Singleton:
#     # we are over riding the __new__ method to make sure that only one instance is being created
#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
# s1 = Singleton()
# s2 = Singleton()
# s3 = Singleton()

# print(s1 == s2 == s3)

# there are chances that multiple threads can create more than one object
# we need to use lock
import threading
class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

def create_singleton_instance():
    singleton = Singleton()
    print(f"Singleton instance: {id(singleton)}")

# Creating multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=create_singleton_instance)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


