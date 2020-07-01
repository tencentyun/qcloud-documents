To ensure proper running of host security service, the Cloud Security option is selected by default when you are purchasing your CPM, in which case security components will be directly installed without your further actions. If the Cloud Security option is not selected when you purchase CPM, you may download and install the component by following the steps below: 

Step 1: Log in to the CPM and download the installation package into the host.

wget http://mirrors.tencentyun.com/install/sec_bm/agent.zip 

Step 2: Decompress the installation package.

 ![](https://mc.qcloudimg.com/static/img/ef729e5387b38f2d8aaed3d50dc0065c/image.png)

Step 3: Execute the installation script: sh install.sh 
 <br>The following result indicates a successful installation:  <br>[RESULT] sec-agent install OK
![](https://mc.qcloudimg.com/static/img/ba3378b68c30648276d7bb1ca002003c/image.png) <br>The following result indicates a failed installation. Please contact customer service for technical support.
 
<br>[RESULT] sec-agent install NOT OK

In Linux operating system, users may check the status of components by using script shown below:

Execute script to check component with administrator account.
/usr/local/sa/agent/check.sh

The following result indicates that the security component is functioning properly [RESULT] sec-agent running OK
![](https://mc.qcloudimg.com/static/img/b28883269f2deb18a5791ce4f3ea412b/image.png)

If the result is "sec-agent agent connection NOT OK", please see if the agent is installed on the same day. If yes, wait for one hour before checking it again--the security component is still connecting. If not, contact customer service for technical support. 

The result "[RESULT]sec-agent running NOT OK,FIX OK" indicates that the security component has been successfully repaired.

