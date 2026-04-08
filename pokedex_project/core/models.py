# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abilities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    short_effect = models.TextField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abilities'


class Evolutions(models.Model):
    evolved_pokedex_number = models.OneToOneField('Pokemon', models.DO_NOTHING, db_column='evolved_pokedex_number', primary_key=True)
    base_pokedex_number = models.ForeignKey('Pokemon', models.DO_NOTHING, db_column='base_pokedex_number', related_name='evolutions_base_pokedex_number_set', blank=True, null=True)
    min_level = models.IntegerField(blank=True, null=True)
    item_required = models.CharField(max_length=20, blank=True, null=True)
    time_of_day = models.CharField(max_length=20, blank=True, null=True)
    trade_required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evolutions'


class Locations(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Moves(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    pp = models.IntegerField(blank=True, null=True)
    type = models.ForeignKey('Types', models.DO_NOTHING, blank=True, null=True)
    effect_chance = models.IntegerField(blank=True, null=True)
    damage_class = models.CharField(max_length=15, blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves'


class Pokemon(models.Model):
    pokedex_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    sp_attack = models.IntegerField(blank=True, null=True)
    sp_defense = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    flavor_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon'


class PokemonAbility(models.Model):
    pk = models.CompositePrimaryKey('pokedex_number', 'ability_id')
    pokedex_number = models.ForeignKey(Pokemon, models.DO_NOTHING, db_column='pokedex_number')
    ability = models.ForeignKey(Abilities, models.DO_NOTHING)
    is_hidden = models.BooleanField(blank=True, null=True)
    slot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_ability'


class PokemonLocation(models.Model):
    pk = models.CompositePrimaryKey('pokedex_number', 'location_id')
    pokedex_number = models.ForeignKey(Pokemon, models.DO_NOTHING, db_column='pokedex_number')
    location = models.ForeignKey(Locations, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pokemon_location'


class PokemonMove(models.Model):
    pk = models.CompositePrimaryKey('pokedex_number', 'move_id')
    pokedex_number = models.ForeignKey(Pokemon, models.DO_NOTHING, db_column='pokedex_number')
    move = models.ForeignKey(Moves, models.DO_NOTHING)
    learn_method = models.CharField(max_length=25, blank=True, null=True)
    level_learned_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_move'


class PokemonType(models.Model):
    pk = models.CompositePrimaryKey('pokedex_number', 'type_id')
    pokedex_number = models.ForeignKey(Pokemon, models.DO_NOTHING, db_column='pokedex_number')
    type = models.ForeignKey('Types', models.DO_NOTHING)
    slot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_type'


class Regions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class TypeEffectiveness(models.Model):
    pk = models.CompositePrimaryKey('attacking_type_id', 'defending_type_id')
    attacking_type = models.ForeignKey('Types', models.DO_NOTHING)
    defending_type = models.ForeignKey('Types', models.DO_NOTHING, related_name='typeeffectiveness_defending_type_set')
    damage_multiplier = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_effectiveness'


class Types(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'
