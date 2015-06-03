from django.contrib import admin
from state_data.models import State, Category, Option, Fact, StateFact

# Register your models here.
admin.site.register(State)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(Fact)
admin.site.register(StateFact)