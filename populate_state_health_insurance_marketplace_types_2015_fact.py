import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact


def populate():

    category = Category.objects.get(name="Labor Rights")

    fact = Fact(category=category,
                    title="State Health Insurance Marketplace Types, 2015",
                    type=Fact.OPT_TYPE,
                    source_label="The Henry J. Kaiser Family Foundation",
                    source_url="http://kff.org/health-reform/state-indicator/state-health-insurance-marketplace-types/#map")

    federal_mkt = Option(label="Federally-facilitated Marketplace", fact=fact, color="#E0ECF8")
    federal_supp_state_mkt = Option(label="Federally-supported State-based Marketplace", fact=fact, color="#5882FA")
    state_partnership_mkt = Option(label="State-Partnership Marketplace", fact=fact, color="#A9D0F5")
    state_based_mkt = Option(label="State-based Marketplace", fact=fact, color="#0B2161")

    state_facts = []
    state_facts.append(StateFact(state=State.objects.get(name='Alaska'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Alabama'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Arizona'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Florida'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Georgia'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Indiana'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Kansas'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Louisiana'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Maine'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Missouri'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Mississippi'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Montana'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='North Carolina'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='North Dakota'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Nebraska'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='New Jersey'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Ohio'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Oklahoma'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Pennsylvania'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='South Carolina'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='South Dakota'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Tennessee'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Texas'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Utah'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Virginia'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Wisconsin'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Wyoming'), details=None, fact=fact, opt=federal_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='New Mexico'), details=None, fact=fact, opt=federal_supp_state_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Nevada'), details=None, fact=fact, opt=federal_supp_state_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Oregon'), details=None, fact=fact, opt=federal_supp_state_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Arkansas'), details=None, fact=fact, opt=state_partnership_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Delaware'), details=None, fact=fact, opt=state_partnership_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Iowa'), details=None, fact=fact, opt=state_partnership_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Illinois'), details=None, fact=fact, opt=state_partnership_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Michigan'), details=None, fact=fact, opt=state_partnership_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='New Hampshire'), details=None, fact=fact, opt=state_partnership_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='West Virginia'), details=None, fact=fact, opt=state_partnership_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='California'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Colorado'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Connecticut'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Hawaii'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Idaho'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Kentucky'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Massachusetts'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Maryland'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Minnesota'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='New York'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Rhode Island'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Vermont'), details=None, fact=fact, opt=state_based_mkt))
    state_facts.append(StateFact(state=State.objects.get(name='Washington'), details=None, fact=fact, opt=state_based_mkt))

    for each_state_fact in state_facts:
        each_state_fact.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate()
