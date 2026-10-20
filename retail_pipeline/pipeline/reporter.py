def total_sales(records):

    total = 0

    for record in records:
        total += record.revenue

    return total


def top_branch(records):

    branch_sales = {}

    for record in records:

        branch = record.branch_id

        if branch not in branch_sales:
            branch_sales[branch] = 0

        branch_sales[branch] += record.revenue

    return max(branch_sales, key=branch_sales.get)


def tier_breakdown(records):

    tiers = {}

    for record in records:

        tier = record.customer_tier

        if tier in tiers:
            tiers[tier] += 1
        else:
            tiers[tier] = 1

    return tiers