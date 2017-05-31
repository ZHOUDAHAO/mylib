import public,sys

src_file = sys.argv[1];
dest_file = sys.argv[2];
src_encoding = sys.argv[3]
dest_encoding = sys.argv[4]
public.change_all_encoding(src_file,dest_file,src_encoding,dest_encoding)
