def active_transactions(records):

    return list(
        filter(
            lambda record: record.revenue > 0,
            records
        )
    )
def taxed_revenues(records):

    return list(
        map(
            lambda record: record.revenue * 1.13,
            records
        )
    )