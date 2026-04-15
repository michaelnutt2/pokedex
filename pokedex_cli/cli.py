# pip install psycopg2-binary

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="pokemon",
        user="postgres",
        host="localhost",
        port="5432"
    )

def main_menu():
    # Loop forever to give the user a menu
    while True:
        print("Pokemon Database")
        print("1. Search for Pokemon by name")
        print("2. Register a new pokemon")
        print("3. View a region report")
        print("4. Exit")

        choice = input("Select an option:")

        if choice == '1':
            search_pokemon()
        elif choice == '2':
            register_pokemon()
        elif choice == '3':
            view_region_report()
        elif choice == '4':
            return
        else:
            print("Invalid selection.")

def search_pokemon():
    search_term = input("Enter Pokemon name to search: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT p.pokedex_number, p.name, t.name
        FROM pokemon p
        JOIN pokemon_type pt ON p.pokedex_number = pt.pokedex_number
        JOIN types t ON pt.type_id = t.id
        WHERE p.name ILIKE %s
        """

        cursor.execute(query, ('%' + search_term + '%',)) #; '
        results = cursor.fetchall()

        print(f"\n{'ID':<5} | {'Name':<15} | {'Type':<10}")

        if not results:
            print("No Pokemon found")
        else:
            for row in results:
                print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<10}")
        print("")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def list_types():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM types ORDER BY id"
        )

        print(f"{'ID':<5} | {'Type':<15}")
        for type in cursor.fetchall():
            print(f"{type[0]} | {type[1]}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def register_pokemon():
    print("Register New Pokemon")
    p_id = input("Enter new Pokedex Number: ")
    p_name = input("Enter new Pokemon name: ")
    p_hp = input("Enter Base HP: ")

    print("Types:")
    list_types()
    type_1_id = input("Enter Primary Type ID: ")
    type_2_id = input("Enter Secondary Type ID (or leave blank): ")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Insert pokemon
        cursor.execute(
            "INSERT INTO pokemon (pokedex_number, name, hp) VALUES (%s, %s, %s)",
            (p_id, p_name, p_hp)
        )

        # Insert the primary type
        cursor.execute(
            "INSERT INTO pokemon_type (pokedex_number, type_id, slot) VALUES (%s, %s, 1)",
            (p_id, type_1_id)
        )

        if type_2_id.strip():
            cursor.execute(
                "INSERT INTO pokemon_type (pokedex_number, type_id, slot) VALUES (%s, %s, 2)",
                (p_id, type_2_id)
            )

        conn.commit()
        print("Pokemon registered.")

    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print(f"Error: A Pokemon with Pokedex Number {p_id} already exists.")

    except psycopg2.errors.ForeignKeyViolation:
        conn.rollback()
        print("Error: Invalid Type ID provided. ")

    except psycopg2.Error as e:
        conn.rollback()
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def view_region_report():
    print("Region Population Report")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT
                r.name AS region_name,
                COUNT(DISTINCT l.id) AS total_locations,
                COUNT(pl.pokedex_number) AS total_pop
            FROM regions r
            JOIN locations l ON r.id = l.region_id
            JOIN pokemon_location pl ON l.id = pl.location_id
            GROUP BY r.name
            ORDER BY total_pop DESC
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print(f"{'Region':<15} | {'Locations':<10} | {'Total Population':<20}")
        print("-"*51)

        if not results:
            print("No region data found")
        else:
            for row in results:
                print(f"{row[0]:<15} | {row[1]:<10} | {row[2]:<20}")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    main_menu()
