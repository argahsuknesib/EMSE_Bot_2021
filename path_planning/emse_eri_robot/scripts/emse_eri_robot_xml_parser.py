#! /usr/bin/env python

import xml.sax
import csv

title_list = []
values_list = []

file = open('/home/whiskygrandee/catkin_ws/src/emse_bot/log/configuration_space/14x14_space.csv', 'w')
writer = csv.writer(file)

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "model":
            global title_list
            title = attrs["name"]
            title_list.append(title)
            map( lambda s : s  if s.find(" ") == -1 else "'" + s + "'", title_list)
            # print(title_list[-1])
            print('{}'.format(title))
            # writer.writerow(title_data_value)
            # writer.writerow(title_list)

    def characters(self, content):
        if self.current == "pose":
            self.name = content

    def endElement(self, name):
        if self.current == "pose":
            global values_list
            values_list.append(self.name)
            data_values = values_list[-1]
            print("{}".format(self.name))
            # writer.writerow(values_list)

print(title_list)

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/home/whiskygrandee/catkin_ws/src/emse_bot/path_planning/emse_eri_robot/worlds/emse_eri_robot_base.world')


