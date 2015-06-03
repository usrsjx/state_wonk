import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'state_wonk.settings')

import django
django.setup()

from state_data.models import State, Option, Category, Fact, StateFact

import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://kff.org/health-reform/state-indicator/state-health-insurance-marketplace-types/#table')
print (r.status, r.data)

federally_facilitate_mkt_option = Option('Federally-facilitated Marketplace')
state_partnership_mkt_option = Option('State-Partnership Marketplace')
state_based_mkt_option = Option('State-based Marketplace')
federally_supported_state_based_mkt_option = Option('Federally-supported State-based Marketplace')
