# -------------------------- Synchronous, Multi Threading, Asynchronous ------------------------
'''
import time

def get_food(c_id):
   print("Customer %s's food is cooking...." % c_id)
   time.sleep(5)
   print("Customer %s's food is ready" % c_id)


def make_order(c_id):
   print("Customer %s's food is Ordering...." % c_id)
   get_food(c_id)


cust = 5

print("=====Starting time: " + str(time.ctime()))
for c in range(cust):
   make_order(c)

print("=====Ending time: " + str(time.ctime()))


# --------------------------- Multi Threading -----------------------------------

import time
from threading import Thread
import threading
def get_food(c_id):
   print("Customer %s's food is cooking...." % c_id)
   time.sleep(5)
   print("Customer %s's food is ready" % c_id)
   print("=======Ending time: " + str(time.ctime()))

def make_order(c_id):
   print("Running Thread: " + str(threading.current_thread().name))
   print("Customer %s's food is Ordering...." % c_id)
   get_food(c_id)

cust = 5

threads = []

print("=======Starting time: " + str(time.ctime()))

for c in range(cust):
   thread = Thread(target=make_order, args=(c,))
   thread.start()

   for t in threads:
       t.join()



# --------------------- Asynchronous ------------------------------

import time
import asyncio
import logging

logging.basicConfig(
        level=logging.INFO,
        format=' %(message)s: %(threadName)10s',
    )

async def get_food(c_id):
   logging.info("Running thread: ")
   print("Customer %s's food is cooking...." % c_id)
   await asyncio.sleep(5)
   print("Customer %s's food is ready" % c_id)


async def make_order(c_id):
   print("Customer %s's food is Ordering...." % c_id)
   await get_food(c_id)


cust = 5
tasks = []

for c in range(cust):
   tasks.append(make_order(c))

print("=======Starting time: " + str(time.ctime()))
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print("=======Ending time: " + str(time.ctime()))
'''
# suppose a teacher order his 5 every single student to do something several thing
# but with same time. that means different tasks will do same time.
import asyncio
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s: %(threadName)5s',
)

async def do_add(student_id):
  if student_id ==1:
    #do something
  elif student_id==2:
    #do something
  #continue
  # sobkichui akisomoy return korbe
  # 2 ta thread use kore korle better hobe
    logging.INFO("Running Thread")
    print("Student %s's doing...." % student_id)
    await asyncio.sleep(7)

# akhane amon akta method thakbke jar moddhe prthom student ase jog,
#  2 as biog, avabe korte thakbe.
