# Cross-Account S3 File Transfer

## Overview

This project showcases a secure and efficient method for transferring files between Amazon S3 buckets hosted in different AWS accounts. It leverages AWS IAM roles, Lambda functions, and AWS SDK/APIs to facilitate seamless file transfers. The solution ensures data integrity and adheres to best practices in cloud-based file management.

## Features

- Secure file transfer between AWS S3 buckets in separate AWS accounts.
- No need to download and upload files manually; all transfers are automated.
- Demonstrates AWS IAM role configuration, Lambda function setup, and event-driven file transfer.
- Emphasizes adherence to AWS security best practices.

## Usage

To use this solution, follow these high-level steps:

1. **Prerequisites:**
   - Ensure you have access to the AWS Management Console for both source and destination AWS accounts.

2. **Source AWS Account Setup:**
   - Create an S3 bucket in the source AWS account.
   - Configure an IAM role with the necessary permissions, including AWS Lambda execution and S3 access. Establish a trust relationship allowing the destination AWS account to assume this role.

3. **Destination AWS Account Setup:**
   - Create an S3 bucket in the destination AWS account.
   - Set up an IAM role with permissions to access the destination S3 bucket. Create a trust relationship allowing the source AWS account to assume this role.

4. **Lambda Function Configuration:**
   - Develop an AWS Lambda function in the source AWS account using the AWS Management Console.
   - Attach the IAM role created in the source account to the Lambda function.
   - Implement the provided Python script to handle the file transfer logic.

5. **File Transfer:**
   - Upload files to the source S3 bucket in the source AWS account using the AWS Management Console.
   - The Lambda function will automatically trigger and copy files to the destination S3 bucket in the destination AWS account.

## Security Considerations

- Emphasize the security measures taken, such as IAM roles and bucket policies, to ensure that only authorized entities can access and transfer files.
- Highlight data encryption and secure transmission practices.
- Discuss IAM best practices for least privilege access.

