import psycopg2

def search():
    conn = psycopg2.connect(dbname="pokemon", user="postgres", host="localhost")
    cursor = conn.cursor()

    user_input = input("Enter Pokemon name: ")

    # SELECT pokedex_number, name FROM demo_pokemon WHERE name = 'Pikachu' OR '1'='1';
    query = f"SELECT pokedex_number, name FROM demo_pokemon WHERE name = '%s';"

    print(f"\nExecuting Query: {query}\n")

    try:
        cursor.execute(query, (user_input,))
        results = cursor.fetchall()
        for row in results:
            print(row)
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    search()


"""
Tables
------
abilities
evolutions
locations
moves
pokemon
pokemon_ability
pokemon_location
pokemon_move
pokemon_type
regions
type_effectiveness
types
"""
