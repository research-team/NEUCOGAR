import pylab

# path like "/home/alex/12636(test-thal-2000ms-52).out"
path = input("Enter the path to the .out")
# User param
max_bars = 54


cpu_data = {}
core_index = 0

# Read file
with open(path, 'r') as file:
	for line in file:
		if line.startswith("MPI"):
			a = line.split("  ")
			for data in a:
				if data.startswith("MPI"):
					del a[a.index(data)]
			del a[-1]
			cpu_data[core_index] = list(a)
			core_index +=1

# Check if user input is not valid by bars range
if max_bars <= 0:
	max_bars = 1
if max_bars > len(cpu_data[0]):
	max_bars = len(cpu_data[0])

# Set min/max time of the graphic
t_min = 0
t_max = len(cpu_data) * 10

# Draw
pylab.ioff()
pylab.figure()

for bar in range(len(cpu_data[0]))[:max_bars]:
	print("bar", bar, "done")
	cpu = []
	for key, data in cpu_data.items():
		cpu.append(data[bar])
	times = [ i*10 for i in range(len(cpu)) ]
	pylab.plot(times, cpu, "", label=bar, linewidth=0.7)

pylab.ylabel("CPU time (s)")
pylab.xlabel("Simulation time (ms)")
pylab.xlim([t_min, t_max])
pylab.legend(loc="best")
pylab.grid(True)
pylab.draw()
pylab.show()
