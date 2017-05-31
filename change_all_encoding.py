import public,sys

path = sys.argv[1]
encoding1 = sys.argv[2]
encoding2 = sys.argv[3]
public.change_all_encoding(path,encoding1,encoding2)
