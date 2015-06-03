import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact


def populate():
    category = Category.objects.get(name="Labor Rights")

    pfl_fact = Fact(category=category,
                    title="Paid Family Leave, 2015",
                    type=Fact.OPT_TYPE,
                    source_label="Washington Post",
                    source_url="http://www.washingtonpost.com/blogs/govbeat/wp/2014/06/24/what-paid-family-leave-looks-like-in-the-three-states-that-require-it/")
    pfl_fact.save()

    pfl_state_opt = Option(label="Paid Family Leave Law", fact=pfl_fact, color="#FF4000")
    pfl_state_opt.save()

    non_pfl_state_opt = Option(label="No Paid Family Leave Law", fact=pfl_fact, color="#BDBDBD")
    non_pfl_state_opt.save()

    state_facts = []
    state_facts.append(StateFact(state=State.objects.get(name="New Jersey"), details="Enacted 2002", fact=pfl_fact, opt=pfl_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="California"), details="Enacted 2004", fact=pfl_fact, opt=pfl_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Rhode Island"), details="Enacted 2014", fact=pfl_fact, opt=pfl_state_opt))

    all_non_pfl_states = list(State.objects.all())
    for each_pfl_state_fact in state_facts:
        all_non_pfl_states.remove(each_pfl_state_fact.state)

    for each_non_pfl_state in all_non_pfl_states:
        state_facts.append(StateFact(state=each_non_pfl_state, fact=pfl_fact, opt=non_pfl_state_opt))

    for each_state_fact in state_facts:
        each_state_fact.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate()