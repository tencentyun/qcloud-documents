## Application Scenarios
Users can select NAT mode or EIP direct connection mode when accessing the public network with EIP. Default is NAT mode.
- EIP is invisible on the local machine in NAT mode.
- EIP is visible on the local machine in EIP direct connection mode. You do not need to add the EIP address manually for each configuration to minimize development cost.

> **Note:**
> EIP direct connection is subject to the whitelist, and only supports devices in the VPC.

## Procedure
### 1. Download EIP configuration script
Since EIP direct connection may cause network interruption, you need first to download EIP direct connection script and upload it to CVM. The steps are as follows:
(1) Download the configuration script of EIP direct connection (optional). Download path:
 - [Download Script for Linux](https://mc.qcloudimg.com/static/archive/e66c8253642e37c62c8e581d6f0299de/eip_linux.zip)
 - [Download Script for Windows](https://mc.qcloudimg.com/static/archive/af1eee0dbe7d9407cddb3e1bd510cb3a/eip_windows.zip)
> Note:
> Script for Linux supports CentOS 6.x, CentOS 7 and Ubuntu.

(2) After the script is downloaded, upload it to the CVM that requires to enable EIP direct connection.

### 2. Run EIP direct connection script
(1) Log in to the CVM that requires EIP direct connection.

(2) Run EIP direct connection script. Method:

 - In CentOS Linux:
```
eip_linux.sh install XX.XX.XX.XX 
```
`XX.XX.XX.XX` represents the EIP address (optional).

 - In Windows:
```
eip_windows.bat XX.XX.XX.XX
```
`XX.XX.XX.XX` represents the EIP address.

### 3. Enable EIP direct connection
(1) Log in to the [CVM console](https://console.cloud.tencent.com/cvm/overview).

(2) In the left navigation pane, click **EIP**.

(3) Click **EIP Direct Connection** button in the **Operation** column of the list to enable EIP direct connection.



> **Note:**
- The script supports eth0 only, but not secondary ENI.
- NAT gateway can be bound with EIPs enabled with direct connection, but direct connection cannot be implemented.

