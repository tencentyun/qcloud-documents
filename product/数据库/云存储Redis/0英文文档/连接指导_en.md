When connecting Tencent Redis after instance initialization, you need to enter the password set before. Here are sample master/slave instance and cluster instance connections:

#### Master/Slave Instance Connection Example
Master/slave instance supports two formats
• Format 1:"Instance id:password". For example, if your instance id is crs-bkuza6i3 and the password is abcd1234, the connection command is
```redis-cli -h IP address -p port -a crs-bkuza6i3:abcd1234```

• Format 2: Open source format. For example, if the password is abcd1234, the connection command is
```redis-cli -h IP address -p port -a abcd1234```
**(Note: Only master/slave instances purchased after June 28, 2017 support access of Format 2)**

<br>

#### Cluster Instance Connection Example
Cluster instance only supports the following password format:
• "Instance id:password". For example, if your instance id is crs-bkuza6i3 and the password is abcd1234, the connection command is
```redis-cli -h IP address -p port -a crs-bkuza6i3:abcd1234```
<br>
#### Note
• Tencent Cloud Redis does not support passwordless access
