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

Run the following command to send a single Telegram message:

```bash
echo Hello world | ./notify.py
```

Alternatively, put `notify.ph` in `$PATH` and pipe the output
of any command to `notify_loop.sh`:

```bash
some-command | ./notify_loop.sh
```

That will send one Telegram message per input line.
