import subprocess

teste = int(subprocess.run(['bash', 'getpower.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8'))

print(f"Consumo: {teste} W")