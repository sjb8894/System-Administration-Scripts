# Script 2 for NSSA 221

import os
import pwd


# reads file and creates instance of class user
def readFile():
    with open('Lab02_Users.csv', 'r') as file:
        line = file.readline()
        usernames = []
        for line in file:
            user = line.strip().split(",")
            user.remove("")
            user.pop(0)
            for string in user:
                if string == "":
                    user.remove(string)

            # if len(user) != 6:
            #     print("Missing user information!")
            else:
                firstName = user[1]
                lastName = user[0]
                group = user[4]
                username = create_username(firstName, lastName, usernames)
                print(username)
                # add_to_group(group)
                # add_user(group, firstName, lastName, username)


# checks if username is avialble under pwd module, returns valid username
def create_username(firstName, lastName, usernames):
    for element in lastName:
        if element == "'":
            lastName = lastName.replace(element, '')

    firstName = firstName.lower()
    lastName = lastName.lower()

    username = firstName[0] + lastName
    for x in usernames:
        if x == username:
            username = username + str(1)
            usernames.append(username)
            return username
    usernames.append(username)
    return username


# adds to group
def add_to_group(group):
    os.system("groupadd -f " + group)


# gets shell based on group
def get_shell(group):
    if group == "ceo":
        shell = "/bin/csh"
    else:
        shell = "/bin/bash"
    return shell


# adds user
def add_user(group, firstName, lastName, username):
    # print("useradd -m -d /home/" + group + "/" + username + " -s " + shell + " -g " + group)
    os.system("useradd -m -d /home/" + group + "/" + username + " -s " + get_shell(
        group) + " -g " + group + " -p " + username[::1] + " -c \"" + firstName + " " + lastName + "\" " + username)
    password_func(username)


def password_func(username):
    # create pw cmd
    os.system("passwd --stdin " + username)

    # prompt for pw change
    os.system("passwd -e " + username)


if __name__ == '__main__':
    readFile()
