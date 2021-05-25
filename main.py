from parsers import FlagsParser, IpsParser
from factories import ServicesInvoker
from writer import ResponseWriter

# All the project prints can be converted to logs for a more complex project.

# Parse the flags from command line
flags_parser = FlagsParser()
flags_parser.add_arguments()
args = flags_parser.parse_args()

# Parse the list of ips from the unstructured text file.
ip_list = IpsParser.from_txt_file(args.txt_file)

# Call service(s)
service_switch = ServicesInvoker(ip_list=ip_list)
response = service_switch.call_services(args.services)

# Call writer to save json file. I am assuming we just need the json format so we are not worrying about
# class representation for the retrieved data
writer = ResponseWriter(response)
writer.save_services_to_json()
