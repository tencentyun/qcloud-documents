Key features of the Global Application Accelerate Platform include acceleration proxy configuration, origin server management, acceleration data statistics, connection monitoring, and acquisition of real user IPs.
## Acceleration Proxy
- Acceleration connections can be configured based on the regions of destination users and origin servers. GAAP selects an optimal acceleration connection automatically according to the regions of the destination user and the origin servers. This connection is the shortest and the optimal path between the destination user and the origin server, which delivers a positive experience for real users. For more information, please see [Access Management](/document/product/608/13763).

- Forwarding via TCP and UDP is supported.
- Forwarding of URL rules is supported for HTTP and HTTPS.
- A listener can be bound with multiple origin servers, and a connection can be used to create multiple listeners.
- Configuration and change of connection forwarding rules are supported. The changes take effect in real time and do not affect online businesses.
- Flexible configuration of acceleration and forwarding rules within connections is supported to meet the needs of step-by-step verification scenarios during beta test. For more information, please see [Listener Management](/document/product/608/13764).

## Origin Server Management
- Manage massive origin servers by IP and domain name, and add them in batches.

## Data Statistics
- Provide statistics about acceleration connection bandwidth, concurrence, packet loss, delay, and packet forwarding. Adjust the limit of acceleration connection capacity as needed based on the actual statistics. For more information, please see [Statistical Data](/document/product/608/14425).

## Connection Monitoring
- Monitor the statuses of connections and origin servers. Trigger alerts in the event of irregularities to keep you abreast of the situation and help you resolve any issue promptly. For more information, please see [here](/document/product/608/17541).

## Acquisition of Real User IPs
- Obtain real user IPs via the TOA module. Ensure effective and transparent transmission of IPs to meet your needs of business data analysis. For more information, please see [here](/document/product/608/14427).

