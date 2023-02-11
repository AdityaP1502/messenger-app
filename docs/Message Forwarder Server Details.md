
Message Forwarder Server is a server that will forward any message to the recipient. 

# Connecting to the server
To connect to the server, the client first initiate a TCP connection via socket to the server. After that, the client must establish a secure connection to the server via RSA. After that, the TCP connection is established. 

To use the service, a server must register it's username to it's socket IP address, via check-in. After the check-in is succesful, the user can send any message or call to any user that are currently active

# Sending a message
A user can send a message to other user. First the user send a **SENDMESSAGE** request to the server. If the request is valid, the server will forward the packet to the recipient if the recipient is active.  If the user isn't active, then the message will be saved in the database. 

# Receiving a message
If a recipient is active, the server won't save the message in the database. It will directly sent to the recipient after a sender sent the message, without any request sent from the recipient. (No MailBox is used). 

If a recipient is offline, the message will be saved in the database (encrypted) with its key that are encrypted via RSA. After the recipient online, the recipient must check the mailbox. Then the message in the mailbox will be cleared. 

# Call
## User Initialize a Call
When a user want to call another user, first the client must send an **INITIATECALL** packet to the server. The server will send a **INCOMINGCALL** response to the user if the user isn't on a call. If a user is on a call then server will send a **CALLABORT** response.  

## Receiver Accept/Decline the Call
In the receiver side,  after the receiver get the message the receiver can accept and declined the call request. If the user accept the request, then a **ACCEPTCALL** request must be sent to the server. If the user declined, then **DECLINEDCALL** need to be sent. 

## Timeout in the Receiver Side
the receiver must implement timeout handler that will terminate the call if the user didn't accept or decline the answer. If a timeout is reached, the client must send a **TIMEOUTCALL** to the server. 

## Accepted Call
If a user accepted the call, then user must send the voice data in bytes using the **SENDMESSAGE** request. When any user end the call, the user that end the call must send a **CALLTERMINATE** request to the server.

## Unexpected Abort
If at the middle of a call a user suddenly disconnect, a **CALLABORT** response will be thrown by the server to the other user in the call.  This include the condition where user is waiting for the response of the recipient. 

# Status Report Response
After each request the user sent to the server, a response will be sent by the server. If a response is succuesful, then the client will received an **OK** response. Else, an **ERROR** Response will be sent with the error type and message. 

# Packet Format
Each data that sent to the socket, by definition, will be in bytes. The encoding that the server used will be **UTF-8**. 

Every packet will have a header and a payload. A header always include the request type/response type and the UID that were assign by the sender (Only used by the sender). The format of the packet used key-value pair called **Field**. The key is called **entryName** and its value called **value**. The key-value is seperated by a `=` and each field is seperated by `;`. 

The payload content of the request is placed in the payload field. Here is the format of the packet:

```
UID=[sender_assigned_number];reqtype=[Supported Request];payload=[all fields that are neccesary for the request]
```

## Request Format
This the format that is used by the client to send a request to the server. If the client sent a request with invalid format, an error will be sent by the server.  

### CHECKIN
The request type of check in request is  CHECKIN. The payload is username that registered to the socket IP. 

```
UID=[];reqtype=CHECKIN;payload=username[]
```

### SENDMESSAGE
The request type of sendmessage request is **SENDMESSAGE**.  The payload in **SENDMESSAGE** is
**sdr**, **rcpt**, and, **message**. **sdr**(sender) contains the sender username that are registered to the socket IP, **rcpt** is the username of the recipient, and **message** is the message that will be sent to the recipient. Here is the format of SENDMESSAGE request

```
UID=[];reqtype=SENDMESSAGE;payload=sdr=[sender username];rcpt=[recipient username];message=[message]
```

### INITIATECALL
The request type of INITIATECALL request is INITIATECALL. The payload of INITIATECALL is **sdr**
and **rcpt**.  **sdr**(sender) contains the sender username that are registered to the socket IP, **rcpt** is the username of the recipient. Here is the format of INITIATECALL request:

```
UID=[];reqtype=INITIATECALL;payload=sdr=[sender username];rcpt=[recipient username];message=[message]
```

### ACCEPTCALL

The request type of acceptcall request is  ACCEPTCALL.  The payload for all call request packet is the same. 

```
UID=[];reqtype=ACCEPTCALL;payload=sdr=[sender username];rcpt=[recipient username]
```

### DECLINEDCALL
The request type of acceptcall request is  ACCEPTCALL. 
```
UID=[];reqtype=DECLINEDCALL;payload=sdr=[sender username];rcpt=[recipient username]
```

### TIMEOUTCALL
The request type of acceptcall request is  TIMEOUTCALL. 
```
UID=[];reqtype=TIMEOUTCALL;payload=sdr=[sender username];rcpt=[recipient username]
```

### TERMINATECALL
The request type of acceptcall request is  TERMINATECALL 
```
UID=[];reqtype=TERMINATECALL;payload=sdr=[sender username];rcpt=[recipient username]
```

### TERMINATE
The request type of terminate connection request is  TERMINATE. The payload is username that registered to the socket IP. 

```
UID=[];reqtype=TERMINATE;payload=username[]
```


