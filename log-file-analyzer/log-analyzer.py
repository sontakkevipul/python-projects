log_file = "application.log"

error_count = 0
warning_count = 0
info_count = 0

try:
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    print("\n===== LOG FILE ANALYSIS =====")
    print("ERROR   :", error_count)
    print("WARNING :", warning_count)
    print("INFO    :", info_count)

except FileNotFoundError:
    print("Log file not found.")
