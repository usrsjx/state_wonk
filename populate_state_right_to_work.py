import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact


def populate():
    category = Category.objects.get(name="Labor Rights")

    rtw_fact = Fact(category=category,
                    title="Right to Work States, 2015",
                    type=Fact.OPT_TYPE,
                    source_label="Wikipedia",
                    source_url="http://en.wikipedia.org/wiki/Right-to-work_law#U.S._states_with_right-to-work_laws")
    rtw_fact.save()

    rtw_state_opt = Option(label="Right to Work State", fact=rtw_fact, color="#04B4AE")
    rtw_state_opt.save()

    non_rtw_state_opt = Option(label="Not Right to Work", fact=rtw_fact, color="#BDBDBD")
    non_rtw_state_opt.save()

    state_facts = []
    state_facts.append(StateFact(state=State.objects.get(name="Alabama"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Arizona"), details="Constitution, State Constitution Article 25 approved 1946", fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Arkansas"), details="Constitution, 1947, Amendment 34", fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Florida"), details="Constitution, 1944, revised 1968, Article 1, Section 6", fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Georgia"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Idaho"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Indiana"), details="State law, 2012", fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Iowa"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Kansas"), details="Constitution, 1958, Article 15, Section 12", fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Louisiana"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Michigan"), details="State law, 2012", fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Mississippi"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Nebraska"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Nevada"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="North Carolina"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="North Dakota"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Oklahoma"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="South Carolina"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="South Dakota"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Tennessee"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Texas"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Utah"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Virginia"), fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Wisconsin"), details="State law, 2015", fact=rtw_fact, opt=rtw_state_opt))
    state_facts.append(StateFact(state=State.objects.get(name="Wyoming"), fact=rtw_fact, opt=rtw_state_opt))

    all_non_rtw_states = list(State.objects.all())
    for each_rtw_state_fact in state_facts:
        all_non_rtw_states.remove(each_rtw_state_fact.state)

    for each_non_rtw_state in all_non_rtw_states:
        state_facts.append(StateFact(state=each_non_rtw_state, fact=rtw_fact, opt=non_rtw_state_opt))

    for each_state_fact in state_facts:
        each_state_fact.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate()