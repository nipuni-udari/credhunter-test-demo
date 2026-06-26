# CredHunter-X Test Demo

A minimal Python project for testing the [CredHunter-X](https://github.com/nipuni-udari/CredHunter-X) secret scanning pipeline.

## Project Structure

```
credhunter-test-demo/
├── .github/
│   └── workflows/
│       └── credhunter-x.yml       <- CI pipeline
├── .credhunter.yml                 <- CredHunter-X configuration
├── src/
│   ├── aws_client.py              <- AWS S3 helper
│   ├── vcs_client.py              <- GitHub API helper
│   ├── messaging.py               <- Slack notification helper
│   └── settings.py                <- Django application settings
├── tests/
│   └── fixtures/
│       └── sample_config.py       <- Fixture file (ignored by scanner)
└── README.md
```

## Setup

1. Push this repository to GitHub.
2. Add your `OPENAI_API_KEY` as a repository secret under **Settings → Secrets and variables → Actions**.
3. Push any commit to trigger the workflow.

## Expected Scan Results

| File | Secret Type | Expected Severity |
|---|---|---|
| `src/aws_client.py` | AWS IAM key pair | Critical |
| `src/vcs_client.py` | GitHub Personal Access Token | High |
| `src/messaging.py` | Slack Webhook URL | Medium |
| `src/settings.py` | Django development secret key | Low |
| `tests/fixtures/sample_config.py` | Multiple secrets | Ignored (path excluded) |

## Configuration

The `.credhunter.yml` `ignore_paths` section excludes `tests/**` from processing.
GitLeaks will still detect the secrets inside that directory, but CredHunter-X will
mark them as ignored findings rather than blocking or warning findings.

The workflow uses `fail_on: high`, so Critical and High findings fail the pipeline,
while Medium and Low findings produce warnings only.

Without `OPENAI_API_KEY` set, the deterministic engine is used as a fallback.
With the key set, the LLM re-ranks each finding more precisely across all four
severity levels (critical, high, medium, low).
