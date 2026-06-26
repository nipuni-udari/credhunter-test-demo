import urllib.request
import json

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T12AB34CD/B56EF78GH/abcdefghijklmnopqrstuvwx"
DEFAULT_CHANNEL = "#alerts"


def send_alert(message: str, channel: str = DEFAULT_CHANNEL) -> bool:
    payload = json.dumps({"text": message, "channel": channel}).encode("utf-8")
    req = urllib.request.Request(
        SLACK_WEBHOOK_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status == 200


def send_deployment_notice(service: str, version: str, env: str) -> bool:
    message = f":rocket: *{service}* `{version}` deployed to *{env}*"
    return send_alert(message, channel="#deployments")


def send_error_report(error: Exception, context: str) -> bool:
    message = f":x: Error in `{context}`:\n```{error}```"
    return send_alert(message, channel="#errors")
