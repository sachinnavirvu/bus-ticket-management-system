from flask import Flask, render_template, request
app = Flask(__name__)
routes = [
    {"id": 1, "origin": "City A", "destination": "City B", "departure_time": "9:00 AM", "price": 20},
    {"id": 2, "origin": "City B", "destination": "City C", "departure_time": "11:00 AM", "price": 25},
    {"id": 3, "origin": "City A", "destination": "City C", "departure_time": "1:00 PM", "price": 30}
]
@app.route('/')
def home():
    return render_template('index.html', routes=routes)
@app.route('/book_ticket/<int:route_id>', methods=['GET', 'POST'])
def book_ticket(route_id):
    if request.method == 'POST':
        print(request.form)
        return "Ticket booked successfully!"

    route = next((r for r in routes if r['id'] == route_id), None)
    return render_template('book_ticket.html', route=route)

if __name__ == '__main__':
    app.run(debug=True)
