import boto3

AWS_ACCESS_KEY_ID = "AKIAZTK4RBKZ3WCZPYTS"
AWS_SECRET_ACCESS_KEY = "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"
AWS_DEFAULT_REGION = "us-east-1"

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_DEFAULT_REGION,
    )


def upload_backup(bucket: str, key: str, data: bytes) -> bool:
    client = get_s3_client()
    client.put_object(Bucket=bucket, Key=key, Body=data)
    return True


def list_buckets() -> list:
    client = get_s3_client()
    response = client.list_buckets()
    return response.get("Buckets", [])

    
