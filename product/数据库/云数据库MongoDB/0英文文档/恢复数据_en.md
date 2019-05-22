The steps for restoring cloud database MongoDB are as follows:

1. Enter the backup restoration list and click rollback action for a certain backup file, enter the password to initiate rollback.
![](https://mc.qcloudimg.com/static/img/93e3ebf30352f40ef89f850166d88ead/huifu.png)


2. The system will create a temporary instance to store rollback data.

3. Please access the temporary instance and verify rollback data within 48 hours after the rollback operation completes 
Then, perform one of the following actions: 

A. "Make Regular" Make the temporary instance a regular instance which is independent from the original instance .

B. "Replace" Replace the original instance using the temporary instance (The private IP of the original instance will be bound to the temporary instance) .

We will terminate the temporary instance if no action is performed within 48 hours .
The user name and password of the temporary instance are identical to those of the original instance.
![](https://mc.qcloudimg.com/static/img/4729ddc8384362dfb9a601343e928807/huifu2.png)

