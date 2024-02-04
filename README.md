Network Sniffing Detector - MacOS

Adversaries may sniff network traffic to capture info about an environment, including authentication material passed over the network. Detector checks for running processes and commands to notify.

What it does

The detector looks for running processes that match the names of known sniffing software, captures the information, and creates a hit on the security dashboard provided by Howler. the same process is repeated if a suspicious looking command is executed. Solution adheres to the detection recommendations outlined in the MITRE analysis of the network sniffing technique.

https://attack.mitre.org/techniques/T1040/

How we built it

The detector is built using a continually running python script. The python script uses subprocesses and system utilities to access data on running processes and executed commands, and checks these against a list of known potentially malicious events. The demo and testing is done through Atomic Red Team test cases

https://atomicredteam.io/discovery/T1040/

Challenges we ran into

The atomic testing framework required modification to run on the host system, getting logs of commands executed is difficult.

Accomplishments that we're proud of

We are pleased that the script runs as expected and was able to detect both command execution and process creation.

What we learned

Containerized red team testing using atomic red team and Docker
Analysis of system status using logging and process monitoring. ## What's next for Network Sniffing Detector - MacOS Increasing the robustness of the program with more research into possible malicious processes.
Using regex to allow for better classification of processes and commands.
