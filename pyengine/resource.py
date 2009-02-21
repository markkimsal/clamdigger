import os

def fullPath(relative, basePath=None):
	dirs = os.path.split(relative)
	fullpath = ''

	for x in dirs:
		fullpath = os.path.join(fullpath, x)

	if basePath is not None:
		return os.path.join(basePath, fullpath)
	else:

		return os.path.join(
				os.path.dirname(os.path.abspath(__file__)), '..',
				fullpath)

