from flask import jsonify
from pymongo import mongo_client, MongoClient
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


class Language:
    def __init__(self, name, add, delete, edit):
        self.__id = id
        self.__name = name
        self.__add = add
        self.__delete = delete
        self.__edit = edit

    def make_dic(self):
        return {"name": self.__name, "add": self.__add, "delete": self.__delete, "edit": self.__edit}

    def show_all(self):
        pass

    def set_name(self, desired_name):
        self.__name = desired_name
        return "Name has been changed"

    def get_name(self):
        return self.__name

    def set_add(self, desired_change):
        self.__add = desired_change
        return "Name has been changed"

    def set_edit(self, desired_change):
        self.__add = desired_change
        return "Edit has been changed"

    def set_delete(self, desired_change):
        self.__delete = desired_change
        return "Delete has been changed"


a = Language("English", "Add", "Delete", "Edit")
b = Language("Turkce", "Ekle", "Sil", "Duzenle")
c = Language("Spanish", "asdasd", "sadasd", "sadasd")

