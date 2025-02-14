# Email configuration

See [post](https://habr.com/ru/company/zimbra/blog/339296/)

## ​Setup SPF, DKIM, DMARC

See [post](https://habr.com/ru/company/zimbra/blog/339296/)

### ​DKIM

generate dkim record for domain
```bash
/opt/zimbra/libexec/zmdkimkeyutil -a -d ditsi.ru
```

add TXT record for your DOMAIN:
```bash
Name: d1bc0820-43cd-43e8-b2344-f28asdasb2b9._domainkey
Content: v=DKIM1;k=rsa;p=CAQ8AMI..ManySymbols..IDAQAB
```

check TXT record

```bash
host -t txt D34334-2745-13CA-ABCD-2124ABCDEF._domainkey.domain.net
```

You can test it [here](https://www.mail-tester.com/)
