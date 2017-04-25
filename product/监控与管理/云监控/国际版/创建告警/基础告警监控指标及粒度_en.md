## CVM Metrics
<table class="t">
<tbody><tr>
<th> <b>Metric Name</b>
</th><th> <b>Unit</b>
</th><th> <b>Range</b>
</th><th> <b>Monitoring Granularity</b>
</th></tr>
<tr>
<td> CPU utilization
</td><td>&nbsp;%
</td><td> [0,100]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Machine reboot
</td><td> -
</td><td> -
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Unreachable ping
</td><td> -
</td><td> -
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Memory utilization
</td><td>&nbsp;%
</td><td> [0,100]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Memory usage
</td><td> MB
</td><td> [0,1000000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Read-only disk
</td><td> -
</td><td> -
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Disk utilization
</td><td>&nbsp;%
</td><td> [0,100]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Disk read traffic
</td><td> KB/s
</td><td> [0, 100000000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Disk write traffic
</td><td> KB/s
</td><td> [0, 100000000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Disk IO wait
</td><td> ms
</td><td> [0,3600000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Inbound traffic of public network
</td><td> bps
</td><td> [0, 10000000000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Outbound traffic of public network
</td><td> bps
</td><td> [0, 10000000000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Inbound packets of public network
</td><td> count
</td><td> [0, 100000000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Outbound packets of public network
</td><td> count
</td><td> [0, 100000000]
</td><td> 1 minute/5 minutes
</td></tr>
<tr>
<td> Public network bandwidth utilization
</td><td>&nbsp;%
</td><td> [0,100]
</td><td> 1 minute/5 minutes
</td></tr></tbody></table>

## Cloud database metrics
<table class="t">
<tbody><tr>
<th> <b>Metric Name</b>
</th><th> <b>Unit</b>
</th><th> <b>Range</b>
</th><th> <b>Monitoring Granularity</b>
</th></tr>
<tr>
<td> Total disk capacity
</td><td> MB
</td><td> [0,9999999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Real disk capacity
</td><td> MB
</td><td> [0,9999999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Disk utilization
</td><td>&nbsp;%
</td><td> [0,100]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Number of full table scans
</td><td> Counts per second
</td><td> [0,99999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Number of slow queries
</td><td> Counts per second
</td><td> [0,99999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Number of current connections
</td><td> count
</td><td> [0,99999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Amount of data received
</td><td> Byte/second
</td><td> [0,9999999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Amount of data delivered
</td><td> Byte/second
</td><td> [0,9999999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Total visits
</td><td> Counts per second
</td><td> [0,999999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Percentage of visits
</td><td>&nbsp;%
</td><td> [0,100]
</td><td> 5 minutes
</td></tr></tbody></table>

## VPN Tunnel Metrics
<table class="t">
<tbody><tr>
<th> <b>Metric Name</b>
</th><th> <b>Unit</b>
</th><th> <b>Range</b>
</th><th> <b>Monitoring Granularity</b>
</th></tr>
<tr>
<td> Tunnel delay
</td><td> ms
</td><td> [0,9999]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Tunnel packet loss rate
</td><td>&nbsp;%
</td><td> [0,100]
</td><td> 5 minutes
</td></tr>
<tr>
<td> VPN outbound bandwidth
</td><td> Mbps
</td><td> [0,1000]
</td><td> 5 minutes
</td></tr>
<tr>
<td> VPN inbound bandwidth
</td><td> Mbps
</td><td> [0,1000]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Whether the tunnel is clear
</td><td> -
</td><td> -
</td><td> 5 minutes
</td></tr></tbody></table>

## CDN Metrics
<table class="t">
<tbody><tr>
<th> <b>Metric Name</b>
</th><th> <b>Unit</b>
</th><th> <b>Range</b>
</th><th> <b>Monitoring Granularity</b>
</th></tr>
<tr>
<td> Traffic
</td><td> Mbps
</td><td> [0, +1000000000]
</td><td> 5 minutes
</td></tr>
<tr>
<td> Number of requests
</td><td> count
</td><td> [0, +1000000000]
</td><td> 5 minutes
</td></tr></tbody></table>
