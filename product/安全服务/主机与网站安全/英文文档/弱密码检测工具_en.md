To acquire weak password checking tool, follow steps below:

Step 1: Log in to the CVM and download the package into the CVM server. Download command is as follows:
wget mirrors.tencentyun.com/install/sec/qcloud-checkpassword.zip 

Step 2: Decompress unzip qcloud-checkpassword.zip. The tool consists of three parts: the binary program checklocalpasswd, the script check.sh and the weak password library.

Instructions:

1. check.sh mainly contains encapsulated default configurations for checklocalpasswd. You can start the process simply by executing the script. The time required for the process depends on the size of your machine and the password library. By default, the script initiates 5 processes to check password simultaneously, and each process takes up to 20% CPU.
2. The binary file checklocalpasswd is the actual program for checking weak password. You can view the instructions for this binary program by using the -h parameter. Main parameters are shown below.
Table 1 Parameter Description
![](//mccdn.qcloud.com/img56c635604f16c.png)
3. Users may add passwords into the weak password library file (one weak password each line).
Example for using the program is shown in the figures below:
Figure 1 Start of Process
![](//mccdn.qcloud.com/img56c635765255b.png)
Figure 2 End of Process
![](//mccdn.qcloud.com/img56c63594ba228.png)
Figure 3 Information about Weak Password
![](//mccdn.qcloud.com/img56c635a806bb0.png)
