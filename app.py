import sys

import numpy as np

from database.dbProcess import ForumDatabase
from strProcess import message_process
from dataProcess import data_process
from dataProcess import build_word_cloud
from dataProcess import get_text_from_clusters



def main(argv):
    database = ForumDatabase()
    messages = database.get_messages()
    messages = message_process(messages)
    y = data_process(messages)
    clusters_text = get_text_from_clusters(messages, y)
    build_word_cloud(clusters_text, "image")



if __name__ == "__main__":
    main(sys.argv)
