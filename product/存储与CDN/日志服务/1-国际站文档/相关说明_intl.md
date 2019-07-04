## Network Environment
### Private network environment

If you are using a Tencent Cloud CVM, and it resides in the same region with the logset in the CLS, then the log data is collected via the private network, and no traffic is generated on the CVM. Therefore, you are recommend to use the CLS in the same region with your business.

### Public network environment
If you are using an external server (not a Tencent Cloud CVM), or if your Tencent Cloud CVM is not in the same region with the logset, the public network is used, and public network traffic is generated on your server.

## Relevant Metrics
- Collection latency: 2 seconds.
- The latency it takes for the collection configuration change takes effect: within 1 minute.
- Maximum log volume: 16 MB/sec.
- Maximum length: 512 KB for a log. If this length is exceeded, the log is truncated to 512 KB and will not be collected.
- Maximum number of connections: 1,024.
- Memory usage: 50 MB at the most in general, and 150 MB in case of a failure of backend service.
- CPU usage: Not more than 20% of single-core CPU for all three processes if log volume is kept at 5 MB/sec.

## Version Limits
- Full text in multi lines is not supported for LogListener below version 2.1.4.
- Log structuring is not supported for LogListener below version 2.1.1.
- You need to exit from the LogListener below version 2.0.0 and update it by downloading and installing the latest version.

