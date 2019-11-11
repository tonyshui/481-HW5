#!/usr/local/bin/python3
import sys
import os

def union(a,b):
	return list(set(a) | set(b))


def dd(p, test, script): #subset, test are both arrays
	#print(test)
	#print('dd(p= ' + str(p) + ' ,  c= ' + str(test) + " )")
	if len(test) == 1:
		return test

	p1 = test[:len(test)//2]
	p2 = test[len(test)//2:]

	if (run(script, union(p, p1)) != 0): #it's interesting!
		return dd(p, p1, script)
	if (run(script, union(p, p2)) != 0):
		return dd(p, p2, script)
	else:
		return union(dd(union(p,p2),p1, script), dd(union(p,p1),p2,script))


def enumerate(size):
	subset = []
	for i in range(0, size):
		subset.append(i)
	return subset


def run(bash_command, subset):
	#convert list into string
	#print(subset)

	#subset_string = list_to_string(subset)
	# print(subset_string)
	# print(subset_string)
	# print(len(subset_string))
	cmd = bash_command
	for case in subset:
		cmd = cmd + ' ' + str(case)
	#print('calling ' + cmd)
	return os.system(cmd)


def main():
	size = sys.argv[1]
	script = sys.argv[2]
	initial = enumerate(int(size))
	minimal_subset = dd([], initial, script)
	minimal_subset.sort()
	print(minimal_subset)
	return minimal_subset


# We will evaluate your delta.py implementation in terms of the correct answers it generates (i.e., the one-minimal interesting subsets) and also in terms of the number of probes (i.e., calls to is-interesting.sh).

if __name__ == "__main__":
	main()