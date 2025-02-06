


ds = {"id":703,"aquarium_name":"Berlinese","sensor_type":"DS18B20","data_temp":23.12,"date":"2025-02-06 18:50:40"}

dht = {"id":701,"aquarium_name":"Berlinese","sensor_type":"DHT","data_temp":17.2,"data_hum":54.73,"date":"2025-02-06 18:51:26"}



print(ds["aquarium_name"])

if ds["aquarium_name"] == "Berlinese":
    print("esatto")