#!/usr/bin/python3
# encoding=utf-8

import paho.mqtt.client as mqtt
import logging
import time
import sys
import json
import signal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SERVER = 'localhost'
PORT = 1883
USERNAME = None
PASSWORD = None

SENSOR_NAME = ""
SENSOR_ID = '123'
UNITS = 'ppm'
CLIENT_ID = f"sensor/{SENSOR_NAME}"
connected = False

done = False

def exit(signalNumber, frame):  
    global done
    done = True
    return

def on_connect(mqttc, obj, flags, rc):
    global connected
    connected = True

    logger.info(f"Connected to {mqttc._host}:{mqttc._port}")

    mqttc.publish(f"{CLIENT_ID}/status", 'online', retain=True)
    # HA AUTOCONFIG
    mqttc.publish(f'homeassistant/sensor/{SENSOR_ID}/config', json.dumps({
        'name': SENSOR_NAME,
        'availability_topic': f'{CLIENT_ID}/status',  # Online, Offline
        'unit_of_measurement': UNITS,
        'unique_id': SENSOR_NAME,
        'state_topic': f'{CLIENT_ID}/state',  # Value published
        'force_update': True}), retain=True)

    return True


def on_message(mqttc, obj, msg):
    logger.debug(f"{msg.topic} {str(msg.qos)} {str(msg.payload)}")


def loop(mqttc):
    logger.debug("Loop start")

    while not done:
        if not connected:
            logger.debug("Not Connected")
        else:
            # Publish timestamp
            mqttc.publish(f"{CLIENT_ID}/state", str(time.time()), retain=True)

        time.sleep(60)

    return True


def main():

    signal.signal(signal.SIGINT, exit)
    mqttc = mqtt.Client(client_id='clients/' + CLIENT_ID)
    mqttc.will_set(f"{CLIENT_ID}/status", 'offline', retain=True)

    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    if USERNAME is not None:
	    mqttc.username_pw_set(username=USERNAME, password=PASSWORD)

    mqttc.loop_start()

    logger.info("Connecting to MQTT")
    mqttc.connect(host=SERVER, port=PORT, keepalive=60)

    logger.info("Running")

    while not done:
        try:
            if not loop(mqttc):
                mqttc.disconnect()
                break
            time.sleep(60)
        except:
            logger.exception("")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-v':
        logger.setLevel(logging.DEBUG)
    main()

