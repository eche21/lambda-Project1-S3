#looping through all the transaction list, if it is refund, print refund and the amount
#
import json
import boto3
s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']

    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)

    content = response['Body']

    jsonObject = json.loads(content.read())

    transactions = jsonObject['transactions']

    for record in transactions:
      if record['transactionType']=='REFUND':
          print("TransactionType: " + record['transactionType'])
          print("TransactionAmount: " + str(record['amount']))
