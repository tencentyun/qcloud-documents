## 1. API Description

This API (DescribeDeviceClass) is used to acquire the list of device classes.
Domain for API request: bm.api.qcloud.com




## 2. Input Parameters
None



## 3. Output Parameters

<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Common error code; 0: Succeeded; other values: Failed. For more information, please see <a href="/doc/api/456/6725" title="Common Error Codes">Common Error Codes</a> on the Error Codes page.
<tr>
<td> message
<td> String
<td> Module error message description depending on API.
<tr>
<td> data
<td> Object
<td> Array containing device class information. Information structure is shown in the table below.
</tbody></table>

</b></th>Device class information structure</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> deviceClass
<td> String
<td> Device class, such as M10, B6.
<tr>
<td> deviceClassDisplay
<td> String
<td> Displayed code for the device class.
<tr>
<td> useType
<td> String
<td> Type of usage scenario.
<tr>
<td> cpuDesc
<td> String
<td> CPU information.
<tr>
<td> memDesc
<td> String
<td> Memory information.
<tr>
<td> diskDesc
<td> String
<td> Hard disk information.
<tr>
<tr>
<td> nicDesc
<td> String
<td> NIC information.
<tr>
<td> canRaid
<td> Int
<td> Whether RAID is supported. 1: Yes. 0: No.
<tr>
<tr>
<td> pid
<td> Int
<td> Product ID of the device class.
<tr>
<tr>
<td> isSale
<td> Int
<td> Whether the device is for sale. 1: Yes. 0: No.
<tr>
<tr>
<td> discount
<td> Int
<td> Discount is the value of "discount/100".
<tr>
<tr>
<td> unitPrice
<td> Int
<td> Price of the device class before discount. (Unit: 0.01 CNY).
<tr>
<tr>
<td> realPrice
<td> Int
<td> Price of the device class after discount. (in 0.01 CNY).
<tr>
</tbody></table>



## 4. Module Error Codes

| code | codeDesc | Description |
|------|------|------|
| 9001 | InternalError.DbError | An error occurred when operating the database |
| 10001 | InvalidParameter | Invalid parameter |


## 5. Example
Input
<pre>
https://bm.api.qcloud.com/v2/index.php?
Action=DescribeDeviceClass
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>
Output
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "deviceClass": "B6",
            "deviceClassDisplay": "PC000",
            "useType": "Computing Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "64GB",
            "diskDesc": "2*300GB(SAS)",
            "canRaid": "1",
            "nicDesc": "Gigabit NIC",
            "pid": "10716",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "M1",
            "deviceClassDisplay": "PS000",
            "useType": "Standard Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "128GB",
            "diskDesc": "6*300G(SAS)",
            "canRaid": "1",
            "nicDesc": "Gigabit NIC",
            "pid": "10711",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "M10",
            "deviceClassDisplay": "PS100",
            "useType": "Standard Server",
            "cpuDesc": "E5-2670v3 (12-core)*2",
            "memDesc": "128GB",
            "diskDesc": "12*300GB(SAS)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10532",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "M10a",
            "deviceClassDisplay": "PM101",
            "useType": "Memory Server",
            "cpuDesc": "E5-2670v3 (12-core)*2",
            "memDesc": "384G",
            "diskDesc": "12*300GB(SAS)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10791",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "M2",
            "deviceClassDisplay": "PS001",
            "useType": "Standard Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "64GB",
            "diskDesc": "6*300G(SAS)",
            "canRaid": "1",
            "nicDesc": "Gigabit NIC",
            "pid": "10712",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "TS60",
            "deviceClassDisplay": "PI102",
            "useType": "Large Storage Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "64GB",
            "diskDesc": "12*2TB(SATA)+1*80GB(SSD)",
            "canRaid": "0",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10535",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "TS80",
            "deviceClassDisplay": "PI110",
            "useType": "High Performance Storage Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "64GB",
            "diskDesc": "4*1.8TB(SSD)+1*80GB(SSD)",
            "canRaid": "0",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10534",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "TS80a",
            "deviceClassDisplay": "PI111",
            "useType": "Storage Server",
            "cpuDesc": "E5-2670v3 (12-core)*2",
            "memDesc": "64G",
            "diskDesc": "4*1.8T(NVMe SSD) + 1*240G(SSD)",
            "canRaid": "0",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10822",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "TS90",
            "deviceClassDisplay": "PI100",
            "useType": "Balanced Storage Server",
            "cpuDesc": "E5-2670v3 (12-core)*2",
            "memDesc": "256GB",
            "diskDesc": "12*800GB(SSD)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10533",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "Y0-TS85-00",
            "deviceClassDisplay": "PI114",
            "useType": "Storage Server",
            "cpuDesc": "E5-2670v3 (12-core)*2",
            "memDesc": "512G",
            "diskDesc": "4*1.8T(NVMe SSD)  + 4*1.8T(SAS)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10810",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "Y1-B60-00",
            "deviceClassDisplay": "PC100",
            "useType": "Computing Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "64GB",
            "diskDesc": "2*300GB(SAS)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10717",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "Y1-TS30-00",
            "deviceClassDisplay": "PI105",
            "useType": "Storage Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "128GB",
            "diskDesc": "12*4T(SATA)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10720",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "Y1-TS30-11",
            "deviceClassDisplay": "PI104",
            "useType": "Storage Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "64GB",
            "diskDesc": "8*2T(SATA)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10719",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        },
        {
            "deviceClass": "Z30",
            "deviceClassDisplay": "PI103",
            "useType": "Storage Server",
            "cpuDesc": "E5-2620v3 (6-core)*2",
            "memDesc": "128GB",
            "diskDesc": "4*600G (SAS)+1*1.2T (High-performance SSD PCIE card)",
            "canRaid": "1",
            "nicDesc": "Ten-Gigabit NIC",
            "pid": "10715",
            "isSale": "1",
            "discount": 100,
            "unitPrice": 310000,
            "realPrice": 310000
        }
    ]
}
```


