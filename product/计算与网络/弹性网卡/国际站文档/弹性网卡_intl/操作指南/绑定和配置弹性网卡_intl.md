**Step 1: Log in to the [VPC Console](https://console.cloud.tencent.com/vpc).**

**Step 2: Click **ENI** in the left sidebar to go to the ENI list page.**

**Step 3: Locate the line of the ENI, and click **Bind to CVM** in the operation column (only CVMs in the same availability zone as the ENI are supported).**

**Step 4: Select the CVM to bind to and click **OK** to complete the binding.**



**Step 5: Configure the bound ENI in the CVM (important)**
>Note: After being bound on the console, the ENI needs to be configured in the CVM before it can be used normally. The following is the operation procedure for centos 7.2:

a. Log in to the CVM as an administrator, and execute the following command:


`cd /etc/sysconfig/network-scripts/`


b. Create the configuration file ifcfg-eth1 for the new ENI:

Enter the command:

`cp ifcfg-eth0 ifcfg-eth1`


Enter the command to modify the configuration file:

`vim ifcfg-eth1`

Modify the configuration file as follows:


`DEVICE='eth1'`

`NM_CONTROLLED='yes'`

`ONBOOT='yes'`

`IPADDR='192.168.1.62'  #Enter the actual address of the ENI`

`NETMASK='255.255.255.192'  #Enter the actual subnet mask`

`GATEWAY='192.168.1.1'  #Enter the actual gateway`


Save the modified configuration file and exit (enter "wq!" in the last line of vim and press Enter).


**Step 6: Disable rp_filter check**


Disable reverse path filtering in etc/sysctl.conf.

> Note: Reverse path filter means that when receiving an IP packet from an IP, the system checks whether the source IP is valid and discards the IP packet if the source IP is invalid. For example, an IP packet from IP B is received on ENI A. If ENI A is not the ENI intended for sending data to IP B, this IP packet is discarded. Because the route uses the primary ENI by default, after the reverse path filtering is enabled, the Ping test of the IP on the secondary ENI will fail.

Open the configuration file:

`vim /etc/sysctl.conf`

Modify

`net.ipv4.conf.default.rp_filter = 1`

to:

`net.ipv4.conf.default.rp_filter = 0`
`net.ipv4.conf.all.rp_filter = 0`
`net.ipv4.conf.eth0.rp_filter = 0`
`net.ipv4.conf.eth1.rp_filter = 0`

**Step 7: Restart network service**

Enter the following command:

`systemctl restart network`

**Step 8: Check and verify**

Enter the following command to check the IP

`ip addr`

Verify whether the secondary ENI and the IP on it are visible. Refer to the figure below:

![](https://mc.qcloudimg.com/static/img/682c0cda0fcbdbdb508785b12e102b4a/ip.png)