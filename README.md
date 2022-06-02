# AWS DDNS Python
Maintains a DDNS record in [AWS Route 53](https://aws.amazon.com/route53/) using the host's public IP address.

## What and Why
Dynamic DNS (DDNS) keeps DNS records automatically up to date when an IP address changes. For example, if your ISP uses DHCP you may want DDNS to reliably communicate with your network even if the IP changes.

## Build Container
> You must cd to the repo

`docker build -t aws-ddns-python:local .`

## Run Container
> You must provide your AWS access key, secret access key, region, hosted zone ID, and domain name in environtment variables.
```
docker run --rm --name aws-ddns-python \
-e AWS_ACCESS_KEY_ID="XXX" \
-e AWS_SECRET_ACCESS_KEY="YYY" \
-e AWS_DEFAULT_REGION="us-east-1" \
-e DOMAIN="ddns.example.com" \
-e HOSTEDZONE_ID="ZZZ" \
aws-ddns-python:local
```

## Schedule Execution
TODO: Provide cron job rule
