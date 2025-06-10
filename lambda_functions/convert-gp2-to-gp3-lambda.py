import json
import boto3

def get_volume_id_from_arn(volume_arn):
    arn_parts = volume_arn.split(':')
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))  # ✅ Log event

    try:
        volume_arn = event['resources'][0]
        volume_id = get_volume_id_from_arn(volume_arn)
        print(f"Volume ARN: {volume_arn}, Volume ID: {volume_id}")

        ec2_client = boto3.client('ec2')

        response = ec2_client.modify_volume(
            VolumeId=volume_id,
            VolumeType='gp3'
        )

        print("Modify volume response:", response)

        return {
            'statusCode': 200,
            'body': json.dumps('Volume modified successfully')
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

