from pyspark.sql import SparkSession
import boto3

#create a sparksesison
print("Creating a Spark Session:")
spark: SparkSession = (
    SparkSession.builder
    .appName('AWS_S3_Workspace') #type: ignore
    .getOrCreate()
)


#Configure your aws in CLI to ignore hardcoding

#Create connection to AWS S3
print("Connecting to S3...")
s3_client = boto3.client('s3') #this takes access keys from aws configure in CLI 


#list the available buckets in s3
response = s3_client.list_buckets()
print("These are the buckets available from s3:")
for i in response['Buckets']:
    print(i['Name'])


#create a new bucket with just bucket name
print("Creating a new bucket....")
response = s3_client.create_bucket(
    Bucket = 'aws-demo-bucke-thru-python',
    CreateBucketConfiguration= {
        'LocationConstraint': 'us-east-2'
    }
)

print(response)



















print("-----------------------------------------------------------------------------")
print("**************************Execution Completed********************************")
print("-----------------------------------------------------------------------------")
spark.stop()