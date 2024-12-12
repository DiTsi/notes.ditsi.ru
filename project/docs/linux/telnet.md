# telnet

## Commands

```bash
telnet 192.168.12.10 22 # test 22 port on host
```

## Send email

[link](https://mediatemple.net/community/products/dv/204404584/sending-or-viewing-emails-using-telnet)

<p class="callout info">Pay attention to the dot at the end</p>

```
telnet example.com 25
ehlo example.com
mail from: username@example.com
rcpt to: friend@hotmail.com, friend2@yahoo.com
data
Subject: My Telnet Test Email
Hello,
This is an email sent by using the telnet command.
Your friend,
Me

.

```