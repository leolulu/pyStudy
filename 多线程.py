import time,threading

total_num = 0
def count_up():
    global total_num
    for i in range(500):
        total_num += 1
        print(threading.current_thread().name,i,total_num)
        time.sleep(0.003)

start_time = time.time()
t_list = [threading.Thread(target=count_up) for a in range(500)]
for i in t_list:
    i.start()
    time.sleep(0.007)

# for i in range(500):
#     for j in range(500):
#         total_num += 1
#         print(total_num)