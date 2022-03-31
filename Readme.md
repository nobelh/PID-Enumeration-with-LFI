# Enumerating Linux Processes Through LFI

I've wrote this Python script to enumerate Linux processes through the Proc File System leveraging a LFI vulnerabilty on a web application.

### The parameters passed to the script are:

| **URL** | The web application URL including the vulnerable parameter. |
| **Max PID Count** | The maximum number of PIDs to try starting from 1. |
| **Proc File** | Name of the file we want to read from inside the PID subdirectory. |
| **Output File** | Name of the output file. |

### Here's screenshot of the script and output file:

![](https://github.com/nobelh/PID-Enumeration-with-LFI/blob/main/pidlfi5.png)