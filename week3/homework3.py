#1st task

#2nd task
import numpy as np

def arr_replace(arr_inp):
	arr_inp = np.array(arr_inp)
	return np.where((arr_inp%2==0), 0, arr_inp) 
 
print(arr_replace([1,2,3,4]))

#3rd task
import numpy as np

def arr_repeat(arr):
	return np.repeat(np.array(arr), 3)

print(arr_repeat([1,2,3]))

#4rth task
import numpys np

def arr_join(arr):
	return np.concatenate([np.array(arr), np.array(arr)])

print(arr_join([1,2,3,1,1]))

#5th task
import numpy as np

def arr_intersection(arr1, arr2):
	arr_bool = [np.intersect1d(arr1, arr2)]
	for false in arr_bool:
		return false

print(arr_intersection([1,1,2], [2,1,1]))

#6th task
import numpy as np

def arr_random(N = 2):
	return 5* np.random.random((N, N)) + 5

print(arr_random())
