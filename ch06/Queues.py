def write_to_scrol(inst, num_loop=10):
    print('hi from Queue', inst)
    for idx in range(num_loop):
        inst.gui_queue.put('Message from a queue: ' + str(idx))
    inst.create_thread(6)
