#looping through all the transaction list, if it is refund, print refund and the amount
#
import json
import boto3
s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = 'lambda-datajson-bucket'

    key = 'data.json'

    response = s3.get_object(Bucket=bucket, Key=key)

    content = response['Body']

    jsonObject = json.loads(content.read())

    transactions = jsonObject['transactions']

    for record in transactions:
      if record['transactionType']=='REFUND':
        print("TransactionType: " + record['transactionType'])
        print("TransactionAmount: " + str(record['amount']))

    print(jsonObject)
