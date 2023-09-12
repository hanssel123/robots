#! /usr/bin/env python3
import time
import random
import cv2
import requests
import numpy as np
import os
import json
from formant.sdk.agent.v1 import Client as FormantClient

# Prepare and encode an image
image_response = requests.get("https://qa-agent-resources.s3.amazonaws.com/formant.png")
image_content = image_response.content
image_array = np.frombuffer(image_content, np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
encoded = cv2.imencode(".png", image)[1].tostring()
with open("formant.png", "wb") as f:
    f.write(image_response.content)
file_path = os.path.join(os.getcwd(), "formant.png")

if __name__ == "__main__":
    print("Starting the ingestion....")
    fclient = FormantClient(
        ignore_throttled=True,
        ignore_unavailable=True,
    )
    agent_id = fclient.get_agent_id()
    print({agent_id})
    status = {"Online": True, "Button toggled": False}

    def handle_teleop(control_datapoint):
        if control_datapoint.stream == "Buttons":
            if (str(control_datapoint.bitset.bits[0]).find("true") != -1):
                status["Button toggled"] = not (status["Button toggled"])

    fclient.register_teleop_callback(handle_teleop, ["Buttons"])

    #  Ingest all datapoint
    def post_random_geolocation_data():
        dec_lat = random.random()/100
        dec_lon = random.random()/100
        fclient.post_geolocation("example.geolocation",  22.835+dec_lat, 33.631667 +
                                 dec_lon)  # lat, long

    def post_random_text_data():
        hex1 = '%012x' % random.randrange(16**12)  # 12 char random string
        fclient.post_text("example.text", "Send text example processed" + hex1)

    def post_random_numeric_data():
        fclient.post_numeric("example.numeric", float(random.randint(0, 100)))

    def post_random_numericset_data():
        fclient.post_numericset(
            "example.numericset",
            {
                "frequency": (random.randint(70, 999), "Hz"),
                "usage": (random.randint(0, 100), "percent"),
                "warp factor": (float(random.randint(0, 100)), None),
            },
        )

    def post_random_bitset_data():
        fclient.post_bitset(
            "example.bitset",
            status,
        )

    def post_status():
        fclient.post_bitset(
            "Status",
            status,
        )

    def post_json():
        message = {
            "name": "Alice",
            "age": 30,
            "email": "alice@example.com",
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": "12345",
            },
            "phone_numbers": ["555-1234", "555-5678"],
        }

        fclient.post_json("myjson", json.dumps(message))
    def post_image():
        print("posting image")
        global image_bytes
        fclient.post_image(
            "billing.image",
            encoded,
        )

    while True:
        post_status()
        post_random_bitset_data()
        post_random_geolocation_data()
        post_random_text_data()
        post_random_numeric_data()
        post_random_numericset_data()
        post_image()
        post_json()
        time.sleep(0.5)