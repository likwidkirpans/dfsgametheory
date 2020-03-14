import time
start_time = time.time()

from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter

optimizer = get_optimizer(Site.FANDUEL, Sport.BASKETBALL)
optimizer.load_players_from_csv("fd.csv")

optimizer.set_min_salary_cap(59400)

exporter = CSVLineupExporter(optimizer.optimize(n=1000, randomness=True))
exporter.export('result.csv')

#for lineup in optimizer.optimize(n=150, randomness=True):
    #print("-")

print("--- %s seconds ---" % (time.time() - start_time))
