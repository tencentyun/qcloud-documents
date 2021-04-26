The producer pushes messages to Topic by specifying the following information:

1) Topic name

2) Topic resource ID

3) Published title. Users may enter the title according to their own needs

4) Published content: Main body of the message, customers may enter the content according to their own needs. CMQ will not encode or modify this content

5) Add message filter tag: Tag, namely message tag, message type, is used to differentiate message categories under the Topic of a certain CMQ. Consumers are allowed to filter messages based on the tags and thus only consume the messages that they're interested in. This feature is disabled by default. In this case, all messages will be sent to all the subscribers. If a subscriber configured a tag, the subscriber will not receive any messages because the tag doesn't match with the tag of the Topic. The message filter tag describes the tag used for message filtering for this subscription (only the messages with consistent tags will be pushed). Each tag is a string with no more than 16 characters. There can be at most 10 tags for a single message

