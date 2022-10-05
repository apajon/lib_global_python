import json

# Get the message received by a MQTT client from a topic as json string
# the firstLine contain the name of data keys of the json datas
# Can print the datas in the terminal
# Can save the datas in a log file 'fh'
# 'printLog', 'saveLog', 'firstLine' and 'fh' are variable of the MQTT client
def on_message(client, userdata, message):
    # Get the MQTT message as json string
#     print("message topic=",message.topic)
    json_string=str(message.payload.decode("utf-8"))
    json_data=json.loads(json_string)

    # split the json data key from the string
    firstLine=client.firstLine.split(', ')

    # Print the datas in the terminal
    if client.printLog:
        k=0
        while k<len(firstLine):
            print(f"{firstLine[k]} : {str(json_data[firstLine[k]])}")
            k+=1
        print("----------")

    # Save the datas in a log file 'fh'
    if client.saveLog:
        k=0
        while k<len(firstLine)-1:
            client.fh.write(f"{str(json_data[firstLine[k]])}, ")
            k+=1
        client.fh.write(str(json_data[firstLine[k]])+ "\n")
