import pandas as pd
import matplotlib.pyplot as plt
import os
from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.models.resource import Resource
from datetime import datetime
import calendar

# Create a folder to store the generated charts
REPORT_DIR = "/app/reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def generate_monthly_report(db: Session, month: int, year: int):
    """
    Generates a bar chart for bookings by type and a line chart for revenue.
    """
    # 1. Fetch bookings for the given month
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year + 1, 1, 1)
    else:
        end_date = datetime(year, month + 1, 1)

    bookings = db.query(Booking).filter(
        Booking.start_time >= start_date,
        Booking.start_time < end_date
    ).all()

    if not bookings:
        return f"No bookings found for {calendar.month_name[month]} {year}."

    # 2. Process data with Pandas
    data = []
    for b in bookings:
        resource = db.query(Resource).filter(Resource.id == b.resource_id).first()
        data.append({
            "date": b.start_time.date(),
            "resource_type": resource.type if resource else "Unknown",
            "revenue": b.total_price
        })

    df = pd.DataFrame(data)

    # 3. Create the Charts
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(f'VenueBot AI - Monthly Report for {calendar.month_name[month]} {year}', fontsize=16, fontweight='bold')

    # Chart 1: Bookings by Resource Type (Bar Chart)
    type_counts = df['resource_type'].value_counts()
    axes[0].bar(type_counts.index, type_counts.values, color=['#FFB300', '#81C784', '#3E2723'])
    axes[0].set_title('Number of Bookings by Type')
    axes[0].set_ylabel('Total Bookings')
    axes[0].set_xlabel('Resource Type')

    # Chart 2: Revenue over time (Line Chart)
    daily_revenue = df.groupby('date')['revenue'].sum()
    axes[1].plot(daily_revenue.index, daily_revenue.values, marker='o', color='#FFB300', linewidth=2)
    axes[1].set_title('Daily Revenue')
    axes[1].set_ylabel('Revenue ($)')
    axes[1].set_xlabel('Date')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    
    # Save the chart
    file_path = f"{REPORT_DIR}/report_{year}_{month}.png"
    plt.savefig(file_path)
    plt.close()

    return file_path