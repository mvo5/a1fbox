from config import FRITZ_IP_ADDRESS, FRITZ_USERNAME, FRITZ_PASSWORD
from phonebook import Phonebook
from callmonitor import CallMonitor, CallMonitorType, CallMonitorLine, CallMonitorLog

if __name__ == "__main__":
    print("To stop enter '!' (exclamation mark) followed by ENTER key..")

    cm_log = CallMonitorLog(file_prefix="callmonitor", daily=True, anonymize=False)
    cm = CallMonitor(logger=cm_log)
    # cm_log.parse_from_file('log/callmonitor-test.log')

    key = ""
    while key != "!":
        key = input()

    cm.stop()
