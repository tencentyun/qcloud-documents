In this tutorial, assuming that:
- The system needs to send an email in a specific case.
- You want to use CMQ to collect and send necessary information and specify the recipient.


## Implementation Overview

The implementation process of the function is as follows:

- Create the function and the event source mapping of CMQ Topic.
- A user sends the required message contents and the recipient to CMQ in a specific data format.
- CMQ calls the SCF and passes the message to the function in an event.
- The SCF platform receives the call request and runs the function.
- The function acquires the message contents and the recipient from the event data, and calls the sendEmail API to send an email.

Note: By the time you finish this tutorial, your account will contain the following resources:

- An SCF to send emails.
- A CMQ Topic.
- Subscription configuration in the CMQ Topic.

This tutorial is divided into three parts:

- Create a CMQ Topic.
- Complete the steps required to create a function, and call the function manually using the sample CMQ event data. This is designed to verify whether the function works normally.
- Bind the CMQ Topic and the function and test the linkage of the CMQ and the SCF using the sendEmail API, so that the CMQ can call the function when receiving a message.

## Data Structure Design
We assume that the data structure used to send an email is shown below. This data structure will be sent to the CMQ after you enter required values as needed and SCF will receive and process it to send the email.

```
{
  "fromAddr":"sender@testhost.com",
  "toAddr":"test@testhost.com",
  "title":"hello from scf & cmq",
  "body":"email content to send"
}
```

