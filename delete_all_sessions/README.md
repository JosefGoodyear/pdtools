# delete_all_sessions

##### Use this script to delete all user sessions for an account, for all users, or a selection of users.

### Usage

To delete all user sessions:

`./delete_all_sessions -k {API KEY} -a`

To delete user sessions from a csv file of login emails:

`./delete_all_sessions -k {API KEY} -f path_to_file.csv`

The csv file should contain login emails like this:

```
user1@example.com
user2@example.com
```
