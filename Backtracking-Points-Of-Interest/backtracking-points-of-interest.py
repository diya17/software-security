# Getting log files using sysdig 
# To get tcp, udp events - sudo sysdig -p "%evt.num %evt.rawtime.s.%evt.rawtime.ns %evt.cpu %proc.name (%proc.pid) %evt.dir %evt.type cwd=%proc.cwd %evt.args latency=%evt.latency exepath=%proc.exepath proc_pid =%proc.pid file_id=%fd.num  fd_name=%fd.name  fd_cip=%fd.cip fd_sip=%fd.sip fd_lip=%fd.lip fd_rip=%fd.rip fd_cport=%fd.cport fd_sport=%fd.sport fd_lport=%fd.lport fd_rport=%fd.rport fd_l4protocol= %fd.l4proto " "proc.name!=tmux and (evt.type=read or evt.type=readv or evt.type=write or evt.type=writev or evt.type=fcntl or evt.type=accept or evt.type=execve or evt.type=clone or evt.type=pipe or evt.type=rename or evt.type=sendmsg or evt.type=recvmsg)" and proc.name!=sysdig > sysdig_28_11_2022_3_4_1.txt
# To get file access events - sudo sysdig -p "%evt.num %evt.rawtime.s.%evt.rawtime.ns %evt.cpu %proc.name (%proc.pid) %evt.dir %evt.type cwd=%proc.cwd %evt.args latency=%evt.latency exepath=%proc.exepath proc_pid =%proc.pid file_id=%fd.num  fd_name=%fd.name  fd_filename=%fd.filename" "proc.name!=tmux and (evt.type=read or evt.type=readv or evt.type=write or evt.type=writev or evt.type=fcntl or evt.type=accept or evt.type=execve or evt.type=clone or evt.type=pipe or evt.type=rename or evt.type=sendmsg or evt.type=recvmsg)" and proc.name!=sysdig > sysdig_28_11_2022_3_4_2.txt
def parse_sysdig_events(filePath):
    logsList = []
    parsedLogTuples = []
    with open(filePath) as logsFile:
        for line in logsFile:
            logsList.append(line)
    for log in logsList:
        processName = log.split()[3]
        pID = log.split('proc_pid =', 1)[1].split()[0]
        processType = log.split()[6]
        fileID = log.split('file_id=', 1)[1].split()[0]
        eventType = log.split()[5]
        fdCIP, fdSIP, fdCPort, fdSPort, fdL4Protocol, fdFileName, parsedLogTuple = None, None, None, None, None, None, None
        if 'fd_cip' in log:
            fdCIP = log.split('fd_cip=', 1)[1].split()[0]
            fdSIP = log.split('fd_sip=', 1)[1].split()[0]
            fdCPort = log.split('fd_cport=', 1)[1].split()[0][1:]
            fdSPort = log.split('fd_sport=', 1)[1].split()[0][1:]
            fdL4Protocol = log.split('fd_l4protocol= ', 1)[1].split()[0]
        else:
            fdFileName = log.split('fd_filename=', 1)[1].split()[0]
        # Tuple structure:
        # for tcp/udp connections - ((processID, processName), (processType, eventType(flow of information)), (fileID, file client IP, file server IP, file client port, file server port, file access protocol))
        # for normal file access - ((processID, processName), (processType, eventType(flow of information)), (fileID, fileName))
        if fdCIP and fdSIP and fdCPort and fdSPort and fdL4Protocol:
            parsedLogTuple = ((pID, processName), (processType, eventType), (fileID, fdCIP, fdSIP, fdCPort, fdSPort, fdL4Protocol))
        else:
            parsedLogTuple = ((pID, processName), (processType, eventType), (fileID, fdFileName))
        parsedLogTuples.append(parsedLogTuple)
    print(parsedLogTuples)
    return parsedLogTuples

parsedLogTuples = parse_sysdig_events('/Users/diyabiju/Downloads/sysdig_28_11_2022_3_4_1.txt')

