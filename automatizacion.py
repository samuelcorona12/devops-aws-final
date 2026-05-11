import boto3
from datetime import datetime, timedelta

# Clientes AWS
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
s3 = boto3.client('s3')
autoscaling = boto3.client('autoscaling')

print("=" * 50)
print("INSTANCIAS EC2")
print("=" * 50)

# Listar instancias EC2
response = ec2.describe_instances()

instance_ids = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:

        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']

        print(f"ID: {instance_id}")
        print(f"Tipo: {instance_type}")
        print(f"Estado: {state}")
        print("-" * 30)

        if state == "running":
            instance_ids.append(instance_id)

print("\n")
print("=" * 50)
print("USO DE CPU - CLOUDWATCH")
print("=" * 50)

# Métricas CPU últimas 24 horas
for instance_id in instance_ids:

    metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            }
        ],
        StartTime=datetime.utcnow() - timedelta(hours=24),
        EndTime=datetime.utcnow(),
        Period=3600,
        Statistics=['Average']
    )

    print(f"\nInstancia: {instance_id}")

    datapoints = metrics['Datapoints']

    if datapoints:
        for data in sorted(datapoints, key=lambda x: x['Timestamp']):
            print(
                f"Fecha: {data['Timestamp']} | "
                f"CPU Promedio: {round(data['Average'],2)}%"
            )
    else:
        print("No hay métricas disponibles.")

print("\n")
print("=" * 50)
print("BUCKETS S3")
print("=" * 50)

# Listar buckets y objetos
buckets = s3.list_buckets()

for bucket in buckets['Buckets']:

    bucket_name = bucket['Name']

    print(f"\nBucket: {bucket_name}")

    try:
        objects = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in objects:
            for obj in objects['Contents']:
                print(f"Objeto: {obj['Key']}")
        else:
            print("Bucket vacío.")

    except Exception as e:
        print(f"Error accediendo bucket: {e}")

print("\n")
print("=" * 50)
print("AUTO SCALING GROUPS")
print("=" * 50)

# Auto Scaling Groups
asg_response = autoscaling.describe_auto_scaling_groups()

groups = asg_response['AutoScalingGroups']

if groups:
    for group in groups:

        print(f"\nNombre: {group['AutoScalingGroupName']}")
        print(f"Min Size: {group['MinSize']}")
        print(f"Max Size: {group['MaxSize']}")
        print(f"Desired Capacity: {group['DesiredCapacity']}")

else:
    print("No existen Auto Scaling Groups.")

