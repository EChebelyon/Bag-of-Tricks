import glob

files = [f for f in glob.glob("path/to/folders" + "*.csv", recursive=True)]