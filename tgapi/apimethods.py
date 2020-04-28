"""Telegram API wrapper"""
from enum import Enum
from typing import List, Optional, Union

import aiohttp

import settings
from .utils import urlformatters
from . import exceptions


class _APIMethods(Enum):
    """

    """
    get_me = "getMe"
    get_updates = "getUpdates"
    set_webhook = "setWebhook"
    delete_webhook = "deleteWebhook"
    get_webhook_info = "getWebhookInfo"
    send_message = "sendMessage"
    forward_message = "forwardMessage"
    webhook_info = "WebhookInfo"
    delete_message = "deleteMessage"
    get_chat = "getChat"


def generate_payload(payload) -> Union[list, Exception]:
    """

    Args:
        payload:

    Returns:

    """
    if payload["ok"]:
        return payload["result"]
    else:
        raise Exception(payload)


async def set_webhook(session: aiohttp.ClientSession,
                      url: str) -> Union[list, Exception]:
    """
    Use this method to specify a url and receive
    incoming updates via an outgoing webhook.
    Whenever there is an update for the bot,
    telegram will send an HTTPS POST request
    to the specified url, containing a JSON-serialized Update.
    In case of an unsuccessful request, telegram will give up
    after a reasonable amount of attempts. Returns True on success.

    Args:
        session:
        url: string type url, to which need to set up telegram webhook
    Examples:
        url = https://www.example.com/<token>
    Returns:
        dict object with response from telegram server.

    """
    async with session.get(
            urlformatters.create_request_url(url,
                                             _APIMethods.set_webhook.value)) \
            as response:
        payload = await response.json()
        return generate_payload(payload)


async def delete_webhook(session: aiohttp.ClientSession,
                         url: str) -> Union[list, Exception]:
    """
    Use this method to remove webhook integration
    if you decide to switch back to getUpdates.
    Returns True on success.
    Requires no parameters.
    Args:
        session:
        url: string type url, to which need to delete telegram webhook
    Returns:
        dict object with response from telegram server.

    """
    async with session.get(
            urlformatters.create_request_url(url,
                                             _APIMethods.delete_webhook.value)) as response:
        payload = await response.json()
        return generate_payload(payload)


async def webhook_info(url: str) -> Union[list, Exception]:
    ...


async def get_updates(session: aiohttp.ClientSession,
                      url: str,
                      offset: Optional[int] = None,
                      limit: Optional[int] = None,
                      timeout: Optional[int] = None,
                      allowed_updates: Optional[List[str]] = None) -> Union[list, Exception]:
    """

    Args:
        session:
        url:
        offset:
        limit:
        timeout:
        allowed_updates:

    Returns:

    """
    if not settings.DEBUG:
        raise exceptions.FunctionNotAllowed(
            "Use long polling methods only in debug mode!")
    _params = {}
    _offset = offset if offset else 0
    if offset:
        _params.update({"offset": offset})
    else:
        _params.update({"offset": _offset})
    if limit:
        _params.update({"limit": limit})
    if timeout:
        _params.update({"timeout": timeout})
    if allowed_updates:
        _params.update({"allowed_updates": allowed_updates})

    if _params:
        async with session.get(
                urlformatters.create_request_url_with_params(url,
                                                             _APIMethods.get_updates.value,
                                                             **_params)) as response:
            payload = await response.json()
            _offset += 1
            return generate_payload(payload)
    else:
        async with session.get(
                urlformatters.create_request_url(url,
                                                 _APIMethods.get_updates.value)) as response:
            payload = await response.json()

            return generate_payload(payload)


async def delete_message(session: aiohttp.ClientSession, url: str,
                         chat_id: str, message_id: str) -> \
        Union[list, Exception]:
    """

    Args:
        session:
        url:
        chat_id:
        message_id:

    Returns:

    """

    async with session.get(
            urlformatters.create_request_url_with_params(url,
                                                         _APIMethods.delete_message.value,
                                                         chat_id=chat_id,
                                                         message_id=message_id
                                                         )) as response:
        payload = await response.json()
        return generate_payload(payload)


async def send_message(session: aiohttp.ClientSession,
                       url: str,
                       chat_id: int,
                       text: str,
                       parse_mode: Optional[str] = None,
                       disable_web_page_preview: Optional[bool] = None,
                       disable_notification: Optional[bool] = None,
                       reply_to_message_id: Optional[int] = None) -> \
        Union[dict, Exception]:
    """

    Args:
        session:
        url:
        chat_id:
        text:
        parse_mode:
        disable_web_page_preview:
        disable_notification:
        reply_to_message_id:

    Returns:

    """

    _params = {"chat_id": chat_id,
               "text": text}
    if parse_mode:
        _params.update({"parse_mode": parse_mode})
    if disable_web_page_preview:
        _params.update({"disable_web_page_preview": disable_web_page_preview})
    if disable_notification:
        _params.update({"disable_notification": disable_notification})
    if reply_to_message_id:
        _params.update({"reply_to_message_id": reply_to_message_id})

    async with session.post(
            urlformatters.create_request_url_with_params(
                url,
                _APIMethods.send_message.value,
                **_params)
    ) as response:

        payload = await response.json()

        return generate_payload(payload)


async def get_chat(session: aiohttp.ClientSession,
                   url: str,
                   chat_identifier: Union[int, str]) -> \
        Union[list, Exception]:
    """

    Args:
        session:
        url:
        chat_identifier:

    Returns:

    """
    async with session.get(urlformatters.create_request_url_with_params(
            url=url,
            method=_APIMethods.get_chat.value,
            chat_id=chat_identifier
    )) as response:
        payload = await response.json()

        return generate_payload(payload)


async def get_me(session: aiohttp.ClientSession,
                 url: str) -> Union[dict, Exception]:
    """

    Args:
        session:
        url:

    Returns:

    """
    async with session.get(urlformatters.create_request_url(
            url,
            _APIMethods.get_me.value
    )) as response:
        payload = await response.json()

        return generate_payload(payload)
