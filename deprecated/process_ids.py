with open('myos/myos_ids.seq', 'r') as handle:
# with open('siphos/siphos_ids.seq', 'r') as handle:
    s = []
    for line in handle:
        s.append(line.strip())
    s1 = s[0:400]
    # s2 = s[400:800]
    s2 = s[400:]

    print len(s1) + len(s2)
    print ','.join(s1)
    print '*****'
    print ','.join(s2)
    # print '*****'
    # print ','.join(s3)
