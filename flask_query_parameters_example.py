
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    # Get query parameters
    query = request.args.get('query')  # Returns the value of 'query' parameter
    limit = request.args.get('limit')  # Returns the value of 'limit' parameter
    
    # Default value if the parameter is not provided
    page = request.args.get('page', default=1, type=int)  # Default is 1, type is int
    
    return f"Query: {query}, Limit: {limit}, Page: {page}"

if __name__ == '__main__':
    app.run(debug=True)
