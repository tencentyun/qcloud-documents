### How is Direct Connect product charged?
The charges for Direct Connect product include:


- Laying fee of physical Direct Connect, which is charged by ISP or Tencent Cloud Direct Connect partner.
- One-off fee for connection to Tencent Cloud: 2,500 USD, including Tencent Cloud port fee and test fee.
- Fee for cross-city Direct Connect tunnel. For more information on charging standard, please see Price Overview.


### How to cancel Direct Connect?
Direct Connect services to be cancelled include:
1. Physical Direct Connect: You need to submit an application for cancellation to the ISP;
2. Direct Connect Tunnel: You can apply to delete the Direct Connect tunnel in the console, and the fee for cross-city Direct Connect tunnel of that month is deducted at the beginning of next month;



### What is the billing method for creating multiple tunnels in non-VLAN mode?
If multiple tunnels are created without sub-APIs enabled (VLAN mode), these tunnels share the traffic bandwidth of a physical port, that is, the traffic data of all the tunnels in this physical Direct Connect cannot be distinguished.

For the postpaid billing based on Monthly 95th Percentile, if multiple tunnels are created for a physical Direct Connect in non-VLAN mode, including inter-city/cross-city tunnels, the physical Direct Connect is charged as follows:

1. Object: Only the Direct Connect tunnel with the highest unit price is charged for this physical Direct Connect.
2. Payment method: According to Monthly 95th Percentile billing for Direct Connect tunnel, the tunnel is billed on a monthly basis by calculating monthly 95th percentile bandwidth with the traffic collected from the physical port of this physical Direct Connect.

Therefore, intra-city Direct Connect may be charged in non-VLAN mode. It is recommended to use VLAN mode to cut cost.

