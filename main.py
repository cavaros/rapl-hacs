import subprocess, json

teste = json.loads(subprocess.run(['./execpowernote.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8'))["powercap"]

print(f"Consumo: {teste} W")