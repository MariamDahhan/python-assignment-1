from pipeline.schema import TransactionRecord


def validate_record(record):

    if record["branch_id"] == "":
        return None

    if record["revenue"] < 0:
        return None

    if record["items"] < 0:
        return None

    try:
        return TransactionRecord(
            record["branch_id"],
            record["date"],
            record["customer_tier"],
            int(record["items"]),
            float(record["revenue"])
        )

    except ValueError:
        return None