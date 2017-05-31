from django.db import models


class Trait(models.Model):
    value = models.CharField(max_length=20)

class Item(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date added')
    picture = models.ImageField()
    traits = models.ManyToManyField(
            Trait,
            through='VotedTrait',
            through_fields=('item', 'trait'),
            )

class VotedTrait(models.Model):
    trait = models.ForeignKey(
            Trait,
            on_delete=models.CASCADE)
    item = models.ForeignKey(
            Item,
            on_delete=models.CASCADE)
    value = models.PositiveIntegerField()
    PLUS_MINUS_CHOICE = (
            ('+', 'Plus'),
            ('-', 'Minus'),
            ('z', 'Zero'),
    )
    plusminus = models.CharField(
            max_length=1,
            choices=PLUS_MINUS_CHOICE,
            default='z',
    )
