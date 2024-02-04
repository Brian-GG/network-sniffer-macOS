import psutil
import subprocess

from howler_client import get_client

USERPASS = ('briangrig', 'briangrig')
process_names_to_check = ["tshark"]
search_string = "tshark -c"
howler = get_client("https://howler.collaboration.cyber.gc.ca", auth=USERPASS)

def search_log_for_string(search_string):
    try:
        # Execute the 'log show' command and capture the output
        command_output = subprocess.check_output(['log', 'show', '--last', '1s'], universal_newlines=True)

        if search_string in command_output:
            lines = command_output.splitlines()
            for line in lines:
                if search_string in line:
                    print("Found in log line: ", line)
                    break
            detection = "Suspicious command executed: " + line
            create_alert(detection)
    except subprocess.CalledProcessError as e:
        print(f"Error executing 'log show' command: {e}")
        
def check_processes(process_list):
    running_processes = psutil.process_iter(['pid', 'name'])

    for process in running_processes:
        if process.info['name'] in process_list:
            print(f"Process {process.info['name']} (PID {process.info['pid']}) is running.")
            detection = "Suspicious process running: " + str(process.info['name']) + " " + str(process.info['pid'])
            create_alert(detection)
            break

def create_alert(detection):
    print("Potetnial Network Sniffing Detected! Creating alert")

    howler.hit.create(
        {
            "howler.analytic": "Network Traffic Anomaly",
            "howler.detection": detection,
            "howler.score": 0,
            "threat.technique.id": "T1040",
            "threat.technique.name": "Network Sniffing",
            "threat.technique.reference": "https://attack.mitre.org/techniques/T1040/",
        }
    )

while True:
    search_log_for_string(search_string)
    check_processes(process_names_to_check)