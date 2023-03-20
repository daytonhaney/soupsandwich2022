def process_data(data):
    print("Beginningn data process")
    modified_data = data + "this is data"
    return modified_data

def read_data_from_web():
    print("Reading data from the web")
    data = "data from web"
    return data 

def write_data_to_db(data):
    print("writing data")
    print(data)

def get_area(area):
    print("Getting the area of house")
    total_area = area 
    print(area)
    return total_area
def area(l,w):

    area = l * w 
    return area 

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_db(modified_data)
    total_area = get_area(area)
    total_area = area("l","w")
main()



