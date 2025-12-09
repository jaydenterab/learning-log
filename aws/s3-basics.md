# AWS CLI: S3 Basics
**Date:** 2025-12-09

## Lab: "Hello World" with S3
Successful connection established between local terminal (using `aws configure`) and AWS Cloud.

## Commands Executed
1. **Create Bucket:** `aws s3 mb s3://unique-name`
   - Creates a logical container for objects.
   - Names must be globally unique (DNS-compliant).

2. **List Buckets:** `aws s3 ls`
   - Confirmed the bucket was created in the `ap-southeast-2` region.

3. **Delete Bucket:** `aws s3 rb s3://unique-name`
   - Cleaned up resources to prevent clutter/costs.

## Key Takeaway
Managing resources via CLI is significantly faster than the Console. This is the foundation for scripting automation.
*Note: Fixed git configuration.*
