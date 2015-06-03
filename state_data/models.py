from django.db import models
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')


class State(models.Model):
    abbr = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.abbr

    class Meta:
        ordering = ('abbr',)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Source(models.Model):
    label = models.CharField(max_length=100, unique=False, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ('label',)


class Fact(models.Model):
    PCT_TYPE = "pct"
    NBR_TYPE = "nbr"
    DLR_TYPE = 'dlr'
    OPT_TYPE = "opt"

    FACT_TYPE_CHOICES = (
        (PCT_TYPE, 'Percentage'),
        (NBR_TYPE, 'Number'),
        (DLR_TYPE, 'Dollar'),
        (OPT_TYPE, 'Multiple Options'),
    )

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=3, choices=FACT_TYPE_CHOICES, default=OPT_TYPE)
    details = models.TextField(blank=True, null=True, unique=False)

    # Sources can be set on the Fact (applies to all states) or on the StateFact (applies only to the single state).
    sources = models.ManyToManyField(Source, null=True)

    def format_number_for_fact(self, flt_nbr):
        if self.type == self.PCT_TYPE:
            return "{0:.0f}%".format(flt_nbr * 100)
        elif self.type == self.NBR_TYPE:
            return "{:d}".format(int(flt_nbr))
        elif self.type == self.DLR_TYPE:
            return locale.currency(flt_nbr)
        else:
            return None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Option(models.Model):
    label = models.CharField(max_length=100, unique=True)
    fact = models.ForeignKey(Fact)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ('label',)


class Range(models.Model):
    fact = models.ForeignKey(Fact)

    start = models.FloatField(blank=True, null=True)
    end = models.FloatField(blank=True, null=True)

    color = models.CharField(max_length=7)

    def __str__(self):
        return '{0} - {1}'.format(
            self.fact.format_number_for_fact(self.start),
            self.fact.format_number_for_fact(self.end))

    class Meta:
        ordering = ('start',)


class StateFact(models.Model):
    state = models.ForeignKey(State)
    fact = models.ForeignKey(Fact)
    details = models.TextField(blank=True, null=True, unique=False)

    # Sources can be set on the Fact (applies to all states) or on the StateFact (applies only to the single state).
    sources = models.ManyToManyField(Source, null=True)

    # One of these will have a value, the other will be None:
    nbr = models.FloatField(blank=True, null=True)
    opt = models.ForeignKey(Option, blank=True, null=True)

    def get_val(self):
        if self.pct is not None:
            return self.fact.format_number_for_fact(self.nbr)
        elif self.opt is not None:
            return self.opt.label
        else:
            return None

    def __str__(self):
        return '{0} > {1}: {2}'.format(str(self.fact), self.state.name, self.get_val())

    class Meta:
        ordering = ('fact', 'state',)


