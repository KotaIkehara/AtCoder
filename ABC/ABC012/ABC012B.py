N = int(input())

print("%02d:%02d:%02d" % (N//(60*60), (N % (60*60))//60, (N % 60)))
