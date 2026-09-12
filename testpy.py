import os
import shutil

storage = input ("Type a folder path: ")

if os.path.exists(storage):
  print("Moving....")
  print ("All folders & files:", os.listdir())
else:
    print ("No such folder path. ngekkk")

os.mkdir("Image")
os.mkdir("Documents")
os.mkdir("Videos")
os.mkdir("Others")















