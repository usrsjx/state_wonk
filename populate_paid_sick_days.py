import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact


def populate():
    category = Category.objects.get(name="Labor Rights")

    psd_fact = Fact(category=category,
                    title="Paid Sick Days, 2015",
                    type=Fact.OPT_TYPE,
                    source_label="Wikipedia",
                    source_url="http://en.wikipedia.org/wiki/Sick_leave#United_States")
    psd_fact.save()

    psd_state_opt = Option(label="Paid Sick Days Law", fact=psd_fact, color="#FF8000")
    psd_state_opt.save()

    non_psd_state_opt = Option(label="No Paid Sick Days Law", fact=psd_fact, color="#BDBDBD")
    non_psd_state_opt.save()

    state_facts = []
    state_facts.append(StateFact(state=State.objects.get(name="Connecticut"), details="Passed July 1, 2011", fact=psd_fact, opt=psd_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="California"), details="Passed Sept 8, 2014", fact=psd_fact, opt=psd_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Massachusetts"), details="Passed Nov 4, 2014", fact=psd_fact, opt=psd_state_opt))

    all_non_psd_states = list(State.objects.all())
    for each_psd_state_fact in state_facts:
        all_non_psd_states.remove(each_psd_state_fact.state)

    for each_non_psd_state in all_non_psd_states:
        state_facts.append(StateFact(state=each_non_psd_state, fact=psd_fact, opt=non_psd_state_opt))

    for each_state_fact in state_facts:
        each_state_fact.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate()