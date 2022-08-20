class Player:

    def __init__(self, first_name, last_name, position, team, number, touchdowns = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team
        self.number = number
        self.touchdowns = touchdowns

    @property
    def player_card(self):
        return '{} {}, {} for the {}, number {}'.format(self.first_name, self.last_name, self.position, self.team, self.number)