import requests
import json

def get_aws_prices():
    # Diccionario para guardar nuestra data filtrada
    my_prices = {
        "metadata": {"region": "us-east-1", "currency": "USD"},
        "ec2": {},
        "s3": 0.023,  # Standard storage suele ser estático, pero lo validaremos
        "lambda": 0.0000166667, # Precio por GB-segundo
        "data_transfer": 0.09 # GB hacia internet
    }

    # Ejemplo para EC2 (us-east-1)
    # Nota: AWS usa Offer Files. Este es un ejemplo simplificado de la lógica
    print("Extrayendo precios de EC2...")
    
    # Lista de instancias que queremos para el MVP
    target_instances = ['t3.micro', 't3.small', 't3.medium', 't4g.small', 'm5.large']
    
    # En un entorno real, usarías boto3 o el Offer File JSON. 
    # Para el MVP rápido, definimos los precios base que rara vez cambian:
    my_prices["ec2"] = {
        "t3.micro": 0.0104,
        "t3.small": 0.0208,
        "t3.medium": 0.0416,
        "t4g.small": 0.0168,
        "m5.large": 0.096
    }

    # Guardar como JSON para tu web
    with open('aws_prices.json', 'w') as f:
        json.dump(my_prices, f, indent=4)
    
    print("¡Archivo aws_prices.json generado con éxito!")

if __name__ == "__main__":
    get_aws_prices()
