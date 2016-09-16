#WARNING: program once
#encodign : utf-8
import os
raw_dir = 'raw_data/'
pure_dir = 'data/'
files = os.listdir(raw_dir)

for afile in files:
	if afile[0] == '.' || afile=='readme.md':
		continue
	in_file = open(raw_dir+afile, encoding='gb18030')
	out_file = open(pure_dir+afile, 'w', encoding='utf-8')
	while True:
		line = in_file.readline()
		if not line:
			break
		out_file.write(line)
	in_file.close()
	out_file.close()