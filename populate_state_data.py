import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State

def populate_states():
    states = []
    states.append(State(name='Alabama', abbr='AL'))
    states.append(State(name='Alaska', abbr='AK'))
    states.append(State(name='Arizona', abbr='AZ'))
    states.append(State(name='Arkansas', abbr='AR'))
    states.append(State(name='California', abbr='CA'))
    states.append(State(name='Colorado', abbr='CO'))
    states.append(State(name='Connecticut', abbr='CT'))
    states.append(State(name='Delaware', abbr='DE'))
    states.append(State(name='Florida', abbr='FL'))
    states.append(State(name='Georgia', abbr='GA'))
    states.append(State(name='Hawaii', abbr='HI'))
    states.append(State(name='Idaho', abbr='ID'))
    states.append(State(name='Illinois', abbr='IL'))
    states.append(State(name='Indiana', abbr='IN'))
    states.append(State(name='Iowa', abbr='IA'))
    states.append(State(name='Kansas', abbr='KS'))
    states.append(State(name='Kentucky', abbr='KY'))
    states.append(State(name='Louisiana', abbr='LA'))
    states.append(State(name='Maine', abbr='ME'))
    states.append(State(name='Maryland', abbr='MD'))
    states.append(State(name='Massachusetts', abbr='MA'))
    states.append(State(name='Michigan', abbr='MI'))
    states.append(State(name='Minnesota', abbr='MN'))
    states.append(State(name='Mississippi', abbr='MS'))
    states.append(State(name='Missouri', abbr='MO'))
    states.append(State(name='Montana', abbr='MT'))
    states.append(State(name='Nebraska', abbr='NE'))
    states.append(State(name='Nevada', abbr='NV'))
    states.append(State(name='New Hampshire', abbr='NH'))
    states.append(State(name='New Jersey', abbr='NJ'))
    states.append(State(name='New Mexico', abbr='NM'))
    states.append(State(name='New York', abbr='NY'))
    states.append(State(name='North Carolina', abbr='NC'))
    states.append(State(name='North Dakota', abbr='ND'))
    states.append(State(name='Ohio', abbr='OH'))
    states.append(State(name='Oklahoma', abbr='OK'))
    states.append(State(name='Oregon', abbr='OR'))
    states.append(State(name='Pennsylvania', abbr='PA'))
    states.append(State(name='Rhode Island', abbr='RI'))
    states.append(State(name='South Carolina', abbr='SC'))
    states.append(State(name='South Dakota', abbr='SD'))
    states.append(State(name='Tennessee', abbr='TN'))
    states.append(State(name='Texas', abbr='TX'))
    states.append(State(name='Utah', abbr='UT'))
    states.append(State(name='Vermont', abbr='VT'))
    states.append(State(name='Virginia', abbr='VA'))
    states.append(State(name='Washington', abbr='WA'))
    states.append(State(name='West Virginia', abbr='WV'))
    states.append(State(name='Wisconsin', abbr='WI'))
    states.append(State(name='Wyoming', abbr='WY'))

    for each in states:
        each.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate_states()