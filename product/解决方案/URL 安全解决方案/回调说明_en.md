Tencent Cloud URL Security Solution takes the active callback method to return the result. After a user has registered a callback domain name, the Tencent Cloud backend actively calls back the blocked URLs or domain names to the user.

## API Description

Protocol: `HTTPS`
Request type: `POST`
Callback address: `Callback address submitted by the customer`
Data encryption method: `AES (128 bits). The key is reserved in the URL solution by the user.`

## Instructions

![Instructions](https://mc.qcloudimg.com/static/img/46f178afc4e313621e4f7eb4c006aad5/image.png)

1. Obtain the data field
After receiving BSP's callback request, the customer's callback server obtains the data field.
BSP URL Security callback example: `http://www.xx.com/callback?data=xx`
In which: `http://www.xx.com/callback` is the address reserved by the customer, and data is the encrypted message for callback.
2. Get the message
Perform the following 3 steps on the data field to get the message:
Step 1: Convert the data field (hexadecimal) to binary data.
Step 2: Perform the AES decryption on the binary data obtained in step 1 to get a decrypted message.
Step 3: Remove the blank spaces at the end of the decrypted message.
**Sample decryption code:**
```
 class prpcrypt():
    def __init__(self,key):
        self.key = key#The key
        self.mode = AES.MODE_CBC
     
    #After decryption, remove the blank spaces with strip()
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_text  = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')
```

3. Decrypt the message
The message decryption is described as follows:
Message example:
```
{"evil_type": 1, "url": "http://www.qq.com/1.html", "site": "qq.com", "source": "BspUrl", "modify_time": "2017-03-24 00:00:00", "evil_lvl": 1}
```

| Parameter | Data Type | Description |
|---------|---------|---------|
| evil_type | Int | Type of malicious content. For more information, please see the appendix: Types of Malicious Content. |
| url | String | Blocked URL |
| site | String | URL's domain name |
| source | String | Source: Used to be identified as the BSP URL Security callback</br>Default value: BspUrl |
| modify_time | String | Update time |
| evil_lvl | 	Int | The level of malicious content. For more information, please see the appendix: Blocking Levels. |

## Appendix
### Types of Malicious Content

| Type ID | Description | Meaning |
|---------|---------|---------|
| 1 | Social engineering fraud | Counterfeit, account phishing, sweepstake fraud |
| 2 | Information scam | Fake top-up, fake employment, fake financial investment, fake credit-card agency, online gambling fraud |
| 3 | Wash sale | Health/beauty/weight-losing products, electronic products, false advertisement, unlawful sale |
| 4 | Malicious document | Links or sites from which virus files, Trojan files and malicious apk files are downloaded, websites with embedded Trojan |
| 5 | Betting website | Betting websites, online gambling websites |
| 6 | Pornographic website | Websites suspected of spreading pornographic contents and providing pornographic services |
| 7 | Risky website | Weakly-typed, websites for spreading spam. This data is not recommended for use if it is blocked by the client |
| 8 | Illegal content | Contents that cannot be disseminated as required by laws and regulations, which are generally politically sensitive and for internal use by default |

### Blocking Levels

| Blocking Level | Description |
|---------|---------|
| 1 | The link is hacked |
| 2 | The CGI is hacked |
| 3 | The path is hacked |
| 4 | The whole website is hacked |
| 5 | The whole domain is hacked |

