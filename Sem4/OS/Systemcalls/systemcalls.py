import os
import time

def child():
   print('\nA new child ',  os.getpid())
   time.sleep(0.5)
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("\nparent: %d, child: %d\n" % pids)
         time.sleep(0.5)
      reply = input("\nq for quit / c for new fork \n")
      if reply.lower() == 'c': 
          continue
      else:
          break
      
if __name__ == "__main__":
    print("55_Adnan Shaikh")
    parent()

