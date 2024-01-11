import configparser
import os
import argparse

def parse_config(file_path, selected_section=None, selected_key=None):
    config = configparser.ConfigParser()
    config.read(file_path)

    if selected_key:
        print(f"All Sections and Key-Value Pairs for Key '{selected_key}':")
        for section in config.sections():
            if config.has_option(section, selected_key):
                value = config.get(section, selected_key)
                print(f"\n[{section}] {selected_key}={value}")

    elif selected_section is None:
        print("\nAvailable Sections:")
        for section in config.sections():
            print(f"- {section}")

    selected_section = input("\nEnter the section you want to print (or press Enter to exit): ")

    if not selected_section:
        print("Exiting.")
        return

    if config.has_section(selected_section):
        #if not selected_key:
            print(f"\n[{selected_section}]")
            for key, value in config.items(selected_section):
                print(f"{key}={value}")
        #else:
        #    if config.has_option(selected_section, selected_key):
        #        value = config.get(selected_section, selected_key)
         #       print(f"\n[{selected_section}] {selected_key}={value}")
         #   else:
          #      print(f"Key '{selected_key}' not found in section '{selected_section}'.")
    else:
        print(f"Section '{selected_section}' not found.")

if __name__ == "__main__":
    home_dir = os.environ.get("HOME")
    file_path = os.path.join(home_dir, ".oci/config")

    if os.path.isfile(file_path):
        parser = argparse.ArgumentParser(description="Parse and print sections from config file")
        parser.add_argument("--section", help="Specify the section to print")
        parser.add_argument("--key", help="Specify the key to print within the section")

        args = parser.parse_args()
        selected_section = args.section
        selected_key = args.key

        parse_config(file_path, selected_section, selected_key)
    else:
        print(f"Config file not found: {file_path}")
