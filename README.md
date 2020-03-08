# telegram-notify

Send stdin as a Telegram message to a specific user.

## Requirements

- Telegram bot (API token)
- python
- python-requests

## Setup

Set API token and chat ID in `notify.ph`.

Make sure `notify.py` is executable.

## Usage

```bash
echo Hello world | ./notify.py
```

