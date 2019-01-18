When using load balancing feature, you can configure the weight for resolution load.
### Configure Load Balancing for Resolution
You can achieve resolution load balancing for records with the same type, the same host name and the same line.
![](//mc.qcloudimg.com/static/img/51f1a5daa232d0b91db9ff5d2a5ac103/image.png)
### Check Load Balancing Page
Default load configuration is equalized, which means the authoritative server returns all record values in a random order, and the system takes the first IP address by default. Each resolution record has approximately the same chance to be taken.
![](//mc.qcloudimg.com/static/img/9cbe986b857e0cf7ff54e2e253b8ced6/image.png)
In this case, the weight is 0, and resolution ratio is equalized.
![](//mc.qcloudimg.com/static/img/a8a3180902b2040b91a97b33c2c04027/image.png)
### Modify Weight 
Click **Modify Weight** to configure a weight form 1 to 100. The authoritative server will return an IP node according to the configured weight.
![](//mc.qcloudimg.com/static/img/9cfcfd37f383173ed5bd2c7f5da8fe7d/image.png)

