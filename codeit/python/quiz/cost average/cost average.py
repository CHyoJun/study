with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0

    for line in f:
        data = line.strip().split(":")
        revenue = int(data[1])
        print(revenue)

        total_revenue += revenue
        total_days += 1
    print(total_revenue / total_days)