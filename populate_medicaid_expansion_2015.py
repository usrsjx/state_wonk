import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact


def populate():
    category = Category.objects.get(name="Obamacare")

    me_fact = Fact(category=category,
                    title="Medicaid Expansion, 2015",
                    type=Fact.OPT_TYPE,
                    source_label="statereforum",
                    source_url="https://www.statereforum.org/Medicaid-Expansion-Decisions-Map")
    me_fact.save()

    expand_state_opt = Option(label="Expanded Medicaid", fact=me_fact, color="#0B2161")
    expand_state_opt.save()

    expand_waiver_state_opt = Option(label="Expanded Medicaid w/ Waiver for Alternative Program", fact=me_fact, color="#A9D0F5")
    expand_waiver_state_opt.save()

    pending_expand_waiver_state_opt = Option(label="Pending Medicaid Expansion w/ Waiver for Alternative Program", fact=me_fact, color="#A9D0F5")
    pending_expand_waiver_state_opt.save()

    no_expand_state_opt = Option(label="Not Expanding Medicaid", fact=me_fact, color="#BDBDBD")
    no_expand_state_opt.save()


    expand_states = State.objects.filter(abbr__in=['HI', 'WA', 'OR', 'CA', 'NV', 'AZ', 'NM', 'CO', 'ND', 'MN', 'IL', 'KY', 'OH', 'WV', 'MD', 'DE', 'VT', 'NY', 'NJ', 'CT', 'RI', 'MA'])
    expand_waiver_states = State.objects.filter(abbr__in=['AR', 'IA', 'IN', 'MI', 'PA', 'NH'])
    pending_expand_waiver_states = State.objects.filter(abbr__in=['MT'])

    all_states = list(State.objects.all())

    all_expand_states = []
    all_expand_states.extend(expand_states)
    all_expand_states.extend(expand_waiver_states)
    all_expand_states.extend(pending_expand_waiver_states)

    no_expand_states = [state for state in all_states if state not in all_expand_states]

    state_facts = []
    for each_state in expand_states:
        state_facts.append(StateFact(state=each_state, fact=me_fact, opt=expand_state_opt))

    for each_state in expand_waiver_states:
        state_facts.append(StateFact(state=each_state, fact=me_fact, opt=expand_waiver_state_opt))

    for each_state in pending_expand_waiver_states:
        state_facts.append(StateFact(state=each_state, fact=me_fact, opt=pending_expand_waiver_state_opt))

    for each_state in no_expand_states:
        state_facts.append(StateFact(state=each_state, fact=me_fact, opt=no_expand_state_opt))


    for each_state_fact in state_facts:
        each_state_fact.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate()