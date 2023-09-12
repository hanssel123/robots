import json
from formant.sdk.agent.v1 import Client as FormantClient

if __name__ == "__main__":
    fclient = FormantClient()

    # # Ingest text datapoint
    # fclient.post_text("examples.text", "Hanssel")

    # # # Ingest numeric datapoint
    # # fclient.post_numeric("example.numeric", 3)

    # # Ingest numericset datapoint, 'percent' and '%' units adds
    # # additional donut visualization
    # fclient.post_numericset(
    #     "example.numericset",
    #     {
    #         "frequency": (998, "Hz"),
    #         "usage": (30, "percent"),
    #         "warp factor": (6.0, None),
    #     },
    # )

    # # Ingest bitset datapoint
    # fclient.post_bitset(
    #     "example.bitset", {"flag": False}
    # )

    # # Ingest geolocation datapoint
    # fclient.post_geolocation("example.geolocation", 10, 10)  # lat, long

    # # Ingest battery
    # fclient.post_battery("example.battery", 50, 50, 50, 50)

    # print("Successfully ingested datapoints. AND...")

    # fclient.create_event(message="Test error event", notify=True, severity="error")

    # fclient.create_teleop_intervention_request("1");

    # fclient.send_command_response();

    # fclient.post_image()
    while True:
        # Ingest bitset datapoint
        fclient.post_bitset(
            "example.bitset2", {"flag": False}
        )
        


