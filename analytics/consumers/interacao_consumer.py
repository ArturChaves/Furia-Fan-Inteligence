import json
import os
from utils.rabbitmq import connect_rabbitmq
from services.interacao_service import salvar_interacao

RABBITMQ_QUEUE_INTERACAO = os.getenv("RABBITMQ_QUEUE_INTERACAO", "fan.interacao")

def processar_interacao(ch, method, properties, body):
    try:
        data = json.loads(body.decode())
        whatsapp_number = data.get("whatsapp_number")
        question = data.get("question")
        answer = data.get("answer")

        print("📋 Nova interação recebida:")
        print(f"📱 WhatsApp: {whatsapp_number}")
        print(f"❓ Pergunta: {question}")
        print(f"💬 Resposta: {answer}")

        salvar_interacao(whatsapp_number, question, answer)
    except Exception as e:
        print(f"❌ Erro ao processar mensagem: {e}")

def main():
    channel = connect_rabbitmq()
    channel.queue_declare(queue=RABBITMQ_QUEUE_INTERACAO, durable=True)

    print(f"✅ Aguardando mensagens na fila '{RABBITMQ_QUEUE_INTERACAO}'. Pressione CTRL+C para sair.")

    channel.basic_consume(
        queue=RABBITMQ_QUEUE_INTERACAO,
        on_message_callback=processar_interacao,
        auto_ack=True
    )

    channel.start_consuming()

if __name__ == "__main__":
    main()