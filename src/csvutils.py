import csv


def write_locations(csvfile, drivers, riders):
    with open(csvfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['type', 'x', 'y', 'paired'])
        for d in drivers:
            writer.writerow(['driver', d.x, d.y, d.is_paired])
        for r in riders:
            writer.writerow(['rider', r.x, r.y, r.is_paired])


def write_results(csvfile, results):
    with open(csvfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["customers", "drivers", "maxseconds"])
        writer.writerows(results)
