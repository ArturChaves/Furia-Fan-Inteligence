import json
from utils.rabbitmq import connect_rabbitmq
from services.segmentar_fan_service import salvar_segmento

import os
from dotenv import load_dotenv

load_dotenv()
RABBITMQ_QUEUE_SEGMENTACAO = os.getenv("RABBITMQ_QUEUE_SEGMENTACAO", "fan.segmentado")

def callback(ch, method, properties, body):
    try:
        print("📥 Mensagem recebida na fila!")
        mensagem = json.loads(body)
        whatsapp_number = mensagem.get("whatsapp_number")
        cluster = mensagem.get("cluster")

        print(f"➡️ Segmentando fã {whatsapp_number} no cluster {cluster}")
        salvar_segmento(whatsapp_number, cluster)
    except Exception as e:
        print(f"❌ Erro ao processar mensagem: {e}")

def main():
    print("🚀 Inicializando consumidor de segmentação...")
    channel = connect_rabbitmq()
    print(f"📡 Conectado com sucesso. Aguardando mensagens na fila '{RABBITMQ_QUEUE_SEGMENTACAO}'.")

    channel.queue_declare(queue=RABBITMQ_QUEUE_SEGMENTACAO, durable=True)
    channel.basic_consume(queue=RABBITMQ_QUEUE_SEGMENTACAO, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    main()