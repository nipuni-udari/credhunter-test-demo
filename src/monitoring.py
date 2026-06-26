import time
import requests

DATADOG_API_KEY = "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d"
DATADOG_BASE_URL = "https://api.datadoghq.com/api/v1"


def submit_metric(metric_name: str, value: float, tags: list = None) -> bool:
    url = f"{DATADOG_BASE_URL}/series"
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": DATADOG_API_KEY,
    }
    payload = {
        "series": [
            {
                "metric": metric_name,
                "points": [[int(time.time()), value]],
                "tags": tags or [],
                "type": "gauge",
            }
        ]
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 202


def record_request_latency(endpoint: str, latency_ms: float) -> bool:
    return submit_metric(
        "app.request.latency",
        latency_ms,
        tags=[f"endpoint:{endpoint}"],
    )


def record_error_count(service: str, count: int) -> bool:
    return submit_metric(
        "app.errors.count",
        float(count),
        tags=[f"service:{service}"],
    )
