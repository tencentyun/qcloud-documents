```java
import java.util.Random;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import sun.misc.BASE64Encoder;

public class Signature {
	public String m_strSecId;
	public String m_strSecKey;
	public long m_qwNowTime;
	public int m_iRandom;
	public int m_iSignValidDuration;

	private static final String HMAC_ALGORITHM = "HmacSHA1";
	private static final String CONTENT_CHARSET = "UTF-8";

	public static byte[] byteMerger(byte[] byte_1, byte[] byte_2) {
		byte[] byte_3 = new byte[byte_1.length + byte_2.length];
		System.arraycopy(byte_1, 0, byte_3, 0, byte_1.length);
		System.arraycopy(byte_2, 0, byte_3, byte_1.length, byte_2.length);
		return byte_3;
	}

	String GetUploadSignature() {
		String strSign = "";
		String contextStr = "";
		long endTime = (m_qwNowTime + m_iSignValidDuration);
		try {
			contextStr += "secretId=" + java.net.URLEncoder.encode(this.m_strSecId, "utf8");
			contextStr += "&currentTimeStamp=" + this.m_qwNowTime;
			contextStr += "&expireTime=" + endTime;
			contextStr += "&random=" + this.m_iRandom;

			String s = contextStr;
			String sig = null;
			Mac mac = Mac.getInstance(HMAC_ALGORITHM);
			SecretKeySpec secretKey = new SecretKeySpec(m_strSecKey.getBytes(CONTENT_CHARSET), mac.getAlgorithm());
			mac.init(secretKey);
			byte[] hash = mac.doFinal(contextStr.getBytes(CONTENT_CHARSET));
			byte[] sigBuf = byteMerger(hash, contextStr.getBytes("utf8"));
			strSign = new String(new BASE64Encoder().encode(sigBuf).getBytes());
		} catch (Exception e) {
			System.out.print(e.toString());
			return "";
		}
		return strSign;
	}
}

class Test {
	public static void main(String[] args) {
		Signature sign = new Signature();
		sign.m_strSecId = "AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv";
		sign.m_strSecKey = "bLcPnl88WU30VY57ipRhSePfPdOfSruK";
		sign.m_qwNowTime = System.currentTimeMillis() / 1000;
		sign.m_iRandom = new Random().nextInt(java.lang.Integer.MAX_VALUE);
		sign.m_iSignValidDuration = 3600 * 24 * 2;
		
		System.out.print(sign.GetUploadSignature());
	}
}
```

## 注意
* 需要导入第三方包 javax-crpyto.jar 和 sun.misc.BASE64Encoder.jar。
* 如果导入第三方包 sun.misc.BASE64Encoder.jar 出现 Access restriction 的错误，可以通过调整错误级别解决（```Windows -> Preferences -> Java -> Compiler -> Errors/Warnings -> Deprecated and trstricted API -> Forbidden reference (access rules): -> change to warning```）。
