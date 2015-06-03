import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact

def populate():
    category = Category.objects.get(name="Labor Rights")

    pvd_fact = Fact(category=category,
                    title="Paid Vacation Days, 2015",
                    type=Fact.OPT_TYPE,
                    source_label="Boston Globe",
                    source_url="http://www.bostonglobe.com/business/2014/08/13/one-few-countries-that-doesn-mandate-paid-vacation-time/eqodEqumohPyca5kt6hrZO/story.html")
    pvd_fact.save()

    non_pvd_state_opt = Option(label="No Paid Vacation Days Law", fact=pvd_fact, color="#BDBDBD")
    non_pvd_state_opt.save()

    all_states = State.objects.all()

    state_facts = []

    for each_state in all_states:
        state_facts.append(StateFact(state=each_state, fact=pvd_fact, opt=non_pvd_state_opt))

    for each_state_fact in state_facts:
        each_state_fact.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate()