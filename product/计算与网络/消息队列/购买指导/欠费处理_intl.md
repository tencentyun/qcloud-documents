## Arrears Processing

1. If your account has been in arrears for less than two hours, CMQ is still available.

2. Two hours later, CMQ service is suspended (only query for details is available).

3. After CMQ is suspended, all features of CMQ become unavailable. When the account balance has been topped up to an amount greater than 0, CMQ service will become available. Unprocessed and accumulated message data will be automatically released based on the expiration time of the message set in the queue, and the released data cannot be recovered. If all messages in the queue have expired, the queue will be deleted automatically.

4. Tencent Cloud account creator and all the collaborators are notified of the deletion of CMQ queues via email and SMS.


## Notes

1. After CQM messages have been removed, the data is cleared and cannot be recovered.

2. Since your actual resource consumption changes from time to time, some errors in balance alerts may exist.

3. The attribute "msgRetentionSeconds" of the queue identifies the number of seconds for which the message can be retained in the queue. The message is deleted after this time has elapsed since the message has been sent to this queue, regardless of whether the message has been pulled or not.








