#!/usr/bin/env python3
import time
import random
import numpy as np
from formant.sdk.agent.v1 import Client as FormantClient
if __name__ == "__main__":
    print("Starting the ingestion....")
    fclient = FormantClient()
    status = {"Online": True, "Button toggled": False}
    def triangular(inf, sup, num):
        if num <= (inf + sup) // 2:
            return num
        else:
            return inf + sup - num
    # def post_random_numeric_data():
    #     fclient.post_numeric("example.numeric", float(random.randint(0, 100)))
    def post_random_numericset_data():
        fclient.post_numericset(
            "example.numericset",
            {
                "frequency": (random.randint(70, 999), "Hz"),
                "usage": (random.randint(0, 100), "percent"),
                "warp factor": (float(random.randint(0, 100)), None),
            },
        )
    while True:
        for i in range(1, 21):
            value = triangular(1, 20, i)
            fclient.post_numeric("example.numeric", value)
        post_random_numericset_data()
        time.sleep(2)