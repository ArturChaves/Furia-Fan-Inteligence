import json
import os
from utils.rabbitmq import connect_rabbitmq
from services.cadastro_service import salvar_cadastro

RABBITMQ_QUEUE_CADASTRO = os.getenv("RABBITMQ_QUEUE_CADASTRO", "fan.cadastro_finalizado")

def processar_cadastro(ch, method, properties, body):
    try:
        data = json.loads(body.decode())
        print("📋 Novo cadastro recebido:")
        salvar_cadastro(data)  # Passa o dicionário inteiro, sem reatribuir campos
    except Exception as e:
        print(f"❌ Erro ao processar mensagem: {e}")

def main():
    channel = connect_rabbitmq()
    channel.queue_declare(queue=RABBITMQ_QUEUE_CADASTRO, durable=True)

    print(f"✅ Aguardando mensagens na fila '{RABBITMQ_QUEUE_CADASTRO}'. Pressione CTRL+C para sair.")

    channel.basic_consume(
        queue=RABBITMQ_QUEUE_CADASTRO,
        on_message_callback=processar_cadastro,
        auto_ack=True
    )

    channel.start_consuming()

if __name__ == "__main__":
    main()
