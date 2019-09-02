IPsec VPN is a method you can use to connect VPC through public network encrypted tunnel.  VPC IPsec VPN connection consists of the following components:

- 	VPN gateway: An IPsec VPN gateway in the VPC, created in the console
- 	Peer gateway: An IPsec VPN service gateway of your IDC data center
- 	VPN tunnel: An encrypted Public IPsec VPN tunnel

IPsec VPN can be fully customized in the console. You need to configure your IPsec VPN gateway before enabling the tunnel.

Tencent Cloud IPsec VPN gateway consists of two virtual sub-machines (a master and a slave). If the master fails, the slave will take over in less than 1.5 seconds.
