import pika
import sys
import time


def connect():
    credentials = pika.PlainCredentials('admin', 'Admin@123')
    parameters = pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='/',
        credentials=credentials,
        connection_attempts=sys.maxsize,
        # retry_delay=5,
        # client_properties={ 
        #     "description": desc
        # }
    )
    conn = pika.SelectConnection(
        parameters=parameters,
        on_open_callback=on_open_connection_callback, 
        on_open_error_callback=on_open_error_connection_callback,
        on_close_callback=on_close_connection_callback,
    )
    conn.ioloop.start()


def on_open_connection_callback(conn):
    print(f"conexion rabbitmq establecida")


def on_open_error_connection_callback(conn, ex):
    print(f'error en apertura de conexion rabbitmq: {ex}')
    time.sleep(5)
    reconnect()


def on_close_connection_callback(conn, ex):
    print(f"conexion rabbitmq cerrada: {ex}")
    reconnect()


def reconnect():
    print(f"reconectando rabbitmq")
    connect()


def close(conn):
    if conn.is_open():
        conn.close()
        #reconnect()