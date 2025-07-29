# src/logic/performance_reviewer.py
from src.database.db_connections import get_mongo_collection

def submit_performance_review(employee_id, review_date, reviewer_name, rating, comments, strengths=None, improvements=None):
    """
    Submits a performance review document to the MongoDB 'reviews' collection.
    The flexibility of NoSQL allows us to easily handle optional fields.
    """
    reviews_collection = get_mongo_collection()
    # CORRECTED LINE: Check for None explicitly
    if reviews_collection is None:
        print("Could not connect to the reviews collection.")
        return None
        
    review_document = {
        "employee_id": employee_id,
        "review_date": review_date,
        "reviewer_name": reviewer_name,
        "overall_rating": rating,
        "comments": comments,
    }
    
    # Add optional fields only if they are provided
    if strengths:
        review_document["strengths"] = strengths
    if improvements:
        review_document["areas_for_improvement"] = improvements
        
    result = reviews_collection.insert_one(review_document)
    print(f"Successfully submitted review. Document ID: {result.inserted_id}")
    return result.inserted_id

def get_performance_reviews_for_employee(employee_id):
    """Retrieves all performance reviews for a specific employee."""
    reviews_collection = get_mongo_collection()
    # CORRECTED LINE: Check for None explicitly
    if reviews_collection is None:
        return []
        
    # The find() method returns a cursor-like object with all matching documents.
    reviews = list(reviews_collection.find({"employee_id": employee_id}))
    
    # Convert ObjectId to string for easier use in Python
    for review in reviews:
        review['_id'] = str(review['_id'])
        
    return reviews