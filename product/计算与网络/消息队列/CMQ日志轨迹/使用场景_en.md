1. The producer can know immediately whether the message from Topic is successfully delivered

2. The producer can know immediately the consumption state of the Queue message

3. The consumer can figure out why he/she fails to receive the message from Topic.

4. The consumer can know whether he/she pulled the same contents of a Queue multiple times

5. The message lifecycle from the producer to the consumer is accessible
     
If the message in the production environment is not sent/received as scheduled, you can use the message trace tool for troubleshooting. You can search for related log trace based on the message attributes (Message ID, Queue, Topic and Time), find out the actual status of the message, and then troubleshoot the problem.

