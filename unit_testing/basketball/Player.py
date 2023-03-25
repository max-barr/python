class Player:

    def __init__(self, first_name, last_name, position, team, number):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team
        self.number = number

    def tee_him_up(self):
        return '{} {} has been assessed a technical foul. The other team will shoot one free throw.'.format(self.first_name, self.last_name)

    @property
    def player_card(self):
        return '{} {}, number {}, {} for the {}'.format(self.first_name, self.last_name, self.number, self.position, self.team)