# capstone-200
serverless Image Processing Pipeline 
Project Description

This project implements a serverless image processing pipeline that automatically resizes images uploaded to an S3 bucket. When a user uploads an image, the system triggers a workflow that resizes the image to a thumbnail size and stores it in a separate S3 bucket. The solution is fully scalable, event-driven, and uses AWS managed services.

Key Features

* An S3 bucket for storing original images

* A Lambda function that is triggered when a new image is uploaded

* The Lambda function resizes the image using the Pillow (Python) library

* A second S3 bucket stores the resized images

* A Step Functions state machine orchestrates the workflow

* An API Gateway endpoint allows manual triggering of the process

* CloudWatch monitors and logs the entire pipeline

# High-Level Architecture 
```
+-----------------+     +-----------------+     +--------------------+     +-----------------+
|   API Gateway   | --> | Step Functions  | --> |  Lambda Function   | --> |       S3        |
+-----------------+     +-----------------+     +--------------------+     +-----------------+
          ^                                                                                    
          |                                                                                    
+-----------------+                                                                            
|   CloudWatch    |                                                                            
+-----------------+
```

# Explanation of the Workflow

### API Gateway

* Provides an endpoint that can manually trigger the Step Functions workflow.

* Useful for tests, dashboards, or external applications.

### Step Functions

* Orchestrates the image processing steps.

* Invokes the Lambda function.

* Checks whether image resizing was successful.

### Lambda Function

* Automatically triggered when a new image is uploaded to the source S3 bucket.

* Resizes the image to a thumbnail size using an image processing library (Pillow).

* Writes the resized image to the destination S3 bucket.

### S3 buckets

* One bucket stores original images.

* Another bucket stores resized images.

### CloudWatch

* Captures logs for Lambda and Step Functions.

* Helps monitor performance and troubleshoot issues.

# Prerequisites

* AWS account with permissions to create S3 buckets, Lambda functions, Step Functions, API Gateway, and IAM roles.

* Lambda runtime environment (Python or Node.js).

* Image processing library included as a Lambda layer (e.g., Pillow for Python or Sharp for Node.js).

* Optional: AWS CLI for local deployment and testing.

# Full Step By Step Guide

### Create S3 Buckets

* Original Images Bucket.

* Processed Images Bucket.

* Configure permissions so Lambda can read from the original bucket and write to the processed bucket.

### Create the Lambda Function

* Go to AWS Lambda → Create Function

* Choose Python runtime

* Assign the IAM role created earlier

* Add the Pillow layer to this function


### Optional: Step Functions

Deploy a Step Function workflow if multiple processing steps are required.

Copy the Step Function ARN for reference and integration with Lambda.

### Configure API Gateway

Deploy an API endpoint to allow HTTP image uploads.

Connect API Gateway to the Lambda function.

Note the final API URL for image upload.

### Test the Entire Pipeline
Test 1: Upload an Image

* Upload a JPG or PNG into your original S3 bucket.

* EventBridge was triggered

* Step Functions started

* Lambda function processed the image

* Resized image appears in the second S3 bucket

Test 2: Trigger via API

* Go to your API Gateway endpoint.

* Use POST with a JSON body (no code shown here).

* Step Functions will execute.

* Lambda will run and generate a thumbnail.
# URL
https://dg5a7b7e2e.execute-api.ca-central-1.amazonaws.com/prod 
