import boto3
import uuid

# Initialize the S3 client using your local credentials
s3 = boto3.client('s3', region_name='ap-southeast-2')

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_name):
    """Create an S3 bucket in a specific region"""
    try:
        location = {'LocationConstraint': 'ap-southeast-2'}
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print(f"✅ Success: Bucket '{bucket_name}' created.")
    except Exception as e:
        print(f"❌ Error: {e}")

def delete_bucket(bucket_name):
    """Deletes an empty S3 bucket"""
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"🗑️  Deleted: Bucket '{bucket_name}' removed.")
    except Exception as e:
        print(f"❌ Error: {e}")

# --- Main Execution ---
if __name__ == '__main__':
    # 1. Generate a unique name (to avoid 'BucketAlreadyExists' errors)
    my_bucket = create_bucket_name('jayden-lab-')
    
    print(f"--- Starting Boto3 Lab: {my_bucket} ---")

    # 2. Create it
    create_bucket(my_bucket)

    # 3. List it (Verify)
    response = s3.list_buckets()
    print("\n🔍 Current Buckets:")
    for bucket in response['Buckets']:
        if 'jayden-lab' in bucket['Name']:
            print(f" - {bucket['Name']}")

    # 4. Cleanup (Delete it so you don't pay)
    print("\n--- Cleaning Up ---")
    delete_bucket(my_bucket)