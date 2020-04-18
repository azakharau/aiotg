"""Webhook utils for Telegram API"""

import requests


async def set_webhook(url: str):
    """
    Use this method to specify a url and receive
    incoming updates via an outgoing webhook.
    Whenever there is an update for the bot,
    telegram will send an HTTPS POST request
    to the specified url, containing a JSON-serialized Update.
    In case of an unsuccessful request, telegram will give up
    after a reasonable amount of attempts. Returns True on success.

    Args:
        url: string type url, to which need to set up telegram webhook
    Examples:
        url = https://www.example.com/<token>
    Returns:
        dict object with response from telegram server.

    """
    resp = requests.get(url)
    await resp.json()


async def delete_webhook(url: str):
    """
    Use this method to remove webhook integration
    if you decide to switch back to getUpdates.
    Returns True on success.
    Requires no parameters.
    Args:
        url: string type url, to which need to delete telegram webhook
    Returns:
        dict object with response from telegram server.

    """
    resp = requests.get(url)
    await resp.json()

async def webhook_info(url: str):
    ...
