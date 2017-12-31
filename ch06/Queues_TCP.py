from socket import socket, SOCK_STREAM, AF_INET


def write_to_scrol(inst, num_loop=10):
    print('hi from Queue', inst)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 24000))
    for idx in range(num_loop):
        # inst.gui_queue.put('Message from a queue: ' + str(idx))
        sock.send((f'Message from a queue: {idx}').encode())
        recv = sock.recv(8192).decode()
        inst.gui_queue.put(recv)
    inst.create_thread(6)
