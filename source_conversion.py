import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact, Source


def populate():
    Source.objects.all().delete()

    # State facts =============================
    state_facts = StateFact.objects.all()

    for each_state_fact in state_facts:
        label = each_state_fact.source_label
        url = each_state_fact.source_url

        if url:
            new_source = Source(label=label, url=url)
            new_source.save()

            each_state_fact.sources.add(new_source)

            each_state_fact.save()

    # Facts =============================
    facts = Fact.objects.all()

    for each_fact in facts:
        label = each_fact.source_label
        url = each_fact.source_url

        if url:
            new_source = Source(label=label, url=url)
            new_source.save()

            each_fact.sources.add(new_source)

            each_fact.save()


# Start execution here!
if __name__ == '__main__':
    print ("Starting state_data population script...")
    populate()