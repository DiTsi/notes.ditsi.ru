# taskset

If your system is multiprocessor, sometimes you may need to ensure that a running process is only served by a specific processor or group of processors. All this can be done easily and simply using the taskset utility.

Taskset allows you to "bind" a process to a specific processor. Let's imagine that you want to configure Google Chrome so that it runs on only one CPU. This is done with the command:

Quote:
taskset 0x00000001 google-chrome
Now the CPU usage for google-chrome will be limited to the first CPU only (mask 0x00000001 denotes the first CPU). If, for example, you want the process to run on the first and second CPU, use the command:

Quote:
taskset 0x00000003 google-chrome
Instead of masks, you can use the -c option of the taskset utility.

If you want to find out which processors a particular process is running on, you can use the command:

Quote:
set of tasks -p XXXX
where XXXX replace this with the PID of the process you are interested in. For example, if you get information about a process that has not been bound, on a dual-processor system, you will see a value of three.

Can a set of tasks be useful to you to improve the performance of your system and is it worth using it all the time? No. However, a task set can be of great help when you are dealing with applications that may be causing problems on your system.