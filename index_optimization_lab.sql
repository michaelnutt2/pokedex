-- Query 1
EXPLAIN SELECT p.name, a.name AS ability_name, l.name AS location_name
FROM pokemon p
JOIN pokemon_ability pa ON p.pokedex_number = pa.pokedex_number
JOIN abilities a ON pa.ability_id = a.id
JOIN pokemon_location pl ON p.pokedex_number = pl.pokedex_number
JOIN locations l ON pl.location_id = l.id
WHERE p.hp > 100;

EXPLAIN SELECT r.name, COUNT(pl.pokedex_number) AS total_pokemon
FROM regions r
JOIN locations l ON r.id = l.region_id
JOIN pokemon_location pl ON l.id = pl.location_id
GROUP BY r.name
HAVING COUNT(pl.pokedex_number) > 200;