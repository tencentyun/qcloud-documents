## Usage Scenarios of Smart Resolution Line

In general, resolution only resolves IP records for users but does not tell where the users come from, which means all users are resolved to fixed IP addresses. While smart resolution can tell where a user comes from in order to make smart adjustments and return the adjusted IP back to the user. For example, smart resolution can tell whether the user is using China Unicom or China Telecom line, then returns the corresponding server IP.

### 1. List of Lines
Here's a detailed list of lines supported by Tencent Cloud DNS:

| Category | Lines |
|---|---|
| By Region | North China, Northeast China, East China, Central China, South China, Southwest China, Northwest China |
| By Province | North China: Beijing, Hebei, Tianjin, Shanxi, Inner Mongolia</br>Northeast China: Heilongjiang, Jilin, Liaoning</br>East China: Jiangsu, Shanghai, Zhejiang, Anhui, Fujian, Jiangxi, Shandong</br>Central China: Hubei, Hunan, Henan</br>South China: Guangdong, Guangxi, Hainan</br>Southwest China: Sichuan, Tibet, Chongqing, Yunnan, Guizhou</br>Northwest China: Gansu, Xinjiang, Shaanxi, Qinghai, Ningxia</br>Hong Kong, Macao, Taiwan |
| By ISP | China Telecom, China Unicom, China Mobile, China Railcom, China Education Network, Teletron, Great Wall Broadband Network, Wasu |
| By Continent | Africa, Antarctica, Asia, Europe, North America, Oceania, South America |
| By Country/Region (247) | Andorra, The United Arab Emirates, Afghanistan, Antigua and Barbuda, Anguilla, Albania, Armenia, Netherlands Antilles, Angola, Argentina, Eastern Samoa, Austria, Australia, Aruba, Aland Islands, Azerbaijan, Bosnia and Herzegovina, Barbados, Bengal, Belgium, Burkina Faso, Bulgaria, Bahrain, Burundi, Benin, Saint-Barthelemy, Bermuda, Brunei Darussalam, Bolivia, Caribbean Netherlands, Brazil, Bahamas, Bhutan, Bouvet Island, Botswana, Belarus, Belize, Canada, Cocos Islands, Democratic Republic of the Congo, Central Africa, Congo (Brazzaville), Switzerland, Ivory Coast, Cook Islands, Chile, Cameroon, China, Colombia, Costa Rica, Czechoslovakia, Cuba, Cape Verde, Curacao, Christmas Island, Cyprus, Czech Republic, Germany, Djibouti, Denmark, Dominican Republic, Dominican Republic, Algeria, Ecuador, Estonia, Egypt, Western Sahara, Eritrea, Spain, Ethiopia, Finland, Fiji, Frankenstein, Micronesia, Faroe Islands, France, Gabon, United Kingdom, Grenada, Georgia, French Guiana, Guernsey, Ghana, Gibraltar, Greenland, Gambia, Guinea, French Peninsula, Equatorial Guinea, Greece, South Georgia and the South Sandwich Islands, Guatemala, Guam, Guinea-Bissau, Guyana, Hurd and McDonald Islands, Honduras, Croatia, Haiti, Hungary, Indonesia, Ireland, Israel, Isle of Man, India, British Indian Ocean Territory, Iraq, Iran, Iceland, Italy, Jersey, Jamaica, Jordan, Japan, Kenya, Kyrgyzstan, Cambodia, Kiribati, Comoros, Saint Kitts and Nevis, North Korea, South Korea, Kuwait, Cayman Islands, Kazakhstan, Laos, Lebanon, Saint Lucia, Liechtenstein, Sri Lanka, Liberia, Lesotho, Lithuania, Luxembourg, Latvia, Libya, Morocco, Monaco, Moldova, Montenegro, French Sint Maarten, Madagascar, Marshall Islands, Macedonia, Mali, Myanmar, Mongolia, Northern Mariana Islands, French Martinique, Mauritania, Montserrat, Malta, Mauritius, Maldives, Malawi, Mexico, Malaysia, Mozambique, Namibia, New Caledonia, Niger, Norfolk Island, Nigeria, Nicaragua, Netherlands, Norway, Nepal, Nauru, Niue New Zealand, Oman, Panama, Peru, French Polynesia, Papua New Guinea, Philippines, Pakistan, Poland, Saint Pierre and Miquelon, Pitcairn Island, Puerto Rico, Palestine, Portugal, Palau, Paraguay, Qatar, French Niwano Island, Romani Senegal, Serbia, Russia, Rwanda, Saudi Arabia, Solomon Islands, Seychelles, Sudan, Sweden, Singapore, Saint Helena, Slovenia, Svalbard and Jan Mayen, Slovakia, Sierra Leone, San Marino, Senegal , Somalia, Suriname, South Sudan, Sao Tome and Principe, El Salvador, Sint Maarten, Syria, Swaziland, Turks and Caicos Islands, Chad, Southern France, Togo, Thailand, Tajikistan Turkmenistan, Tunisia, Tonga, Turkey, Trinidad and Tobago, Tuvalu, Tanzania, Ukraine, Uganda, United States Overseas Territories, United States, Uruguay, Uzbekistan, Vatican City, Saint Vincent and the Grenadines, Venezuela, British Virgin Islands, United States Virgin Islands, Vietnam, Vanuatu, Wallis and Futuna Islands, Western Samoa, Yemen, Mayotte, South Africa, Zambia, Zimbabwe |
| By Search Engine | Baidu, Google, Soso, Youdao, Bing, Sougou, Qihoo |

### 2. How to Use Regional/ISP Lines
For example, for `cloud.tencent.com`, configure "Default" lines to be resolved to 8.8.8.8, "Guangdong" lines to be resolved to 9.9.9.9, "Guangdong Telecom" lines to be resolved to 10.10.10.10. With such configuration, IP addresses of 10.10.10.10 are returned to Guangdong Telecom ISP users, IP addresses of 9.9.9.9 are returned to non-Telecom Guangdong ISP users, and IP addresses of 8.8.8.8 are returned to non-Guangdong users.
If you suspend resolution for Guangdong Telecom lines or Guangdong lines, the resolution across the country will not be affected (IP addresses of 8.8.8.8 are returned). **Thus, make sure to add resolution for "Default" lines first, whether you will add regional/ISP lines or not**.

### 3. How to Use Search Engine Lines
For search engine lines, you can configure spiders of Baidu, Google and so on, to capture different IP addresses. For example, for `cloud.tencent.com`, configure "Default" lines to be resolved to 8.8.8.8, "Baidu" lines to be resolved to 9.9.9.9, "Sougou" lines to be resolved to 10.10.10.10. With such configuration, IP addresses of 10.10.10.10 are returned to users who use Sougou to search and access the website, IP addresses of 9.9.9.9 are returned to those who use Baidu, and IP addresses of 8.8.8.8 are returned to those who access the website directly.

>**Note:**
> "Search engine" line refers to a group of search engines such as Baidu, Google and so on.

## Resolution Lines Supported by Different Packages

| DNS Package  | Supported Lines |
|---|---|
| Free Package | Basic lines are supported: default, lines inside/outside China, China Mobile, China Telecom, China Unicom, China Education Network and all search engine lines |
| Individual Professional Package | Basic lines are supported: default, lines inside/outside China, China Mobile, China Telecom, China Unicom, China Education Network and all search engine lines |
| Enterprise Basic Package | China Railcom and Teletron lines are provided in addition to all basic lines |
| Enterprise Standard Package | In addition to all basic lines, China Railcom lines, Teletron lines, Great Wall Broadband lines, provincial lines of China Telecom and China Unicom, Hong Kong/Macao/Taiwan Lines, continental lines outside of China are provided |
| Enterprise Ultimate Package | In addition to all basic lines, China Railcom lines, Teletron lines, Great Wall Broadband lines, Provincial lines of China Telecom/China Unicom/China Mobile, Hong Kong/Macao/Taiwan Lines, continental lines outside of China and lines of 247 countries/regions are provided |

