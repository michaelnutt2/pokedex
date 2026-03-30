# Pokemon Database
## How to Setup
After starting your codespace, run the following:
```bash
psql -c CREATE DATABASE pokemon
psql -X pokemon < setup_script
```
## Pokemon Database Schema
### Region Table
| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| region | id | Integer | PK |
| | name | Varchar | |
### Location Table

| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| location | id | Integer | PK |
| | name | Varchar | |
| | region_id | Integer | FK -> region.id |
### Type Tables
| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| type | id | Integer | PK |
| | name | Varchar | |
| type_efficacy | attacking_type_id | Integer | PK, FK -> type.id |
| | defending_type_id | Integer | PK, FK -> type.id |
| | damage_multiplier | Decimal | |
### Ability Table
| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| ability | id | Integer | PK |
| | name | Varchar | |
| | effect | Text | |
| | short_effect | Varchar | |
| | flavor_text | Text | |
### Move Table
| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| move | id | Integer | PK |
| | name | Varchar | |
| | power | Integer | |
| | accuracy | Integer | |
| | pp | Integer | |
| | type_id | Integer | FK -> type.id |
| | effect_chance | Integer | |
| | damage_class | Varchar | |
| | effect | Text | |
| | flavor_text | Text | |
### Pokemon Core Tables
| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| pokemon | pokedex_number | Integer | PK |
| | name | Varchar | |
| | hp | Integer | |
| | attack | Integer | |
| | defense | Integer | |
| | sp_attack | Integer | |
| | sp_defense | Integer | |
| | speed | Integer | |
| | height | Integer | |
| | weight | Integer | |
| | flavor_text | Text | |
### Evolution Tables
| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| pokemon_evolution | evolved_pokedex_number | Integer | PK, FK -> pokemon.pokedex_number |
| | evolved_pokemon_name | Varchar | |
| | base_pokedex_number | Integer | FK -> pokemon.pokedex_number |
| | min_level | Integer | |
| | item_required | Varchar | |
| | time_of_day | Varchar | |
| | trade_required | Boolean | |
### Pokemon Mapping Tables
| Table | Column | Data Type | Constraints / Keys |
|---|---|---|---|
| pokemon_type | pokedex_number | Integer | PK, FK -> pokemon.pokedex_number |
| | type_id | Integer | PK, FK -> type.id |
| | slot | Integer | |
| pokemon_ability | pokedex_number | Integer | PK, FK -> pokemon.pokedex_number |
| | ability_id | Integer | PK, FK -> ability.id |
| | is_hidden | Boolean | |
| | slot | Integer | |
| pokemon_move | pokedex_number | Integer | PK, FK -> pokemon.pokedex_number |
| | move_id | Integer | PK, FK -> move.id |
| | learn_method | Varchar | PK |
| | level_learned_at | Integer | |
| pokemon_location | pokedex_number | Integer | PK, FK -> pokemon.pokedex_number |
| | location_id | Integer | PK, FK -> location.id |
