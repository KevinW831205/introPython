import csv

hosts = [["workstation.local", "0.0.0.0"], ["webserver.cloud", "0.0.0.1"]]
with open('hosts.csv', "w", newline='') as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)

with open('hosts.csv') as host_csv:
    hostdata = csv.reader(host_csv)
    for row in hostdata:
        name, ip = row
        print("name: {}, ip: {}".format(name,ip))


keys = ["col1","col2"];
values = [{"col1":"abc", "col2":"def"},{"col1":"123", "col2":"456"}]
with open('dict.csv',"w",newline='') as dict_csv:
    writer = csv.DictWriter(dict_csv,fieldnames=keys)
    writer.writeheader()
    writer.writerows(values)

with open('dict.csv') as dict_csv:
    reader = csv.DictReader(dict_csv)
    for row in reader:
        print(row)
        print("col1: {} col2: {}".format(row["col1"],row["col2"]))

