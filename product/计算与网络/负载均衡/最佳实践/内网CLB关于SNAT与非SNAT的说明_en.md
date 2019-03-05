Starting from December 15th, 2016, newly purchased private network-based Cloud Load Balancers under Virtual Private Cloud (choose private network VPC) will no longer undergo SNAT processing, that is, the access IP received from server end is the real client IP. To ensure that your business operates properly, please note the followings:

1. For private network-based CLB newly purchased after 15th, after security group policy is enabled, you must allow all inbound rules of client IPs to ensure normal access.

2. If necessary, you can switch the existing private network-based CLB to the new one by submitting a ticket to the after-sales team. After the switching, the access IP acquired from the server side is the client IP. Your business will not be interrupted during the switching process
