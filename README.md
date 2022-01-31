# Docker image default configurations for DHCP server

References: https://wiki.debian.org/DDNS

### Run Instructions

## Configure DNS location

Configure the correct DNS server location inside
the docker-compose.yml file.

## Run container

Prior to running the image, change the DDNS key with a valid one.
WARNING! This key must be the same one as the DNS server. If you have
already done this for a DNS server, just copy the key and copy to the
appropriate file.

You can generate one with:

```
dnssec-keygen -a HMAC-MD5 -b 128 -r /dev/urandom -n USER DDNS_UPDATE
```

Inside the file "Kdhcp_updater.\*.private" copy the key starting with
"Key:". For instance,

```
Key: pRP5FapFoJ95JEL06sv4PQ==
```

Everything after "Key: " is the actual key.

And, in file data/bind/ddns.key, substitute the following string:

```
secret "${DDNS_KEY}";
```

With the key from the previous step. Like, this for instance:

```
secret "pRP5FapFoJ95JEL06sv4PQ==";

docker-compose up -d
```
