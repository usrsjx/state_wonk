from django.shortcuts import render
from django import forms

from state_data.models import Category, Fact, StateFact, Option


def view_map(request):

    context = {}

    if request.method == 'GET':
        category_id = request.GET.get('selected_category')
        fact_id = request.GET.get('selected_fact')

        categories = Category.objects.all()
        category = None
        fact = None
        facts_for_category = {}
        state_facts = {}

        if category_id:
            category = Category.objects.get(id=category_id)
            facts_for_category = Fact.objects.filter(category=category)

            if fact_id:
                fact = Fact.objects.get(id=fact_id)
                state_facts = StateFact.objects.filter(fact=fact)

        context = {'categories': categories,
                   'category': category,
                   'fact': fact,
                   'facts_for_category': facts_for_category,
                   'state_facts': state_facts,
                   'map_key': get_map_key(fact)}

    return render(request, 'state_data/map.html', context)


def get_map_key(fact):
    map_key = {}

    if fact and fact.type == Fact.OPT_TYPE:
        options_for_fact = Option.objects.filter(fact=fact)

        for each_option in options_for_fact:
            state_facts = StateFact.objects.filter(opt=each_option)
            label = each_option.label + " ({0})".format(state_facts.count())
            map_key[label] = each_option.color

    return map_key