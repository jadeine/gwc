import school_scores
list_of_scores = school_scores.get_all()

# state name and year
for row in list_of_scores:
    print(row["State"]["Name"], row["Year"])

# total test-takers
for row in list_of_scores:
    print(row["Total"]["Test-takers"])
