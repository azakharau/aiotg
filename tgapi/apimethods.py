"""Telegram API wrapper"""
from enum import Enum

import aiohttp

import settings
from utils.strformatters import prepare_request_url
from . import exceptions


class TMethods(Enum):
    get_me = "getMe"
    get_updates = "getUpdates"
    set_webhook = "setWebhook"
    delete_webhook = "deleteWebhook"
    get_webhook_info = "getWebhookInfo"
    send_message = "sendMessage"
    forward_message = "forwardMessage"
    webhook_info = "WebhookInfo"


async def set_webhook(session: aiohttp.ClientSession, url: str):
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
    async with session.post(
            prepare_request_url(url, TMethods.set_webhook.value)) as response:
        payload = await response.json()
        if payload["ok"]:
            return payload["result"]


async def delete_webhook(session: aiohttp.ClientSession, url: str):
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
    async with session.post(
            prepare_request_url(url,
                                TMethods.delete_webhook.value)) as response:
        payload = await response.json()
        if payload["ok"]:
            return payload["result"]


async def webhook_info(url: str):
    ...


async def get_updates(session: aiohttp.ClientSession, url: str) -> dict:
    if not settings.DEBUG:
        raise exceptions.FunctionNotAllowedInProduction(
            "Use long polling methods only in debug mode!")
    async with session.post(
            prepare_request_url(url, TMethods.get_updates.value)) as response:
        payload = await response.json()
        if payload["ok"]:
            return payload["result"]
