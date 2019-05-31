### What is event source?

Event source is an application created by a certain Tencent Cloud service or developers to generate events that can trigger SCF.

### What are the event sources?

Currently, manual trigger (API), timed trigger, COS trigger, CMQ Topic trigger, API gateway trigger, Ckafka trigger are supported. More trigger methods will be available soon.

### How does the application trigger a function directly?

You can call the Invoke API of SCF to trigger a function directly. Only the function owner or users with the permission to call Invoke API can call the function.

### How long is the delay when a function responds to an event?

Generally, SCF can process requests and respond within milliseconds. However, the delay may increase when a function is being created or updated, or if it has not been called recently.