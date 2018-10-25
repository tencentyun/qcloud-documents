## Renaming Instances
You can modify the instance name as needed. The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/0cffc15e8492c67596768921c809f5ee.png)
![](https://main.qcloudimg.com/raw/50f948972ab3b5fdf9950780dddc49e7.png)
## Oplog Capacity Adjustment
The default Oplog capacity is 10% of the storage capacity of the entire instance purchased. To prevent rollback failure caused by Oplog flushing, you can adjust the Oplog size as needed, which can be expanded to up to 90% of the instance capacity. The specific procedure is as follows:<br>
![](https://main.qcloudimg.com/raw/cbea67ae9f7f158ca3227932c4025022.png)
![](https://main.qcloudimg.com/raw/960b2ebc7da3c4dec5b1a8c4218df8d0.png)
## Instance Capacity Expansion
With the development of business, the MongoDB instance configuration may not be able to meet the business requirements. Then you can expand the instance capacity in the console. Capacity expansion includes computing resource expansion and storage expansion. You can choose to expand to higher node specifications and larger node capacity. Because Oplog is a capped collections, too small Oplog may be flushed easily. It is recommended to expand Oplog capacity while expanding the instance capacity. The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/1431188010f656c90d2e11b32a56ef5f.png)
![](https://main.qcloudimg.com/raw/1dd06176d8544498d331cbfd985ccbb5.png)
## Instance Restarting 
Restarting an instance means restarting mongos and mongod. If mongod is restarted when data is being written, a rollback may be caused and data may be lost. Restarting mongos and mongod may cause a flash disconnection, which is very risky. It is recommended to stop your business before restarting them. If you need to restart the instance, submit a ticket or apply for the whitelist.
## Instance Termination 
Postpaid MongoDB instances can be terminated by users. The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/7fb099ff4aa63a1160b055cfdca31144.png)
![](https://main.qcloudimg.com/raw/794a7d20867d683e9899a00c71876b18.png)
## Account Management
Go to the Instance Management page, and click **Account Management** to enter the sub-page. The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/5e7458e70608b906fb3c60b61d46c5f1.png)
### Account list 
The Account List page lists all the account details, including the account name, authentication method, creation time, modification time and operations. The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/e7f782bcf58ed15deb14d0c8790d879c.png)
### Creating an account 
You can create an account and allow it to have access to the database table. The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/81e67382632e8771bdcb0a83360233d4.png)
![](https://main.qcloudimg.com/raw/a9b9f75e2ebdb951fc53f8d03d1b7fdc.png)
### Changing account passwords 
The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/44216a3a917742837d0abdf10ee1b530.png)
![](https://main.qcloudimg.com/raw/f0f9f6022ee8d1b5b2c5b8600340a2d1.png)
### Deleting accounts 
The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/201f5cdfc8f83e2fffcca39c6d99ed10.png)
![](https://main.qcloudimg.com/raw/8fd633ef85ba6823645334083a3ccc1c.png)
### Changing account permissions 
The specific procedure is as follows:
![](https://main.qcloudimg.com/raw/5ffadc9ab1b93d6d3f474f1e2ad418b8.png)
![](https://main.qcloudimg.com/raw/e326bacaa202e1de6614c4396b3afce8.png)

