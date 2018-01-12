A common message that has been sent to the common message queue is originally in an ***Active*** status. If retrieved, this message will be in an ***Inactive*** status within VisibilityTimeout. If the message has not been deleted within the VisibilityTimeout, it will return to ***Active*** status. The status of the message will become ***Deleted*** if it is deleted within VisibilityTimeout. MessageRetentionPeriod specified upon the creation of a queue determines the maximum retention time of the message. It will become ***Expired*** and be reclaimed when the retention time expires.

Consumers can only retrieve the messages in an ***Active*** status. This ensures that a message cannot be repeatedly consumed in the same period of time but can be repeatedly consumed in sequence.

![](//mccdn.qcloud.com/static/img/c6842c7b34226a86f34ab1ae18373499/image.jpg)

- Component 1 sends Message A to a queue, and the message provides multiple copies of redundant data across the CMQ servers.

- When Component 2 is ready to process a message, it retrieves messages from the queue, and Message A is returned. While Message A is being processed, it remains in the queue and cannot be received by other business for the duration of the *visibility timeout*

- Component 2 deletes Message A from the queue to prevent the message from being received and processed again once the visibility timeout expires. If Message A is not deleted, it can be consumed repeatedly by other business
