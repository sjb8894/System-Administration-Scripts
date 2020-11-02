# Sam Benoist
# NSSA 221 - Script 3


# import
import os
import subprocess
import os.path
from os import path


def get_file():
    fileName = raw_input("Origin File Name: ")
    return fileName

# Check if user directory is Desktop
def check_dir():
    currentDir = os.getcwd()
    print("Your current directory is: " + currentDir)
    if currentDir == "/home/student/Desktop":
        print("You are in the Desktop directory\n")
    else:
        print("You are not in the Desktop directory\n")


# Create Symbolic Link
def create_link(fileName):
    fileShortcut = raw_input("Enter Shortcut for file: ")
    os.system("ln -s " + str(fileName) + " " + str(fileShortcut))


# Prints Report Summary
def report_summary():
    numOfLinks = subprocess.Popen(["find . -type l -ls | wc -l"], stdout=subprocess.PIPE, shell=True)
    (result, errorMsg) = numOfLinks.communicate()
    numOfLinks = result;

    linkSummary = subprocess.Popen(["find . -type l -ls"], stdout=subprocess.PIPE, shell=True)
    (result, errMsg) = linkSummary.communicate()
    linkSummary = result;
    print("Number of existing Symbolic Links:" + "\n" + str(numOfLinks))
    print("Symbolic Links Summary Report: " + "\n" + str(linkSummary))


if __name__ == '__main__':
    check_dir()
    fn = get_file()
    create_link(fn)
    report_summary()
