import sys
import json
import xmltodict
if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]
    print("Converting from: ", infile, " to:", outfile)
    with open(infile) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

    json_data = json.dumps(data_dict)
    with open(outfile, "w") as json_file:
        json_file.write(json_data)