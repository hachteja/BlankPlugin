# standard libraries
import gettext
import logging
import numpy as np
import scipy
import threading

# third party libraries
from nion.data import Calibration
from nion.data import DataAndMetadata
from nion.data import xdata_1_0 as xd

_ = gettext.gettext

########################################
### Enter PlugIn Name Between Quotes ###
########################################

NAME="Blank Plugin"

###################################
### Header Stuff (DO NOT TOUCH) ###
###################################

class Extension(object):
    extension_id = NAME

    def __init__(self, api_broker):
        api = api_broker.get_api(version="1", ui_version="1")
        self.__panel_ref = api.create_panel(Delegate(api))
        print('Running!')

    def close(self):
        print('Closed!')
        self.__panel_ref.close()
        self.__panel_ref = None

class Delegate(object):
    def __init__(self,api):  
        self.api = api
        self.panel_id = NAME
        self.panel_name = _(NAME)
        self.panel_positions = ["left", "right"]
        self.panel_position = "right"

######################
### Create UI Here ###
######################

    def create_panel_widget(self, ui, document_window):

################################
### Different Options for UI ###
################################

        ### Create Editable Variable
        ### Two items created
        ### 1. self.field - (value) Internal value stored in class that can be used for calcuations
        ### 2. FIELD - (UI Field) Editable field displayed in swift that can be used to set the internal self.field
        self.field=0.    
        Field=ui.create_line_edit_widget()
        Field.text=self.field
        def FieldEdited(val):
            self.field=val
            Field.text=self.field
        Field.on_editing_finished = FieldEdited
        
        ### Create Function Execute Button
        ### One item created
        ### 1. Buttton - (UI Field) A clickable button that will execute any function defined in this UI  
        Button = ui.create_push_button_widget(NAME)
        def Buttonclicked():
            data_item=document_window.target_data_item  ### This selects whatever data_item was clicked last, do not edit ###
            dataout=Function(data_item.data,self.field)
            self.api.library.create_data_item_from_data(dataout)
        Button.on_clicked = Buttonclicked

        ### Create Label for UI
        ### One item created
        ### 1. Label - (UI Field) A text label that can be inserted next to any UI Field
        Label = ui.create_label_widget('Label: ')
        
        ### Create Menu
        ### Two items created
        ### 1. Menu - (UI Field) A column of UI fields that will be the displayed UI upon launching swift
        ### 2. Row - (UI Field) A row of two UI fields that will be added as a single entry in the column
        Menu = ui.create_column_widget()
        Row = ui.create_row_widget()
        Row.add(Label)
        Row.add(Field)
        Menu.add(Row)
        Menu.add(Button)
        return Menu

##########################
### Add Functions Here ###
##########################

def Function(data,field):
    ### A test function which just returns an exact copy of the input data and prints the field in the Swift Output Dialog
    print(field)
    return data
