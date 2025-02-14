# aws, aws-cli

## Commands

```bash
aws configure
aws ec2 describe-instances
```

# S3

## Commands

```bash
export AWS_ACCESS_KEY_ID=<key_id>
export AWS_SECRET_ACCESS_KEY=<access_key>
aws --endpoint-url http://192.168.1.1:8443 s3 ls s3://bucket_name
```

```bash
aws --endpoint-url http://192.168.1.1:8443 s3 ls s3://bucket_name
# directory size
aws --endpoint-url http://192.168.1.1:8443 s3 ls s3://bucket_name/directory --recursive --summarize
```
