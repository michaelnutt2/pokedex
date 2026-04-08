SELECT * FROM pokemon WHERE name = 'Teddiursa';

EXPLAIN SELECT * FROM pokemon WHERE name = 'Teddiursa';

EXPLAIN SELECT * FROM pokemon WHERE pokedex_number = 216;

CREATE INDEX idx_pokemon_name ON pokemon(name);

-- CREATE INDEX idx_is_hidden ON pokemon_ability(is_hidden);

-- SELECT COUNT(*) FROM pokemon_ability WHERE is_hidden = true;

-- JOIN pokemon_ability pa ON p.pokedex_number = pa.pokedex_number