import requests
import json

# Define constants
BASE_URL = "https://api.ciscospark.com/v1"
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_NOT_FOUND = 404
API_ROOMS = "/rooms"
API_MESSAGES = "/messages"

def test_connection(headers):
    response = requests.get(f"{BASE_URL}/people/me", headers=headers)
    if response.status_code == 200:
        print("Connection to Webex server successful.")
    else:
        print("Connection to Webex server failed.")
    input("Press Enter to return.")

def display_user_info(headers):
    response = requests.get(f"{BASE_URL}/people/me", headers=headers)
    if response.status_code == 200:
        user_info = json.loads(response.text)
        print("User Information:")
        print(f"Display Name: {user_info['displayName']}")
        print(f"Nickname: {user_info['nickName']}")
        print("Emails:")
        for email in user_info['emails']:
            print(email)
    input("Press Enter to return.")

def list_rooms(headers):
    response = requests.get(f"{BASE_URL}/rooms", headers=headers)
    if response.status_code == 200:
        rooms = json.loads(response.text)
        print("List of Rooms:")
        for room in rooms['items'][:5]:
            print(f"Room ID: {room['id']}")
            print(f"Room Title: {room['title']}")
            print(f"Create Date: {room['created']}")
            print(f"Recent Activity: {room['lastActivity']}")
            print()
    input("Press Enter to return.")

def create_room(headers):
    room_title = input("Please Enter Room Name: ")
    room_data = {
        "title": room_title
    }
    response = requests.post(f"{BASE_URL}/rooms", headers=headers, json=room_data)
    if response.status_code == 200:
        print("Room created successfully.")
    else:
        print("Failed to create a room.")
    input("Press Enter to return.")

def send_message(headers):
    response = requests.get(f"{BASE_URL}/rooms", headers=headers)
    if response.status_code == 200:
        rooms = json.loads(response.text)
        print("Select a room to send a message:")
        for i, room in enumerate(rooms['items'][:5]):
            print(f"{i}. {room['title']}")

        room_index = int(input("Enter the room ID: "))
        if 0 <= room_index < 5:
            room_id = rooms['items'][room_index]['id']
            message = input("Enter the message: ")
            message_data = {"roomId": room_id, "text": message}
            response = requests.post(f"{BASE_URL}/messages", headers=headers, json=message_data)
            if response.status_code == 200:
                print("Message sent successfully.")
            else:
                print("Failed to send the message.")
    input("Press Enter to return.")

def main():
    access_token = input("Please enter your Webex access token: ")
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    while True:
        print("Webex TroubleShooting center:")
        print("0. Test Connection with Webex")
        print("1. Display User all Information")
        print("2. All Room information")
        print("3. Create a Room")
        print("4. Send Message to a Room")
        print("5. Exit")
    
        option = input("Please select an option: ")
    
        if option == "0":
            test_connection(headers)
        elif option == "1":
            display_user_info(headers)
        elif option == "2":
            list_rooms(headers)
        elif option == "3":
            create_room(headers)
        elif option == "4":
            send_message(headers)
        elif option == "5":
            print("See you again next time,have a nice dayy!")
            break
        else:
            print("Failed to pick an option. Please choose the correct option.")

if __name__ == "__main__":
    main()
