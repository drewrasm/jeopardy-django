class HelloMessage:

    INITIAL_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "This is the Jeopardy Bot! :triumph: \n\n"
                "*Hello, hope your day is fantastic!*"
            ),
        },
    }
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username = "jeopardybot"
        self.icon_emoji = ":dromedary_camel:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.INITIAL_BLOCK,
            ],
        }