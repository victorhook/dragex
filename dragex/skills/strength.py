from skills.skill import Skill, Ability


class Strength(Skill):

    def __init__(self, experience: int):
        super().__init__(
            'Strength',
            experience, [
            Ability('Beginner', 'You are beginning to learn to damage', 5),
            Ability('Intermediate', 'You are good at dealing damage', 10),
            Ability('Pro', 'You are pro at dealing damage', 20),
        ])
