SCF is billed by usage on a monthly postpaid basis. The bill for the current month is issued on the 3rd to 5th day of the next month and is settled in USD.

The monthly bill of SCF consists of three parts, with each calculated in a specific method based on the collected data. The calculated amount is in USD and retains two decimal places.

* Fee for resource usage 
* Fee for calls
* Fee for public network outbound traffic

## Fee for Resource Usage

**Fee for resource usage** = (**Resource usage** - **Free resource quota**) X **Resource unit price**

### Resource unit price

**Resource unit price: 0.0000167/GBs**

### Resource usage (GBs)

Resource usage = Memory configured for SCF X Charged running duration

Memory configured for SCF is calculated in GB, and charged duration is calculated in seconds (converted from milliseconds). So resource usage is calculated in **GBs** (GB-second).

For example, if SCF is configured with a memory of 256 MB and runs 1760 ms (calculated by 1800 ms) for each processing, the resources used in a single run are (256/1024) X (1800/1000) = 0.45 GBs.

Resources used in each run are calculated on a monthly basis.

## Fee for Calls

**Fee for calls** = (**Total number of calls** - **Free call quota**) X **Call unit price**

SCF is deemed called every time it is triggered to run. Collect the number of calls on a monthly basis and charge by a granularity of **1 million calls**.

### Call unit price

**Call unit price: 0.15 USD/million calls**


## Fee for Public Network Outbound Traffic

**Fee for public network outbound traffic** = **Public network outbound traffic** X **Traffic unit price**

When you access public network resources from SCF, such as uploading a file to an external storage, outbound traffic is generated.

For public network outbound traffic, you are also [charged by the actual traffic usage](https://cloud.tencent.com/document/product/213/10578#.E6.8C.89.E4.BD.BF.E7.94.A8.E6.B5.81.E9.87.8F.E8.AE.A1.E8.B4.B9).

### Unit price for public network outbound traffic

**Traffic unit price varies according to different regions**

Public network outbound traffic is calculated in GB. For traffic fees, please see below:

| Region | Unit | Price |
| --- |--- |---|
| China - Beijing, Shanghai, Guangzhou, Hong Kong) | GB | 0.12 USD/GB |
| North America | GB | 0.077 USD/GB |
| Singapore | GB | 0.081 USD/GB |
| Europe - Frankfurt | GB | 0.077 USD/GB |
| Europe - Moscow | GB | 0.13 USD/GB |
| Asia Pacific - Seoul | GB | 0.12 USD/GB |
| Asia Pacific - Mumbai, Bangkok | GB | 0.10 USD/GB |
| Asia Pacific - Tokyo | GB | 0.13 USD/GB |


## Fees for Other Products

If other products (such as CMQ, API gateway, and COS) are also used in addition to SCF, these products are billed according to their own billing rules.

