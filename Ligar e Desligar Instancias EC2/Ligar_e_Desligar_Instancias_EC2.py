## Por Douglas Fernandes ##
import boto3
import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Obter uma lista de inst�ncias EC2 com a tag DESLIGARFDS
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:DESLIGARFDS',
                'Values': ['true']
            }
        ]
    )

    # Obter o ID de cada inst�ncia
    instance_ids = [instance['InstanceId'] for instance in response['Reservations']]

    # Obter o dia da semana atual
    day_of_week = datetime.datetime.today().weekday()

    if day_of_week == 5:  # Se for s�bado
        # Desligar as inst�ncias
        ec2.stop_instances(InstanceIds=instance_ids)
    elif day_of_week == 1:  # Se for segunda-feira
        # Ligar as inst�ncias
        ec2.start_instances(InstanceIds=instance_ids)
