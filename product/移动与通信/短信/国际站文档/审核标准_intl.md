## Signature Audit Criteria
### Format Limits

1. A signature cannot contain information related to pornography, gambling, drug abuse, or any religion, party or government.
2. A signature cannot be ambiguous. It must clearly indicate the company or individual who sends SMS messages.
3. A China [SMS Signature](https://intl.cloud.tencent.com/document/product/382/13299#sms-signature) is composed of 【】 and signature content which contains 2 to 12 Chinese/English characters or numbers. Special symbols such as "+, @, and |" are not supported. Try to use Chinese characters for China SMS signatures. Only signature content is required when you apply for an SMS signature on the [Console](https://console.cloud.tencent.com/sms/smsSign/1400054957/0/10). For example, if the signature of a Tencent Cloud SMS message is "【Tencent Cloud】", you need only to submit "Tencent Cloud" when applying for an SMS signature.
4. International SMS signature is composed of [] and signature content which is a combination of 2-15 characters excluding []. Only signature content is required when you apply for an SMS signature on the [Console](https://console.cloud.tencent.com/sms/smsSign/1400054957/0/10). For example, if the international signature of a Tencent Cloud SMS message is "[Tencent Cloud]", you need only to submit "Tencent Cloud" when applying for an SMS signature.

### Audit Rules

An [SMS signature](https://intl.cloud.tencent.com/document/product/382/13299#sms-signature) needs to be licensed by operators and the original or the copy of business license stamped with the company's official seal must be provided. If the signature infringes the rights of any third party, an appropriate authorization from this third party must be obtained. For any questions, contact [Submit a ticket](https://console.cloud.tencent.com/workorder/category).

1. The signature is **the name of a WeChat Official Account or Mini Program**.
 - For enterprise identify verification, the account subject of the Official Account must be identical with the company name on the copy of the business license (or organization code certificate).
 - For individual identity verification, a screenshot of the backend management interface for the Official Account or Mini Program must be uploaded.
2. If the signature is **a company name or its abbreviation**, it must be identical with the company name on the uploaded copy of the business license (or organization code certificate).
3. If the signature is **a product name or its abbreviation**, a note containing a download link to an App Store must be provided.
 - For enterprise identity verification, the information of the App in the App Store must be identical with that on the copy of the business license (or organization code certificate).
 - For individual identity verification, a screenshot of the backend management interface of the App Store must be uploaded.
4. If the signature is **a website name or its abbreviation**, it must be the full name or abbreviation of the website licensed by MIIT.
 - For enterprise identity verification, the ICP licensing information of the website must be identical with that on the copy of the business license (or organization code certificate).
 - For individual identity verification, a screenshot of the ICP licensing information must be provided. If the subject is an enterprise, a copy of the business license must be provided.
5. If the signature is **a brand name or its abbreviation**, the brand registration certificate is required.


## Audit Criteria for Common SMS Messages
### Format Limits

1. Full variable template is not supported (which means that the structure and use scenarios of SMS messages cannot be known).
2. Since special symbols may cause unreadable codes displayed in SMS messages, ￥, ★ or combination of special symbols such as ^_^&, ☞, √, ※ that can be typed in by pressing keys are not supported.

### Content Limits

1. Verification code templates must contain "verification code".
2. Content related to marketing or promotion is not supported.
3. SMS messages involving stock, immigration, interview & recruitment, lottery, rebate, loan, dunning, investment & financing, gambling, winning a prize, getting or purchasing a product with one CNY, counterfeit products, healthcare, plastic surgery, beauty, clubs, bars, foot massage, violence, intimidation, pornography, fur, cheating in exams, trademark registration, QQ or WeChat group invitation, personal information trafficking, messaging channels, promotion on game/exhibition/website/coupon/card/insurance/alcohol, prospect invitation, and existing customer recall are prohibited, and those involving finance, real estate and education are also not allowed except for verification code.
4. Unauthorized invitations for purposes of registration or joining membership are not allowed.

>If any infringement of [Terms of Service](https://intl.cloud.tencent.com/document/product/301/13616) is identified, Tencent Cloud may at any time restrict, suspend or terminate services to you under the terms as appropriate, or block your account (forever) and take other measures. Once a package is purchased, whether it has been used or not, unsubscription or refund is not allowed. If any serious impact or consequences are identified, Tencent Cloud retains the right to pursue related liability against you. Therefore, make sure to comply with the regulations strictly, strengthen your business security, and send SMS messages properly.

## Audit Criteria for Marketing SMS Messages
### Format Limits

1. Full variable template is not supported (which means that the structure and application scenarios of SMS messages cannot be known).
2. Unsubscription methods must be added at the end of the marketing SMS messages. Replying "TD, T or N" for unsubscription is supported.
3. Since special symbols may cause unreadable codes displayed in SMS messages, ￥, ★ or combination of special symbols such as ^_^&, ☞, √, ※ that can be typed in by pressing keys are not supported.

### Content Limits
1. Do not send marketing SMS messages to nonmembers.
2. SMS messages involving stock, immigration, real estate, education, training, recruitment, lottery, rebate, loan, dunning, investment, gambling, winning a prize, getting or purchasing a product with one CNY, counterfeit products, health care, plastic surgery, beauty, clubs, bars, foot massage, violence, intimidation, pornography, fur, cheating in exams, trademark registration, QQ or WeChat group invitation, personal information trafficking, messaging channels, decoration (including building materials and furniture), promotion on game/exhibition/website/coupon/card/insurance/alcohol, prospect invitation, and existing customer recall are prohibited.
3. Unauthorized invitations for purposes of registration or joining membership are not allowed.

>If any infringement of [Terms of Service](https://intl.cloud.tencent.com/document/product/301/13616) is identified, Tencent Cloud may at any time restrict, suspend or terminate services to you under the terms as appropriate, or block your account (forever) and take other measures. Once a package is purchased, whether it has been used or not, unsubscription or refund is not allowed. If any serious impact or consequences are identified, Tencent Cloud retains the right to pursue related liability against you. Therefore, make sure to comply with the regulations strictly, strengthen your business security, and send SMS messages properly.


## Standards on Marketing SMS messages
1. Always add "reply T if you don't want to receive such message" at the end of any SMS message.
2. Do not send marketing SMS messages to nonmembers.
3. Strictly comply with [SMS message standards](https://intl.cloud.tencent.com/document/product/382/13444#audit-criteria-for-common-sms-messages) and do not send any SMS messages that violate applicable regulations and laws.
4. Send marketing SMS messages in the daytime (8:00 - 22:00) to minimize complaints.

## Audit Procedure
Generally, you can get the audit result of your signature and content template in half a working day. The audit time is from Monday to Sunday between 9:00 to 21:00.
If you want to use the SMS service in a short time, [submit a ticket](https://console.cloud.tencent.com/workorder/category) and we will accelerate the audit process. If the audit is not approved, [submit a ticket](https://console.cloud.tencent.com/workorder/category) for a solution.
Since the approved content templates also need to be spot checked and reviewed by operators, SMS messages may not be sent successfully. If such issue occurs, [submit a ticket](https://console.cloud.tencent.com/workorder/category) for a solution. 

## Rules for Blocking SMS
Both SMS signatures and SMS templates applied for by users are reviewed by SMS technical support, and SMS content is also monitored and detected by the cloud SMS system when users are sending SMS messages, so as to prevent the content that violates national laws and regulations from appearing in SMS messages.
For users who send [SMS messages that violate the rules](https://intl.cloud.tencent.com/document/product/382/13444#audit-criteria-for-common-sms-messages), we may freeze their accounts, deduct deposit, or pursue related liability against the users as the case may be.


