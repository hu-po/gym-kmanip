import zmq
import asyncio


async def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://0.0.0.0:5555")  # Bind to all available interfaces
    print("Server started")

    while True:
        message = await socket.recv_json()
        print("Received task description:", message)
        # Process the task description
        response = {"success": True, "message": "Task received successfully"}
        await socket.send_json(response)


if __name__ == "__main__":
    asyncio.run(server())
