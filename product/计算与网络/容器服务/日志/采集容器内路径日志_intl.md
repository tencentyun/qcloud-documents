## Collecting Logs of a Path in the Container

The log collection service does not allow you to collect log files directly from the file system in the container. To collect logs of a certain path in the container, you need to mount the directory in which the specified log file reside to the specified path of CVM in the format of "host path volume", and then collect the corresponding CVM path using the feature of collecting CVM log files.

## How to Make the Configuration

For example, application prints the log file to the file system path `/data/app-log/nginx.log` in the container. You can configure log collection rules as follows:

1. When creating an application, mount the path `/data/app-log/nginx` where the log file locates in the container to the CVM path `/var/log/nginx`.
![][1]
![][2]

2. Create a log collector and specify the collection path as `/var/log/nginx/*.log`, and specify a metadata to be attached (optional).
![][3]

3. Specify log receiver.
![][4]

4. Consume related Topic of Kafka to view collected logs.
![][5]

[1]:https://mc.qcloudimg.com/static/img/f260d93e0c77c2021543a0353b171d7e/image.jpeg
[2]:https://mc.qcloudimg.com/static/img/6a7219a31ac56be11b21fbcc23f6ef88/image.jpeg
[3]:https://mc.qcloudimg.com/static/img/8b5594d5bd36c4ee28f769fe1bc86301/4VA%7D2PX0SYKF%60B2P%7ENTICQG.png
[4]:https://mc.qcloudimg.com/static/img/0fe6bed71772b09231771e320a789e9d/image.jpeg
[5]:https://mc.qcloudimg.com/static/img/32f72a65f46f33d67a93d1a9a3f3e3d1/hostlogwithmetadata.jpeg





