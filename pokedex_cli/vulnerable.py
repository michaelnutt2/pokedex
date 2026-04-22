import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="pokemon_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

def search_pokemon():
    conn = get_connection()
    cursor = conn.cursor()

    user_input = input("Enter Pokemon name to search: ")

    query = f"SELECT pokedex_number, name, hp FROM pokemon WHERE name = '{user_input}';"

    print(f"\n[DEBUG] Executing Query: {query}\n")

    cursor.execute(query)
    results = cursor.fetchall()

    if not results:
        print("No Pokemon found.")
    else:
        print(f"{'ID':<5} | {'Name':<15} | {'HP':<5}")
        print("-" * 30)
        for row in results:
            print(f"{row[0]:<5} | {row[1]:<15} | {row[2]:<5}")

    conn.close()

def add_pokemon():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n--- Register New Pokemon ---")
    p_id = input("Enter Pokedex Number: ")
    p_name = input("Enter Pokemon Name: ")
    p_hp = input("Enter Base HP: ")
    type_id = input("Enter Primary Type ID (1-18): ")

    query_insert_pokemon = f"INSERT INTO pokemon (pokedex_number, name, hp) VALUES ({p_id}, '{p_name}', {p_hp});"
    query_insert_type = f"INSERT INTO pokemon_type (pokedex_number, type_id, slot) VALUES ({p_id}, {type_id}, 1);"

    print(f"\n[DEBUG] Executing: {query_insert_pokemon}")
    cursor.execute(query_insert_pokemon)

    print(f"[DEBUG] Executing: {query_insert_type}")
    cursor.execute(query_insert_type)

    conn.commit()
    print("\nSuccess: Pokemon successfully added!")

    conn.close()

def main():
    while True:
        print("\n=== Pokedex OS v1.0 (VULNERABLE) ===")
        print("1. Search Pokemon")
        print("2. Add Pokemon")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            search_pokemon()
        elif choice == '2':
            add_pokemon()
        elif choice == '3':
            print("Shutting down...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()