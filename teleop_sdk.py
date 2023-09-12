#! /usr/bin/env python3
import time
import random
import subprocess

from formant.sdk.agent.v1 import Client as FormantClient

if __name__ == "__main__":
    print("Starting the ingestion....")
    fclient = FormantClient(
        ignore_throttled=True,
        ignore_unavailable=True,
    )

    # Limit upload speed to 100mbits and introduce 10ms delay
    subprocess.check_output(
        "sudo tc qdisc add dev ens5 root netem delay 10ms rate 100mbit".split()
        )

    status = {"Online": True, "Button toggled": False}

    def handle_teleop(control_datapoint):
        if control_datapoint.stream == "Buttons":
            if (str(control_datapoint.bitset.bits[0]).find("true") != -1):
                status["Button toggled"] = not (status["Button toggled"])

    def handle_command_request(request):
        if request.command == "disconnect_device":
            disconnect_device()

    fclient.register_teleop_callback(handle_teleop, ["Buttons"])
    fclient.register_command_request_callback(
        handle_command_request, command_filter=["disconnect_device"]
        )

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

    def turtlebot():
        while True:
            ps = subprocess.Popen(["ps", "x"], stdout=subprocess.PIPE)
            o1 = subprocess.Popen(["grep", "-v", "grep"], stdin=ps.stdout,
                                  stdout=subprocess.PIPE)
            sp = subprocess.Popen(["grep", "-c", "turtlebot3_gazebo"],
                                  stdin=o1.stdout, universal_newlines=True,
                                  stdout=subprocess.PIPE)
            output, _ = sp.communicate()
            clean_output = output.split()[0]
            if int(clean_output) != 3:
                print("turtlebot is not running")
                subprocess.run("/home/ubuntu/bin/turtlebot.sh")
                time.sleep(15)
            else:
                break
        print("turtlebot is running")

    def disconnect_device():
        result = subprocess.run(["sudo", "ip", "route", "show", "default"], stdout=subprocess.PIPE, encoding='utf-8')
        gateway = result.stdout.split()[2]
        subprocess.run(["sudo", "ip", "route", "delete", "default"])
        time.sleep(20)
        subprocess.run(["sudo", "ip", "route", "add", "default", "via", gateway])

    while True:
        turtlebot()
        post_status()
        post_random_bitset_data()
        post_random_geolocation_data()
        post_random_text_data()
        post_random_numeric_data()
        post_random_numericset_data()
        time.sleep(0.5)
