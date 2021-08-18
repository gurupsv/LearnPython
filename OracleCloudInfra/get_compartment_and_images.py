import sys
import argparse
import datetime
import oci
import json
import os


##########################################################################
# check service error to warn instead of error
##########################################################################
def check_service_error(code):
    return ('max retries exceeded' in str(code).lower() or
            'auth' in str(code).lower() or
            'notfound' in str(code).lower() or
            code == 'Forbidden' or
            code == 'TooManyRequests' or
            code == 'IncorrectState' or
            code == 'LimitExceeded'
            )


def create_signer(config_profile):
    config = oci.config.from_file(
        oci.config.DEFAULT_LOCATION,
        (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
    )
    signer = oci.signer.Signer(
        tenancy=config["tenancy"],
        user=config["user"],
        fingerprint=config["fingerprint"],
        private_key_file_location=config.get("key_file"),
        pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
        private_key_content=config.get("key_content")
    )
    return config, signer


##########################################################################
# Load compartments
##########################################################################
def identity_read_compartments(identity, tenancy):
    print("Loading Compartments...")
    try:
        compartments = oci.pagination.list_call_get_all_results(
            identity.list_compartments,
            tenancy.id,
            compartment_id_in_subtree=True
        ).data

        # Add root compartment which is not part of the list_compartments
        compartments.append(tenancy)

        print("    Total " + str(len(compartments)) + " compartments loaded.")
        return compartments

    except Exception as e:
        raise RuntimeError("Error in identity_read_compartments: " + str(e.args))


##########################################################################
# Main
##########################################################################

# Get Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument('-t', default="", dest='config_profile', help='Config file section to use (tenancy profile)')
parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
cmd = parser.parse_args()

# Start print time info
start_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Running List Virtual Circuits")
print("Written By Guruprasad Shringeri Vidyaranyapura, July 2021")
print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# Identity extract compartments
config, signer = create_signer(cmd.config_profile)
compartments = []
tenancy = None
try:
    print("\nConnecting to Identity Service...")
    identity = oci.identity.IdentityClient(config, signer=signer)
    if cmd.proxy:
        identity.base_client.session.proxies = {'https': cmd.proxy}

    tenancy = identity.get_tenancy(config["tenancy"]).data
    regions = identity.list_region_subscriptions(tenancy.id).data
    compute = oci.core.ComputeClient(config, signer=signer)

    print("Tenant Name : " + str(tenancy.name))
    print("Tenant Id   : " + tenancy.id)
    print("")

    compartments = identity_read_compartments(identity, tenancy)
    computes = compute.list_images(tenancy.id)
except Exception as e:
    raise RuntimeError("\nError extracting compartments section - " + str(e))

print("===========================================================")
for compartment in compartments:
    print(str("Compartment  -> " + compartment.name))

print("===========================================================")

print("===========================================================")
temp=json.loads(str(computes.data))

for something in temp:
    if something['operating_system'] == 'Oracle Linux':
        print(something['operating_system']+"----"+something['display_name'])
print("===========================================================")

print("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
