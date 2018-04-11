The parameter "message" should be the payload (a json string) specified by APNS. For detailed definition, please see APNS official manual.
XGPush only adds two reserved fields xg and accept_time. The payload cannot exceed 800 bytes. Note that the accept_time field is not passed to APNS and therefore does not take up the payload capacity.

## Example of Ordinary Notification
```
{
"aps" : { // The key-value specified by APNS
"alert" : { // Set fields of notification bar
"title": "this is a title", // Notification title
"body" : "Bob wants to play poker", // Notification content
},
"badge" : 5,
"category" : "INVITE_CATEGORY",
},
"accept_time":[ // The period when messages are allowed to be pushed to users (optional). Accept_time does not occupy the capacity of payload
{
"start":{"hour":"13","min":"00"},
"end": {"hour":"14","min":"00"}
},
{
"start":{"hour":"00","min":"00"},
"end": {"hour":"09","min":"00"}
}
] // Notifications can only be pushed from 0 to 9 o'clock and from 13 to 14 o'clock.
"custom1" : "bar", // Valid custom key-value which is passed to App
"custom2" : [ "bang", "whiz" ], // Valid custom key-value which is passed to App
"xg" : "oops" // Error! xg is the reserved key in XGPush and its value will be overridden by XGPush. Avoid using it.
}
```
## Example of Silent Notification

```
{
"aps" : { // The key-value specified by APNS
"badge" : 5,
"category" : "INVITE_CATEGORY",
"content-available": 1, // The identity of silent notification
},
"custom1" : "bar", // Valid custom key-value which is passed to App
"custom2" : [ "bang", "whiz" ], // Valid custom key-value which is passed to App
"xg" : "oops" // Error! xg is the reserved key in XGPush and its value will be overridden by XGPush. Avoid using it.
}
```

