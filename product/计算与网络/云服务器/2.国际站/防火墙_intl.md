### For Linux system, how to configure firewall software iptables?
> **Note:**
> iptables is quite different before and after CentOS 7.
> - Prior to CentOS 7, the iptables service was used as a firewall by default. Using the `service iptables stop` code, the iptables service clears the rules first and then unmount the iptables module. When it starts again, rules are loaded from the configuration file. When you stop the iptables service, you can test whether the firewall is restricted.
> ![](https://main.qcloudimg.com/raw/4a404e0187b0ee677034c0df82468e4a.png)
> - After CentOS 7, the firewall service is used as firewall by default. For compatibility, the iptables_filter module is also loaded, but the iptables service is not available. So after CentOS 7, you can add rules using the iptables command, but the iptables service is disabled by default. The user confirms that the iptable_filter module is loaded and the rules take effect.

The most secure method for learning the firewall is `iptables -nvL`. 
Here are two examples on how to configure: 
#### Scenario 1
For Ubuntu 14 system, the security group and listening port are opened, but telnet does not work.
Inbound rule of security group:
![](https://main.qcloudimg.com/raw/ef640902a0e0c78af6c07eb7102bb0d7.png)
Outbound rule of security group:
![](https://main.qcloudimg.com/raw/03a960f82b6e88fdca9aff8f10d76f4c.png)
telnet does not work:
![](https://main.qcloudimg.com/raw/74c521a97d4b9dab64b85ce62ab2cf86.png)
#### Solutions
1. First, capture the packets of CVM to determine if packets have reached the CVM.
 - If they do not reach the CVM, they may be blocked by the security group or the upper tgw and the ISP.
 - If packets reach the CVM, but there is a problem with return packets, it is most likely caused by the iptables policy within CVM. As shown below, there is no TCP packet back to 64.11 after telnet operation.
![](https://main.qcloudimg.com/raw/1052893022c8786a9b7b0166a57ce16d.png)  

2. After confirming it is the iptables policy problem, confirm whether the policy opens port 8081 to Internet via `iptables -nvL`. Here this port is not opened to Internet. 
![](https://main.qcloudimg.com/raw/bccfca60e3d707ae61c5ba236bf088f8.png) 
3. Use the command to add the policy to open port 8081 to Internet.
```
iptables -I INPUT 5 -p tcp  --dport 8081 -j ACCEPT
```
4. Port 8081 is tested to be opened. The problem is solved.  


#### Scenario 2
In terms of iptables configuration, the policy has been opened to Internet, but the destination server still cannot be pinged.
![](https://main.qcloudimg.com/raw/46fdf4e20187c5b366c7773d73eb1cee.png)
#### Solutions
If the following cases occur:
![](https://main.qcloudimg.com/raw/d1b01f74223ed34c78a789dc43d53bc8.png)
Use the command to delete the first rule in the output direction:
```
iptabels -D OUTPUT 1
```
The problem is solved after testing.

### How to clear the firewall?
#### Windows instance:
1. After logging in to the instance, click **Start** -> **Control Panel** -> **Firewall Settings** to enter the firewall settings page.

2. Check whether the firewall and other security software (such as Safedog) are enabled. If enabled, disable them.

#### Linux instance:
1. Run the command to check whether the client has enabled the firewall policy. If not, skip Step 2 and go directly to Step 3:
```
iptables -vnL
```

2. If the firewall policy is enabled, run the command to back up the current firewall policy:
```
iptables-save
```

3. Run the command to clear the firewall policy.
```
iptables -F
```

### Will CVM acceleration using non-Tencent Cloud CDN be blocked by the firewall?
No. If you are concerned about the impact, you can disable the firewall.
