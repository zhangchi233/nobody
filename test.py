import os
import time
from multiprocessing import Process
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# the tast is cpu bound, i use multprocessing to speed up the result
n1 = 5000 
n2=500000 
n3=5000000
n4= 50000000
times=[n1,n2,n3,n4]
d = {'cpp_debug':[],'python':[],'cpp_release':[]}
times = np.linspace(50000,500000,10,dtype=int)
def command_time(command,dict=d):
	start= time.perf_counter()
	os.system(command)
	end= time.perf_counter()
	time_diff=end-start
	#print(command+" time is ",time_diff)
	iteration = str(command.split(' ')[-2])
	if command.find('python') != -1:
		
		d['python'].append([iteration,time_diff])
	elif command.find('Debug') != -1:
		
		d['cpp_debug'].append([iteration,time_diff])
	else:
		d['cpp_release'].append([iteration,time_diff])
	#return time_diff
if __name__=='__main__':
	f=open("time_output.csv",'w')
	f.write("cpp_debug,cpp_release,python_file\n")
	write_decision=0
	for n in times:
		python_file="python nbody.py {} {}".format(n,write_decision)
		cpp_release="assignment4-dkcjnkyzvqzooafocrfpppdbrqki/Build/Products/Release/assignment4 {} {}".format(n,write_decision)
		cpp_debug = "assignment4-dkcjnkyzvqzooafocrfpppdbrqki/Build/Products/Debug/assignment4 {} {}".format(n,write_decision)
		'''p1 = Process(target=command_time,args=(cpp_debug,d,))
		p1.start()
		p2 = Process(target=command_time,args=(cpp_release,d,))
		p2.start()
		p3 = Process(target=command_time,args=(python_file,d,))
		p3.start()
		p1.join()
		p2.join()
		p3.join()'''
		command_time(cpp_debug)
		command_time(cpp_release)
		command_time(python_file)
		#f.write("{},{},{}".format(time_diff1,time_diff2,time_diff3))
	f.close()
	print(d)
	time_table = pd.DataFrame(data=d)
	print(time_table)
	for i in tuple(d.values()):
		x,y = zip(*i)
		x = list(x)
		y = list(y)
		plt.plot(x,y)
	plt.show()


