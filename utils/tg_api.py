"""Telegram API wrapper"""
from enum import Enum

import aiohttp
import requests


class TMethods(Enum):
    get_me = "getMe"
    get_updates = "getUpdates"
    set_webhook = "setWebhook"
    delete_webhook = "deleteWebhook"
    get_webhook_info = "getWebhookInfo"
    send_message = "sendMessage"
    forward_message = "forwardMessage"
    webhook_info = "WebhookInfo"


def prepare_method(method: str) -> str:
    return f"/{method}"


def prepare_request_url(url: str, method: str) -> str:
    return f"{url}{prepare_method(method)}"


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


async def get_updates(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.post(
            prepare_request_url(url, TMethods.get_updates.value)) as response:
        payload = await response.json()
        if payload["ok"]:
            return payload["result"][-1]
