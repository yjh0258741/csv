#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import csv


class CsvUtil:
    csvFile: None
    fileName: None

    def open(self, fileName):
        self.fileName = fileName;
        self.csvFile = open(fileName, "r+", newline="", encoding='utf-8')

    def read(self):
        content = self.csvFile.readline()
        if content == "":
            print("已经读到尽头")
        else:
            print(content, end="")

    def readAll(self):
        read = csv.reader(self.csvFile)
        for i in read:
            print(i)

    def write(self, content):
        position = self.csvFile.tell();
        self.csvFile.seek(0, 2);
        write = csv.writer(self.csvFile)
        write.writerow(content)
        self.csvFile.seek(position, 0)

    def writeAll(self, *args):
        position = self.csvFile.tell();
        self.csvFile.seek(0, 2);
        write = csv.writer(self.csvFile)
        write.writerows(args)
        self.csvFile.seek(position, 0)

    def close(self):
        self.csvFile.close();

    def read_header(self):
        self.csvFile.seek(0, 0)
        print(self.csvFile.readline(), end="")

    def row_generator(self):
        read = csv.reader(self.csvFile)
        return iter(read)
