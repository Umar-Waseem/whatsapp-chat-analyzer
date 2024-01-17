import argparse
import os
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Path to the chat data file")
parser.add_argument("top_users", type=int, help="Number of top users to display")
args = parser.parse_args()

filepath = args.filename
with open(filepath, "r") as file:
    chat_data = file.readlines()

# number of messages from each user
user_messages = {}
for line in chat_data:
    if "- " in line:
        user = line.split("- ")[1].split(":")[0].strip()
        if user in user_messages:
            user_messages[user] += 1
        else:
            user_messages[user] = 1

# top users
top_users = sorted(user_messages.items(), key=lambda x: x[1], reverse=True)[:args.top_users]
users = [user[0] for user in top_users]
message_counts = [user[1] for user in top_users]

filename = os.path.splitext(args.filename)[0]  # Remove .txt extension from file path
# bottom margin
plt.subplots_adjust(bottom=0.22)

plt.bar(users, message_counts)

plt.xlabel("Users")
plt.ylabel("Message Counts")

plt.title(f"Top {args.top_users} Most Active Users for {filename}")
plt.xticks(rotation=90)  # rotate x labels vertically

for i, count in enumerate(message_counts):
    plt.text(i, count, str(count), ha='center', va='bottom') # values on top of bars
plt.show()
