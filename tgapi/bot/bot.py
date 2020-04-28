from typing import (Optional,
                    List,
                    Union)

from tgapi.bot.base_bot import BaseBot
from tgapi import (tgtypes,
                   apimethods)


class Bot(BaseBot):

    async def get_updates(self,
                          offset: Optional[int] = None,
                          limit: Optional[int] = None,
                          timeout: Optional[int] = None) -> \
                          List[tgtypes.Update]:
        """
        Use this method to receive incoming updates using long polling (wiki).

        Notes:
        1. This method will not work if an outgoing webhook is set up.
        2. In order to avoid getting duplicate updates,
           recalculate offset after each server response.

        Source: https://core.telegram.org/bots/api#getupdates

        Args:
            offset: Identifier of the first update to be returned.
            limit: The number of updates to be retrieved.
            timeout: Timeout in seconds for long polling.

        Returns: An Array of Update objects is returned.


        """

        result = await apimethods.get_updates(session=self.session,
                                              url=self.url,
                                              offset=offset,
                                              limit=limit,
                                              timeout=timeout)

        return tgtypes.dataclass_factory(tgtypes.Update, result)

    async def send_message(self,
                           chat_id: Union[int, str],
                           text: str,
                           parse_mode: Optional[str] = None,
                           disable_web_page_preview: Optional[bool] = None,
                           disable_notification: Optional[bool] = None,
                           reply_to_message_id: Optional[int] = None
                           ) -> tgtypes.Message:
        """
        Use this method to send text messages.

        Source: https://core.telegram.org/bots/api#sendmessage

        Args:
            chat_id: Unique identifier for the target chat
                     or username of the target channel.
            text: Text of the message to be sent.
            parse_mode: Send Markdown or HTML, if you want
                        Telegram apps to show bold, italic,
                        fixed-width text or inline URLs in your bot's message.
            disable_web_page_preview: Disables link previews
                                      for links in this message.
            disable_notification: Sends the message silently.
                                  Users will receive a notification
                                  with no sound.
            reply_to_message_id: If the message is a reply,
                                 ID of the original message.

        Returns: On success, the sent Message is returned.

        """

        result = await apimethods.send_message(session=self.session,
                                               url=self.url,
                                               chat_id=chat_id,
                                               text=text,
                                               parse_mode=parse_mode,
                                               disable_web_page_preview=
                                               disable_web_page_preview,
                                               disable_notification=
                                               disable_notification,
                                               reply_to_message_id=
                                               reply_to_message_id)

        return tgtypes.dataclass_factory(tgtypes.Message, result)

    @property
    async def me(self):
        """
        A simple method for testing your bot's auth token.
        Requires no parameters. Returns basic information about the bot
        in form of a User object.

        Returns: User object.

        """

        result = await apimethods.get_me(session=self.session,
                                         url=self.url)

        return tgtypes.dataclass_factory(tgtypes.User, result)

    async def reply_to_message(self,
                               chat_id: Optional[Union[int, str]] = None,
                               message_id: Optional[Union[int, str]] = None,
                               text: Optional[str] = None) -> \
                               tgtypes.Message:
        _message_id = message_id
        _chat_id = chat_id
        if not message_id or not chat_id:
            _upd = await self.get_updates()
            _message_id = _upd[-1].to_dict()["message"]["message_id"]
            _chat_id = _upd[-1].to_dict()["message"]["from"]["id"]

        _text = text if text else "Ku-ku"

        result = await self.send_message(_chat_id,
                                         _text,
                                         reply_to_message_id=_message_id)

        return tgtypes.dataclass_factory(tgtypes.Message, result.to_dict())

