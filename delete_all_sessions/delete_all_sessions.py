#!/usr/bin/env python
import argparse
import csv
from pdpyras import APISession


def get_users_from_file(f):
    user_emails = []
    with open(f) as csvfile:
        email_reader = csv.reader(csvfile)
        for row in email_reader:
            user_emails.append(row[0])
    return user_emails 


def add_users_from_file(user_emails):
    users = session.dict_all('users', by='email')
    user_ids = []
    for user_email in user_emails:
        if user_email in users:
            user_ids.append(users[user_email]['id'])
        else:
            print("No user was found with login email: {}. Their sessions will not be deleted.".format(user_email))
    return user_ids


def add_all_users():
    user_ids = []
    for user in session.iter_all('users'):    
        user_ids.append(user['id'])
    return user_ids


def delete_user_sessions(user_ids):
    user_sessions = []
    for user_id in user_ids:
        print("deleting all sessions for user {} . . .".format(user_id))
        session.rdelete('/users/{}/sessions'.format(user_id))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Deletes all user sessions for all users on an account")
    parser.add_argument('-a', '--api-key', required=True, help="REST API key")
    parser.add_argument('-f', '--file', required=False, help="File containing user login emails")
    args = parser.parse_args()
    session = APISession(args.api_key)
    if args.file:
        user_emails = get_users_from_file(args.file)
        user_ids = add_users_from_file(user_emails)
    else:
        user_ids = add_all_users()
    delete_user_sessions(user_ids)