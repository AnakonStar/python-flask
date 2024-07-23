from flask import request;
import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue='forms')
# channel.basic_publish(exchange='', routing_key='forms', body=data)

def init_forms_routes(app):
    @app.route(f'/send-forms', methods=['POST'])
    def sendForms():
        data = request.json
        print(data)
        return data
