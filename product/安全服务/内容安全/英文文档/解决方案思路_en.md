## Background
As the Internet flourishes, users have generated vast amounts of textual contents, including spam texts, which may decrease product experience, violate laws and regulations, or even lead to website shutdown. Most of these spam texts are made by practitioners in the Internet underground industry.
It is conservatively estimated that the number of practitioners in the current underground industry of Internet is not less than 400,000 in China, and the industrial scale of the entire underground industry has reached the level of one hundred billion. After years of rapid development, there has been a clear division of labors in the Internet underground industry: advertisers, black-hat groups specialized in tool development and technical supports, card providers who have massive mobile phone cards, group message senders, cheap coders, and so on. The devices also become much more sophisticated, including automatic registration machines with complex logic, group texting machines, and verification code recognition platforms running on a 24/7 basis. The underground industry practitioners often add noises and deformations in the spam text to make it hard to be recognized. Tencent provides a professional system to deal with these bad guys.

## BSP Solution Overview
BSP recommends to identify the malicious users and contents from the processes of registration, login, and user-generated content (UGC) generation. BSP provides APIs for identifying malicious users and contents in each of the process to secure business systems.

![Solution](https://mc.qcloudimg.com/static/img/036a90c3c9bc82d9bf0e6e8be8b81c79/image.png)

### Registration
In the registration process, BSP Antispam services identify, block, and crack fake accounts to minimize the number of accounts that can be used by bad people.

### Login
In the login process, BSP Antispam services increase the login threshold for fake accounts by using CAPTCHA and SMS verification code. These means reduce the efficiency of automaton login, the number of logins of fakes accounts, and the UGC productivity of the underground industry practitioners.

### UGC Generation
In the UGC generation process, BSP Antispam services identify and block the malicious texts that contain pornography, advertising, and other contents from the text level, so as to capture the overlooked ones in the registration and login processes.




