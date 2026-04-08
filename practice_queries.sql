SELECT name, weight
FROM pokemon
WHERE (name LIKE 'C%' OR name LIKE 'P%')
AND weight > 500;

SELECT name, effect
FROM abilities
WHERE
    (effect LIKE '%burn%'
    OR effect LIKE '%paralyze%'
    OR effect LIKE '%sleep%')
    AND effect NOT LIKE '%poison%';

SELECT
    p_base.name AS base_pokemon,
    p_evolved.name AS evolved_pokemon
FROM evolutions e
JOIN pokemon p_base ON e.base_pokedex_number = p_base.pokedex_number
JOIN pokemon p_evolved ON e.evolved_pokedex_number = p_evolved.pokedex_number
WHERE (p_base.name LIKE '%saur' OR p_base.name LIKE 'Char%');