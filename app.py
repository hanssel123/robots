import subprocess
import time

from formant.sdk.agent.v1 import Client as FormantClient
fclient = FormantClient()
def handle_command_request(request):
    if request.command == "event_command":
        return print ("event command sent")
    if request.command == "calendar_command":
        return print ("calendar command")
    if request.command == "issue_command":
        return print ("issue command sent")
    if request.command == "motor_check":
        return print ("motor check")

    if request.files is not None:
        for file in request.files:
            # example of reading files from a command
            print(
                "Command sent with file "
                + file["name"]
                + " accessible via "
                + file["url"]
            )
if __name__ == "__main__":
    fclient.register_command_request_callback(
        handle_command_request, command_filter=["event_command", "calendar_command", "issue_command", "motor_check"]
    )

    # idly spin while the command request callback listens for commands
    while True:
        time.sleep(0.1)