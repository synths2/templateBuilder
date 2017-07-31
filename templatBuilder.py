## ---------------------------------------------------------------------------
## Builds configuration files from a template and a CSV of values
## DEL - 2017-07-26
## ---------------------------------------------------------------------------

from __future__ import print_function
import jinja2
import csv
import sys
import os.path
from templateConfig import CONFIGS_DIR, TEMPLATE, DEVICES


## ---------------------------------------------------------------------------
## define a function that will transform the "vlan_name_<n>" and "vlan_id_<n>"
## into a new dictionary called 'vlans'
## ---------------------------------------------------------------------------

def transform_vlan_data(row):
    # the first thing we want to do is remove all fields that start with
    # "vlan_" from the original dictionary.  we only want to keep the
    # fields that do not have a value of "0" as the csv-data uses "0" to
    # indicate a non-used vlan.  The result is a dictionary.

    vlan_fields = {
        field_name: field_value
        for field_name, field_value in row.items()
        if field_name.startswith('vlan_') and row.pop(field_name)
        if field_value != '0'
    }

    # now that we have that field list, we want to map the "vlan_name_<n>"
    # values to the actual "vlan_id_<n>" values.  we want to create a new
    # entry in the original dictionary called 'vlans' to store this new
    # vlan dictionary.  We also need to handle the case when the vlan name
    # has whitespace; so covert spaces to underscoores (_).

    row['vlans'] = {
        vlan_fields[f].replace(' ', '_'): vlan_fields[f.replace('name', 'id')]
        for f in vlan_fields if f.startswith('vlan_name')
    }


## ---------------------------------------------------------------------------
## Creates a jinja2 environment and loads the template specified in the
## templateConfig.py file. To-do: Accept parameters for template name.
## Opens a CSV file in the inventory folder and reads in all the parameters
## before asking the template to render and stores the output in ./configs
## ---------------------------------------------------------------------------

def build_templates(template_file, devices):
    templateLoader = jinja2.FileSystemLoader(searchpath=".")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(template_file)

    f = open(devices, 'rt')
    try:
        reader = csv.DictReader(f)
        for dict_row in reader:
            transform_vlan_data(dict_row)
            outputtext = template.render(dict_row)

            config_filename = CONFIGS_DIR + dict_row['hostName'] + '-config'
            with open(config_filename, 'w') as config_file:
                config_file.write(outputtext)
            print("wrote file: %s" % config_filename)

    finally:
        f.close()


if __name__ == "__main__":
    build_templates(TEMPLATE, DEVICES)
