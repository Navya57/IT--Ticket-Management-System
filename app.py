from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ticket_system"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def home():

    cursor.execute("SELECT * FROM ticket")
    tickets = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM ticket")
    total_tickets = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ticket WHERE status='Open'")
    open_tickets = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ticket WHERE status='Resolved'")
    resolved_tickets = cursor.fetchone()[0]

    return render_template(
        'index.html',
        tickets=tickets,
        total_tickets=total_tickets,
        open_tickets=open_tickets,
        resolved_tickets=resolved_tickets
    )
@app.route('/search')
def search():

    search_text = request.args.get('search')

    query = """
    SELECT * FROM ticket
    WHERE issue_title LIKE %s
    """

    cursor.execute(
        query,
        ('%' + search_text + '%',)
    )

    tickets = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM ticket")
    total_tickets = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ticket WHERE status='Open'")
    open_tickets = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ticket WHERE status='Resolved'")
    resolved_tickets = cursor.fetchone()[0]

    return render_template(
        'index.html',
        tickets=tickets,
        total_tickets=total_tickets,
        open_tickets=open_tickets,
        resolved_tickets=resolved_tickets
    )

# Create Ticket
@app.route('/create_ticket', methods=['POST'])
def create_ticket():

    issue_title = request.form['issue_title']
    description = request.form['description']
    priority = request.form['priority']

    query = """
    INSERT INTO ticket
    (issue_title, description, priority, status)
    VALUES (%s,%s,%s,%s)
    """

    values = (
        issue_title,
        description,
        priority,
        "Open"
    )

    cursor.execute(query, values)
    db.commit()

    return redirect('/')


# Update Status
@app.route('/update_status/<int:ticket_id>')
def update_status(ticket_id):

    query = """
    UPDATE ticket
    SET status='Resolved'
    WHERE ticket_id=%s
    """

    cursor.execute(query, (ticket_id,))
    db.commit()

    return redirect('/')


# Delete Ticket
@app.route('/delete_ticket/<int:ticket_id>')
def delete_ticket(ticket_id):

    query = """
    DELETE FROM ticket
    WHERE ticket_id=%s
    """

    cursor.execute(query, (ticket_id,))
    db.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)