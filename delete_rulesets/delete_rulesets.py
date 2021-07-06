#!/usr/bin/env python3
import argparse
from pdpyras import APISession

def get_all_rulesets():
    ruleset_ids = []
    for ruleset in session.iter_all('rulesets'):
        if ruleset['type'] != 'default_global':
            ruleset_ids.append(ruleset['id'])
    print(ruleset_ids)
    return ruleset_ids

def delete_rulesets(rulesets):
    for ruleset in rulesets:
        print("deleting ruleset {}".format(ruleset))
        session.rdelete('/rulesets/{}'.format(ruleset))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deletes all rulesets")
    parser.add_argument('-a', '--api-key', required=True, help="REST API key")
    args = parser.parse_args()
    session = APISession(args.api_key)
    ruleset_ids = get_all_rulesets()
    delete_rulesets(ruleset_ids)
