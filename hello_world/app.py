import json
# import requests
import pandas as pd
from datetime import date


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    # print("d1 =", d1)

    msg = 'not found'

    query = event['currentIntent']['slots']['Query']

    # try:
    # query = 'Amazon Athena'
    data = parse_csv()
    for index in range(0, len(data['Product'])):
        if data['Product'][index] == query:
            msg = data['Details'][index]
            # print(data['Details'][index])
    # print(data.head(3))
    # for key, value in data.iteritems():
        # print(key+' '+value)
    # print(data['Product'][0])
    # except Exception as e:
        # print(e)

    # response = {
    #     "sessionAttributes": {
    #     },
    #     "dialogAction": {
    #         "type": "Close",
    #         "fulfillmentState": "Fulfilled",
    #         "message": {
    #             "contentType": "PlainText",
    #             "content": result
    #         }
    #     }
    # }

    
    return  {
      "sessionAttributes": { 
     
      },
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "PlainText",
          "content": msg
          }
        }
    }

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": d1,
    #         # "csv_data": data,
    #         "result": msg
    #         # "location": ip.text.replace("\n", "")
    #     }),
    # }


def parse_csv():
    # my_sheet = 'Sheet1'
    file_name = 'List of AWS Services.csv'
    # df = pd.read_excel(file_name, sheet_name=my_sheet)
    data = pd.read_csv(filepath_or_buffer=file_name)
    # print(data['Product'][0])
    # print(type(data))
    # print(data['Product'], type(data['Product']))
    # print(df, df['Correct Answer'])
    return data
