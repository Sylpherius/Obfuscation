import os, json, sys, collections, re

def read_json(file):
    output_file_text = sys.argv[2]
    output_file = open(output_file_text, "w")
    sensitive_data = ["Id", "Address", "Zip", "Location", "SSN", "Website", "Company", "DOB", "Email", "WeightKG", "Vehicle"]

    data = json.load(file, object_pairs_hook=collections.OrderedDict)
    for element in data:
        for key in element:
            print_element = element[key]
            print_title = key
            if print_element:
                # Exceptions for keys that need slight modifications to remove PII
                if key == "Name":
                    print_element = element[key].split(" ")[0]
                elif key == "Phone":
                    print_element = element[key].split("-")[0]
                    print_title = "Phone Area Code"
                elif key == "UserName":
                    print_element = element[key][0 :min(3, len(element[key])): 1] + "***"

                if key not in sensitive_data:
                    output_file.write(("{}: " + print_element.encode('utf-8') + "\n").format(print_title.encode('utf-8')))

        output_file.write("\n")


def main():
    path = os.path.abspath(sys.argv[1])
    if os.path.isfile(path):
        with open(path) as f:
            read_json(f)
    else:
        raise Exception("Invalid File\n Parameters: (json_file, output_file)")


if __name__ == '__main__':
    main()
