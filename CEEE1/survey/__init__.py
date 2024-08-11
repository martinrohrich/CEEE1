from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = ('survey'
                   )
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number = models.IntegerField(label='Participant Number?', min=1, max=50)
    age = models.IntegerField(label='What is your age?', min=13, max=95)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    hand = models.StringField(
        choices=[['Right', 'Right'], ['Left', 'Left']],
        label='What is your dominant hand ?',
        widget=widgets.RadioSelect,
    )
    paina = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Do you feel/ have pain - for period up to 3 month ?',
        widget=widgets.RadioSelect,
    )
    painch = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Do you feel/ have pain - for period more than 3 month ?',
        widget=widgets.RadioSelect,
    )

    activ = models.IntegerField(
        label='''
        Do you have any kind of the physical activity ? Yes/No: 
        If Yes, specify type of the activity. If No, type No'''
    )
    dis_def = models.StringField(
        choices=[['Yes', 'Yes'], ['No', 'No']],
        label='Are you holder of the OZZ/ disability card ?',
        widget=widgets.RadioSelect,
    )



# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['number', 'age', 'gender', 'hand', 'paina', 'painch', 'activ', 'dis_def']




page_sequence = [Demographics]
