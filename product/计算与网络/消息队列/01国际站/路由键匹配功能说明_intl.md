The routing key matching feature of CMQ is similar to the exchange queue of rabbitMQ. It is used to filter messages, and make subscribers receive different messages based on different conditions. You can enable "Routing Key Matching" when creating Topic.

Instructions:

- Binding key and Routing key are used together, they provide a message filtering function which is similar to RabbitMQ. The Routing key used when sending messages is provided by the client when it sends messages. The Binding key used when creating subscription relationships is the binding relationship between Topic and Subscriber.

Restrictions:

- 1. There can be at most five Binding keys. Binding key is used to indicate the routing path for sending messages, it must be no longer than 64 Bytes, and can contain up to 15 ".", i.e. 16 phrases at most

 - 2. Routing key consists of a string. Routing key is used to indicate the routing path for sending messages, it must be no longer than 64 Bytes, and can contain up to 15 ".", i.e. 16 phrases at most

Wildcards:

- 1. Asterisk (*), can be used in place of a word (a string of continuous characters) 

- 2. Pound sign (#), can be used to match with one or multiple characters


For example:

- 1. Subscriber is "1.*.0", and message is "1.<any character>.0", then the subscriber will receive the message

- 2. Subscriber is "1.#.0", and message is "1.2.3.4.4.2.2.0", then the subscriber will receive the message (the middle part of the message can be anything) 

- 3. Subscriber is "#", then the subscriber will receive all messages


![](https://mc.qcloudimg.com/static/img/7b82bed30d4ec3fda544112adeace96f/image.png)


