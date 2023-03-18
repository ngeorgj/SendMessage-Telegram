   def send_message(self, bot_id, room_id, text, parse_mode="MarkdownV2"):
        return requests.get(
            f"https://api.telegram.org/bot{bot_id}/sendMessage?parse_mode={parse_mode}&chat_id={room_id}&text={text}")
