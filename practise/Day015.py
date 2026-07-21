from collections import Counter


def analyze_logs(logs):
    status_codes = [log["status"] for log in logs]

    return {
        "total_requests": len(logs),
        "successful_requests": sum(200 <= status < 300 for status in status_codes),
        "client_errors": sum(400 <= status < 500 for status in status_codes),
        "server_errors": sum(500 <= status < 600 for status in status_codes),
        "status_summary": Counter(status_codes)
    }


def display_report(report):
    print("===== LOG ANALYSIS REPORT =====")
    print(f"Total Requests: {report['total_requests']}")
    print(f"Successful Requests: {report['successful_requests']}")
    print(f"Client Errors: {report['client_errors']}")
    print(f"Server Errors: {report['server_errors']}")
    print(f"Status Summary: {report['status_summary']}")


logs = [
    {"endpoint": "/api/users", "status": 200},
    {"endpoint": "/api/users", "status": 200},
    {"endpoint": "/api/orders", "status": 404},
    {"endpoint": "/api/login", "status": 500},
    {"endpoint": "/api/products", "status": 201},
]

report = analyze_logs(logs)
display_report(report)