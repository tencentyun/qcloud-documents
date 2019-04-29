## Individual Verification vs. Enterprise Verification

![](//mc.qcloudimg.com/static/img/3dab63de8c91f81e3004eb93236087fa/image.png)

## Signature Verification Standard
### Format Limitation

1. Signature cannot contain information related to pornography, gambling, drug abuse, religion, party or government.
2. Signature cannot be ambiguous. It must clearly indicate whether it is sent from a company or an individual.
3. A China [SMS signature](https://cloud.tencent.com/document/product/382/13299#.E7.9F.AD.E4.BF.A1.E7.AD.BE.E5.90.8D) is composed of 【】 and signature content containing 2 to 12 Chinese/English characters or numbers. Special symbols such as "+, @, and |" are not supported. Try to use Chinese characters for China SMS signatures. Only signature content is required when you apply for an SMS signature on the [Console](https://console.cloud.tencent.com/sms/smsSign/1400054957/0/10). For example, if the signature of a Tencent Cloud SMS message is "【Tencent Cloud】", you can just submit "Tencent Cloud" when applying for an SMS signature.
4. International or regional SMS Signature is composed of [] and signature content containing 2-15 characters without []. Only signature content is required when you apply for an SMS signature on the [Console](https://console.cloud.tencent.com/sms/smsSign/1400054957/0/10). For example, if the international signature of a Tencent Cloud SMS message is "[Tencent Cloud]", you can just submit "Tencent Cloud" when applying for an SMS signature.

## Verification Rules

[SMS signatures](https://cloud.tencent.com/document/product/382/13299#.E7.9F.AD.E4.BF.A1.E7.AD.BE.E5.90.8D) need to be licensed by operators and the original or the copy of enterprise's business license stamped with its official seal should also be provided. If the signature infringes the rights of any third party, an appropriate authorization from this third party must be obtained. For any questions, [contact SMS Helper](/document/product/382/3773).

1. The signature is **the name of a WeChat Official Account or Mini Program**.
 - For enterprise verification, the account subject of the Official Account must be identical with the company name on business license.
 - For individual verification, a screenshot of the backend management interface for the Official Account or Mini Program must be uploaded.
2. If the signature is **a company name or its abbreviation**, it must be identical with the company name on the uploaded business license.
3. If the signature is **an app name or its abbreviation**, a note containing a download link to one of any app stores must be provided.
 - For enterprise verification, the information of the app in the app store must be identical with that on the business license.
 - For individual verification, a screenshot of the backend management interface for the app store must be uploaded.
4. If the signature is **a website name or its abbreviation**, it must be the full name or abbreviation of the website licensed by MIIT.
 - For enterprise verification, the ICP licensing information of the website must be identical with that on the business license.
 - For individual verification, a screenshot of the ICP licensing information at the backend end of domain name ICP licensing ISP (If the subject is an enterprise, a copy of business license must be provided).
5. If the signature is **a brand name or its abbreviation**, the brand registration certificate is required.


## Verification Standard for Common SMS
### Format Limitation

1. Templates with only variables are not supported (which means that the structure and application scenarios of SMS messages cannot be determined).
2. Since special symbols may cause unreadable codes displayed in SMS messages, ￥, ★ or combination of special symbols such as ^_^&, ☞, √, ※ that can be typed in by pressing keys are not supported.

### Content Limitation

1. Verification code templates must contain "verification code".
2. Content involving marketing or promotion is not supported.
3. SMS messages involving stock, immigration, interview & recruitment, lottery, rebate, loan, dunning, investment & financing, gambling, winning a prize, get or purchase a product at one yuan, counterfeit products, healthcare, plastic surgery, beauty, clubs, bars, foot massage, violence, intimidation, pornography, fur, cheating in exams, trademark registration, QQ or WeChat group invitation, personal information trafficking, messaging channels, promotion on game/exhibition/website/coupon/card/insurance/alcohol, prospect invitation, and existing customer recall are prohibited, and those involving finance, real estate and education are also not allowed except for verification code.
4. Unauthorized invitations primarily for purposes of registration or joining membership are not allowed.
>In case anyone violates any of the aforesaid regulations and causes bad impacts, we will punish him/her and disable his/her account. Therefore, comply with the regulations strictly, strengthen your business security, and send SMS messages properly.

## Verification Standard for Marketing SMS
### Format Limitation

1. Templates with only variables are not supported (which means that the structure and application scenarios of SMS messages cannot be determined).
2. Unsubscribing method must be added at the end of the marketing SMS content. Replying "TD, T or N" for unsubscription is supported.
3. Since special symbols may cause unreadable codes displayed in SMS messages, ￥, ★ and combination of special symbols such as ^_^&, ☞, √, ※ that can be typed in by pressing keys are not supported.

### Content Limitation
1. Do not send marketing SMS to non-members.
2. SMS messages involving stock, immigration, real estate, education, training, recruitment, lottery, rebate, loan, dunning, investment, gambling, winning a prize, get or purchase a product at one yuan, counterfeit products, health care, plastic surgery, beauty, clubs, bars, foot massage, violence, intimidation, pornography, fur, cheating in exams, trademark registration, QQ or WeChat group invitation, personal information trafficking, messaging channels, decoration (including building materials and furniture), promotion on game/exhibition/website/coupon/card/insurance/alcohol, prospect invitation, and existing customer recall are prohibited.
3. Unauthorized invitations primarily for purposes of registration or joining membership are not allowed.
>In case anyone violates any of the aforesaid regulations and causes bad impacts, we will punish him/her and disable his/her account. Therefore, comply with the regulations strictly, strengthen your business security, and send SMS messages properly.


## Standards on Marketing SMS
1. Always add "Reply T if you don't want to receive such message" at the end of any text.
2. Do not send marketing SMS to non-members.
3. Strictly comply with the [standards on SMS content](https://cloud.tencent.com/document/product/382/13444#.E6.99.AE.E9.80.9A.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86) and do not send any messages that violate applicable regulations.
4. Send marketing SMS messages in the daytime (8:00 - 22:00) to minimize complaints.

## Verification Procedure
Generally, you can get the review result of your signature and content template in half a work day. The review time is from Monday to Sunday between 9:00 to 21:00.
If you want to use the SMS in a short time, [contact SMS Helper](/document/product/382/3773) and we will accelerate the review process. If the verification is not approved, [contact SMS Helper](/document/product/382/3773) for a solution.
Since the approved content templates also need to be spot checked and reviewed by operators, the templates may not be sent successfully. If such issue occurs, [contact SMS Helper](/document/product/382/3773) for a solution. 

## Rules for Blocking SMS
Both [SMS signature](https://cloud.tencent.com/document/product/382/13299#.E7.9F.AD.E4.BF.A1.E7.AD.BE.E5.90.8D) and [SMS template](https://cloud.tencent.com/document/product/382/13299#.E7.9F.AD.E4.BF.A1.E6.A8.A1.E6.9D.BF) applied for by users are reviewed by SMS technical support, and the SMS content is also monitored and detected by the cloud SMS system when users are sending SMS messages, so as to prevent content that violates the requirements of national laws and regulations from appearing in the SMS messages.
For users who send SMS messages that [violate the rules](https://cloud.tencent.com/document/product/382/13444#.E6.99.AE.E9.80.9A.E7.9F.AD.E4.BF.A1.E5.AE.A1.E6.A0.B8.E6.A0.87.E5.87.86), we may freeze their accounts, deduct deposit, or hold them liable as the case may be.
After the account is frozen, the user can neither use SMS service nor apply for activation of the service later. Any unused messages in the [SMS service package](https://cloud.tencent.com/document/product/382/13298) of the account are unavailable either.


