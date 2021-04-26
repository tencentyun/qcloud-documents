Consumers can pull and view messages by specifying the following attributes:

1) ReceiptHandle: Temporary receipt handle generated when the current message is successfully received, which is used to delete or modify the message in Inactive status and is valid before NextVisibleTime.

2) EnqueueTime: Time when a received message is sent to the queue.

3) DequeueCount: Total consumption times of a received message.

4) FirstDequeueTime: Time when a received message is consumed for the first time.

5) NextVisibleTime: Time when a received message can be consumed again when the VisibilityTimeout is set.

6) MessageBody: The body of a received message. It is the source text sent by the producer, and will not be encoded or modified by CMQ.

