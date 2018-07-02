SCF is billed by usage on a monthly postpaid basis. The bill for the current month is issued on the 3rd to 5th day of the next month and is settled in CNY.

The monthly bill of SCF consists of three parts, with each calculated in a specific method based on the collected data. The calculated amount is in CNY and remains two digits after the decimal point.

* Resource usage fee 
* Fee of number of calls
* Fee of public network outbound traffic

## Resource Usage Fee

**Resource usage fee** = (**Resource usage** - **Free resource quota**) X **Resource unit price**

### Resource unit price

**Resource unit price: 0.000115 CNY/GBs**

### Resource usage (GBs)

Resource usage = Memory configured for SCF X Charged running duration

Memory configured for SCF is calculated in GB, and charged duration is calculated in seconds (converted from milliseconds). So resource usage is calculated in **GBs** (GB-second).

For example, if SCF is configured with a memory of 256 MB and runs 1760 ms (calculated by 1800 ms) for each processing, the resources used in a single run are (256/1024)*(1800/1000) = 0.45 GBs.

Resources used in each run are calculated on a monthly basis.

## Fee of Number of Calls

**Fee of number of calls** = (**Total number of calls** - **Free call quota**) X **Call unit price**

SCF is deemed called every time it is triggered to run. Collect the number of calls on a monthly basis and charge by a granularity of **1 million calls**.

### Call unit price

**Call unit price: 1.38 CNY/million calls**


## Fee of Public Network Outbound Traffic

**Fee of public network outbound traffic** = **Public network outbound traffic** X **Traffic unit price**

When you access public network resources from SCF, such as uploading a file to an external storage, outbound traffic is generated.

For public network outbound traffic, you are also [charged by the actual traffic usage](https://cloud.tencent.com/document/product/213/10578#.E6.8C.89.E4.BD.BF.E7.94.A8.E6.B5.81.E9.87.8F.E8.AE.A1.E8.B4.B9).

### Unit price of public network outbound traffic

**Traffic unit price: 0.8 CNY/GB**

Public network outbound traffic is calculated in GB. For traffic fees, please see [Bill-by-traffic](https://cloud.tencent.com/document/product/213/10579#.E6.8C.89.E6.B5.81.E9.87.8F.E8.AE.A1.E8.B4.B9).


## Fees of Other Products

If other products (such as CMQ, API gateway, and COS) are also used in addition to SCF, these products are billed according to their own billing rules.

