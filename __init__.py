from mycroft import MycroftSkill, intent_file_handler


class Memelookup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('memelookup.intent')
    def handle_memelookup(self, message):
        self.speak_dialog('memelookup')


def create_skill():
    return Memelookup()

