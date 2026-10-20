from pipeline.validator import validate_record
from pipeline.reporter import total_sales, top_branch, tier_breakdown
from pipeline.transformer import active_transactions, taxed_revenues
raw_data = [
    {
        "branch_id": "B001",
        "date": "2026-10-01",
        "customer_tier": "Gold",
        "items": 5,
        "revenue": 300
    },
    {
    "branch_id": "B002",
    "date": "2026-10-02",
    "customer_tier": "Silver",
    "items": 3,
    "revenue": 150
    }
]

clean_records = []

for record in raw_data:

    validated = validate_record(record)

    if validated:
        clean_records.append(validated)

for record in clean_records:
    print(record)
print("Total Sales:", total_sales(clean_records)) 
print("Top Branch:", top_branch(clean_records))
print("Customer Tiers:", tier_breakdown(clean_records)) 
active = active_transactions(clean_records)

print("Active Transactions:", len(active))

print("Taxed Revenues:", taxed_revenues(clean_records))  

