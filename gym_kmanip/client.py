import zmq
import asyncio


async def client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    # Replace <host_ip> with the host machine's IP address
    socket.connect("tcp://127.0.0.1:5555")
    # Alternatively, you can use the host machine's hostname if it resolves correctly
    # socket.connect("tcp://<host_hostname>:5555")

    task_description = {
        "task_id": 1,
        "task_name": "Do something",
        "task_details": "Details of the task",
    }
    await socket.send_json(task_description)
    response = await socket.recv_json()
    print("Response:", response)


if __name__ == "__main__":
    asyncio.run(client())
