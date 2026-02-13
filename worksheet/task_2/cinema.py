import sqlite3

def customer_tickets(conn, customer_id):
    cursor = conn.cursor()
    query = """
    SELECT f.title, s.screen, t.price
    FROM tickets t
    JOIN screenings s ON t.screening_id = s.screening_id
    JOIN films f ON s.film_id = f.film_id
    WHERE t.customer_id = ?
    ORDER BY f.title ASC
    """
    cursor.execute(query, (customer_id,))
    return cursor.fetchall()

def screening_sales(conn):
    cursor = conn.cursor()
    query = """
    SELECT s.screening_id, f.title, COUNT(t.ticket_id)
    FROM screenings s
    JOIN films f ON s.film_id = f.film_id
    LEFT JOIN tickets t ON s.screening_id = t.screening_id
    GROUP BY s.screening_id
    ORDER BY COUNT(t.ticket_id) DESC
    """
    cursor.execute(query)
    return cursor.fetchall()

def top_customers_by_spend(conn, limit):
    cursor = conn.cursor()
    query = """
    SELECT c.customer_name, SUM(t.price)
    FROM customers c
    JOIN tickets t ON c.customer_id = t.customer_id
    GROUP BY c.customer_id
    ORDER BY SUM(t.price) DESC
    LIMIT ?
    """
    cursor.execute(query, (limit,))
    return cursor.fetchall()

    def add_ticket(conn, screening_id, customer_id, price):
    cursor = conn.cursor()
    query = "INSERT INTO tickets (screening_id, customer_id, price) VALUES (?, ?, ?)"
    cursor.execute(query, (screening_id, customer_id, price))
    conn.commit()

    def update_ticket_price(conn, ticket_id, new_price):
    cursor = conn.cursor()
    query = "UPDATE tickets SET price = ? WHERE ticket_id = ?"
    cursor.execute(query, (new_price, ticket_id))
    conn.commit()