import operator
year_sales = {
    "c1": 1000,
    "c2": 505,
    "c3":1999
}

popular_year, popluar_year_sales = sorted(year_sales.items(),key=operator.itemgetter(1),reverse=True)[0];
summary = [
    "The most popular year was {}, wtih {} sales".format(popular_year,popluar_year_sales)
]


print(summary[0])
