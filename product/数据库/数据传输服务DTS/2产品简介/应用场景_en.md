
# Application Scenario #
### Remote Disaster Recovery for Cloud Database ###
TencentDB Service for Transmission (DTS) is capable of providing disaster recovery synchronization based on Tencent private direct connection for cloud database disaster recovery instances. The disaster recovery architecture allows mutual redundancy of different data centers in multiple regions such that when any data center goes down or fails to provide service due to any force majeure, the service can be quickly switched to another data center.

DTS optimizes database replication and greatly reduces synchronization delay between master/slave databases, thereby reducing the risk of data loss caused by synchronization delay during disasters to the utmost extent.
![][img1]

### Migrate Data onto Cloud ###
The data migration feature offered by DTS is the best choice for migrating data onto cloud. Data migration only requires several steps of configuration to help you complete complicated activities for migrating your local data onto the cloud. The migration process does not prevent your source database from providing external service, thereby minimizing the effect on your business caused by the cloud migration task.
![][img2]

### Local IDC Disaster Recovery ###
DTS allows data synchronization by using a local IDC as business center while using Tencent Cloud as disaster recovery center. This feature, together with the out-of-the-box cloud service, allows you to easily implement disaster recovery for a local IDC without the need for huge investment on infrastructures in advance.
![][img3]

### Data Archiving and Storage ###
By using the data subscription feature offered by DTS, you can push incremental update data from a cloud database to an archive database or data warehouse in the form of data streams.
![][img4]


[img1]: //mc.qcloudimg.com/static/img/bf6360c3cccb86e54391288c9e9b33bf/DTS-scenarios2.png
[img2]: //mc.qcloudimg.com/static/img/bbe90cec1fc0882e05c441ac38089295/image.png
[img3]: //mc.qcloudimg.com/static/img/7459283867e3acbcb4bff4e5b8481d31/DTS-scenarios3.png
[img4]: //mc.qcloudimg.com/static/img/6bc58a2088159ccb0264765a4f2e922e/DTS-scenarios4.png
