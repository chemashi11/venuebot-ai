import random
from datetime import datetime, timedelta
from app.core.database import SessionLocal
from app.models.booking import Booking
from app.models.user import User
from app.models.resource import Resource

db = SessionLocal()

def seed_data():
    print("Seeding historical data...")
    
    # Get a customer and resources
    customer = db.query(User).filter(User.role == "customer").first()
    resources = db.query(Resource).all()

    if not customer or not resources:
        print("Error: You need at least one customer and some resources in the DB first.")
        return

    # Generate 6 months of data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)

    current_date = start_date
    while current_date < end_date:
        # Randomly generate 1-5 bookings per day
        for _ in range(random.randint(1, 5)):
            res = random.choice(resources)
            
            # Random time between 9 AM and 8 PM
            booking_time = current_date.replace(hour=random.randint(9, 20), minute=0, second=0)
            
            booking = Booking(
                customer_id=customer.id,
                resource_id=res.id,
                start_time=booking_time,
                end_time=booking_time + timedelta(hours=2),
                status="confirmed",
                total_price=res.base_price_per_hour * 2
            )
            db.add(booking)
        
        current_date += timedelta(days=1)
    
    db.commit()
    print("Successfully generated 6 months of fake booking data!")

if __name__ == "__main__":
    seed_data()