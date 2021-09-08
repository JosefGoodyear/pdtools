# Convert Incident Numbers to ids

Given a csv of PagerDuty incident numbers, get the incident IDs for those numbers
and add them to a new csv (prepended by "ids_" ).


### Usage
`python3 convert_incident_numbers_to_ids.py -k {api-key} -f {csv-file} -c {column}`

Column is an optional parameter denoting the column in the original csv where the
incident numbers are found. By default, this value is 0.
