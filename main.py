import boto3
import os
import sys
import requests

if not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY") or not os.getenv("AWS_DEFAULT_REGION"):
    print("Error: Did not provide AWS credentials or region")
    sys.exit(1)

route53 = boto3.client('route53')

def main():
    domain = os.getenv("DOMAIN")
    if not domain:
        print("Error: Did not provide a domain name")
        sys.exit(1)

    hostedzone_id = os.getenv("HOSTEDZONE_ID")
    if not hostedzone_id:
        print("Error: Hostedzone ID not provided")
        sys.exit(1)
    
    # Obtain public IP
    public_ip = requests.get('https://checkip.amazonaws.com').text.strip()
    print("Current Public IP: ", public_ip)

    try:
        response = route53.change_resource_record_sets(
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': domain,
                            'ResourceRecords': [
                                {
                                    'Value': public_ip,
                                },
                            ],
                            'TTL': 300,
                            'Type': 'A',
                        },
                    },
                ],
                'Comment': 'DDNS',
            },
            HostedZoneId=hostedzone_id,
        )
    except botocore.exceptions.ClientError as error:
        raise error

    print("OK")

if __name__ == "__main__":
    main()
