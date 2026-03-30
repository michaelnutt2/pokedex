SELECT name, weight
FROM pokemon
WHERE (name LIKE 'C%' OR name LIKE 'P%')
AND weight > 500;

-- Find abilities related to specific status effects. Return
-- the name and effect of abilities where the effect
-- contains the words 'burn', 'paralyze', or 'sleep', but also
-- exclude any that include 'poison'

SELECT name, effect
FROM abilities
WHERE
    (effect LIKE '%burn%'
    OR effect LIKE '%paralyze%'
    OR effect LIKE '%sleep%')
    AND effect NOT LIKE '%poison%';

-- Find pokemon evolutionary lines that maintain a convention
-- find base Pokemon whose names end in 'saur' or begin with
-- 'char' and join to the evolutions table to display
-- the base Pokemon and evolved pokemon names.
EXPLAIN ANALYZE SELECT
    p_base.name AS base_pokemon,
    p_evolved.name AS evolved_pokemon
FROM evolutions e
JOIN pokemon p_base ON e.base_pokedex_number = p_base.pokedex_number
JOIN pokemon p_evolved ON e.evolved_pokedex_number = p_evolved.pokedex_number
WHERE (p_base.name LIKE '%saur' OR p_base.name LIKE 'Char%');