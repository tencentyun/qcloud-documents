## FAQs on Offline Speech Recognition

### 1. Is there any limit on the size of voice data for a POST request?
The size of voice data for each POST is limited to 5 MB.

### 2. Can the request be sent in the format of ``post   xxx/appid    -d "projectid=xx&type=yy"``?
No. Request can only be sent in the format of `` post  xxx/appid?projectid=xx&type=yy ``.

### 3. Can the generated signature contain the symbol \n?
Yes. "\n" in the signature has no impact on the authentication.

### 4. When constructing an original signature string, can I replace HOST with IP address?
Yes.


## FAQs on COS + Offline Speech Recognition
### 1. What types of voice files can be uploaded?
The format of voice files uploaded during connection testing should conform to the general standard format, such as mp3, wma, wav, etc.

### 2. How long can an uploaded voice file be?
It can be between 1 second (inclusive) and 1 hour.

### 3. What is the requirement for async callback URL?
The async callback URL provided during connection testing needs to provide service for public network to guarantee a normal performance of callback operation.

### 4. What are the naming rules for COS source bucket and target bucket?
Source bucket and target bucket must have different names. Otherwise when the text recognized for the first time is put into the target bucket which shares the same name with the source bucket, a recognition request is triggered by the system automatically, and a message indicating recognition failure is returned.

### 5. What if users do not return the confirmation message immediately after receiving the recognized text?
  We recommend that users return the confirmation message immediately after they receive the normally recognized data before they can process the recognized text. Otherwise the system may resend the callback notification if no response is received within timeout period.


