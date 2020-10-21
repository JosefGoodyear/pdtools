#!/usr/bin/env python3
import argparse
from pdpyras import APISession

def delete_user_sessions():
	user_ids = []
	user_sessions = []
	for user in session.iter_all('users'):
    	 user_ids.append(user['id'])
	for user_id in user_ids:
		print("deleting all sessions for user {} . . .".format(user_id))
		session.rdelete('/users/{}/sessions'.format(user_id))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deletes all user sessions for all users on an account")
    parser.add_argument('-a', '--api-key', required=True, help="REST API key")
    args = parser.parse_args()
    session = APISession(args.api_key)
    delete_user_sessions()
