Cloud Monitor of Tencent Cloud provides the following monitoring metrics for Cloud Load Balancing(CLB):

## Cloud Load Balancer Instance Monitoring Metrics

<table class="t"><tbody><tr>
<th><b>Metric Name </b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> Active Connection 
<td> rrv_connum
<td> count
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Inactive Connection 
<td> rrv_inactive_conn
<td> count
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Inbound Packet 
<td> rrv_inpkg
<td> count/s
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Inbound Traffic 
<td> rrv_intraffic
<td> bps
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> New Connection 
<td> rrv_new_conn
<td> count
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Outbound Packet 
<td> rrv_outpkg
<td> count/s
<td> Back-end CVM IP, back-end CVM port, and VPC ID
<tr>
<td> Outbound Traffic 
<td> rrv_outtraffic
<td> bps
<td> Back-end CVM IP, back-end CVM port, and VPC ID
</tbody></table>

## Backend CVM Monitoring Metrics

<table><tbody><tr>
<th><b>Metric Name</b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> Active Connection
<td> rv_connum
<td> count
<td> Backend CVM IP and VPC ID
<tr>
<td> Inactive Connection
<td> rv_inactive_conn
<td> count
<td> Back-end CVM IP and VPC ID
<tr>
<td> Inbound Packet
<td> rv_inpkg
<td> count/s
<td> Backend CVM IP and VPC ID
<tr>
<td> Inbound Traffic
<td> rv_intraffic
<td> bps
<td> Backend CVM IP and VPC ID
<tr>
<td> New Connection
<td> rv_new_conn
<td> count
<td> Back-end CVM IP and VPC ID
<tr>
<td> Outbound Packet
<td> rv_outpkg
<td> count/s
<td> Backend CVM IP and VPC ID
<tr>
<td> Outbound Traffic
<td> rv_outtraffic
<td> bps
<td> Backend CVM IP and VPC ID
</tbody></table>

## Backend CVM Port-level Monitoring Metrics

<table class="t"><tbody><tr>
<th><b>Metric Name</b></th>
<th><b>Description</b></th>
<th><b>Unit</b></th>
<th><b>Dimension</b></th>
<tr>
<td> Active Connection (port-level)
<td> rrv_connum
<td> count
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Inactive Connection (port-level)
<td> rrv_inactive_conn
<td> count
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Inbound Packet (port-level)
<td> rrv_inpkg
<td> count/s
<td> Backend CVM IP, back-end CVM port, and VPC ID
<tr>
<td> Inbound Traffic (port-level)
<td> rrv_intraffic
<td> bps
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> New Connection (port-level)
<td> rrv_new_conn
<td> count
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Outbound Packet (port-level)
<td> rrv_outpkg
<td> count/s
<td> Backend CVM IP, backend CVM port, and VPC ID
<tr>
<td> Outbound Traffic (port-level)
<td> rrv_outtraffic
<td> bps
<td> Backend CVM IP, backend CVM port, and VPC ID
</tbody></table>


For more information about the monitoring metrics of Cloud Load Balancing, please see [Read Monitoring Data API](https://cloud.tencent.com/doc/api/405/4667) in the Cloud Monitor API.


