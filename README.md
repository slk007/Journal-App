Personal Journal App

Create a terminal application to store personal journal log with user management, to be run locally
and not on cloud. For simplicity consider you could enter only textual content in journal data.

Terminologies
User​ : An independent entity with access to its own journal. Data should not be shared between
users.
Journal​ : A text log containing multiple entries.

Journal Entry​ : A piece for text accompanied by a timestamp

Features required
1. User Management:​ On starting the application the user should be presented with either
Login or Sign Up options. On Sign Up Do not ask for a password again

2. Journal Management:​ After authentication, the user should be presented with two
options to either list all his previous entries or create a new entry. Maximum 50 Journal
entries should be allowed per user. Newer entry after 50 should replace the oldest
entry(like a queue).

3. While showing previous entries each entry should be preceded by time in readable
format and data followed by the text input
Eg.
25 Jun 2019 10.30pm - Some text that the user entered
23 Jun 2019 10.00am - Some text that user entered

The application should run locally on a terminal and store data on files locally but not in any
database (hosted locally including authentication data). The application should support multiple
account creation up to 10 accounts.

Tech Specifications
1. The app should run in terminal. No GUI can be used. The application should only be
able to take input via keyboard
2. User should not be able to read journals written by the software by looking at the files
through explorers or any other software
3. Do not use database for storing data, use files to store all your user data
4. Build your code in Go, python or PHP
