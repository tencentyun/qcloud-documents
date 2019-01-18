Tencent Cloud Monitor provides the following monitoring metrics for direct connect tunnel:

| Indicator | Name      | Description                                     | Unit   | Dimension           | Statistical Method |
| ----- | ---------- | ---------------------------------------- | ---- | ------------ | ---- |
| Inbound traffic   | intraffic  | The inbound traffic from access point AR to VPC collected every 1 minute or 5 minutes       | KB   | unInstanceId | max  |
| Outbound traffic   | outtraffic | The outbound traffic from VPC to access point AR  collected every 1 minute or 5 minutes       | KB   | unInstanceId | max  |
| Inbound packets   | inpkg      | Number of inbound packets per second from access point AR to VPC collected every 1 minute or 5 minutes | pck/sec  | unInstanceId | sum  |
| Outbound packets   | outpkg     | Number of outbound packets per second from VPC to access point AR collected every 1 minute or 5 minutes | pck/sec  | unInstanceId | sum  |


For more information about how to use the monitoring metrics of direct connect tunnel, please see the API [Read Monitoring Data](https://cloud.tencent.com/document/product/248/4667) in the Cloud Monitor API.
