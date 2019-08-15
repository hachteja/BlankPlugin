Blank Plugin
======
Blank Plugin is a Nion Swift plugin designed to straightforwardly convert existing python functions into a clickable button in the Nion Swift user interface. It also has easily replicated fields that can be used to enter in fields required for the python function. 

The plugins can be made much more complex than this, but probably not much more simple and easy to generate.

Usage Instructions (Nion Swift)
-------------------------------
1. Installation
	a. Download from `GitHub <https://github.com/hachteja/BlankPlugin>`
        b. Identify folder where Nion Swift looks for Plugins. For example, in a MAC environment when Swift is launched it will display a line of dialog that says 'Loading plug-ins from /Users/<your username here>/Documents/Nion/Swift/PlugIns'
        c. Move the entire BlankPlugin folder to this directory
	d. Swift will now automatically find and load the BlankPlugin

2. Test the Blank Plugin
        a. Open Nion Swift
        b. Go to Window Tab. Select "Blank Plugin", this should open the Blank Plugin UI.
    	c. Click the button that says 'Blank Plugin'. This should create a copy of whatever data_item is currently selected (blue border) and print whatever the field value is in the Swift dialog box.

3. Edit the Plugin
	a. Rename the plugins. Renaming takes place in several locations.
		i. Rename the BlankPlugin directory
		ii. Rename the BlankPlugin.py file
		iii. Open the __init__.py file and change the Filename to whatever you renamed the BlankPlugin.py file
		iv. In the BlankPlugin.py file, edit the field name to change what the Plugin display name will be
	b. Copy and paste the field section to create as many editable fields as you want, than rename each accordingly. (Labels optional but pretty straightforward)
	c. Replace the placeholder function with your desired function. Note: No editing of the function is needed, just copy and paste straight from your code/notebook
	d. Edit the lines in the Buttonclicked function to correctly input the data into your python function
	e. Part d can be potentially complicated if you are unfamiliar with the data structure of Swift. Swift uses data_items which is a larger class that stores the data, metdata, and calibrations separately. I have included a quick primer here on how access the most important ones. All of these assume that the data_item has been selected using the command 'data_item=document_window.target_data_item'
		i. The data: data_item.data (Simple but can be stored as an hdf5 or numpy array depending on which type of dataset you're using, watch out for type errors)
		ii. Dimensional calibrations: data_item.dimensional_calibrations (Has as many axes as your data set and has 'scale', 'offset' and 'units'. So to access the dispersion on an EELS dataset you'd use data_item.dimensional_calibrations[2].sclae)
		iii. Metadata fields: This one is not so obvious, its worth exploring using Swifts metadata plugin (a default that will already be installed in Swift). If you want to see the metadata open Swift, got to the Window tab, select "Metadata". This should open a new UI on the Swift side toolbars, click on the dataset you're interested in and the metadata will display there. This is all stored as a python dictionary so if you want to access say the dwell time in a HAADF image you would use data_item.metadata['hardware_source']['autostem']['pixel_time_us'].

4. Run your function. Now when Swift is launched whatever you renamed the plugin to should be available as an option in the Window tab. You should be able to open it, select any dataset in your library by dragging it into the active workspace and clicking it, and then executing your python function with the 

If You Found This Useful
------------------------
There is no paper assosciated with this so there's nothing to cite if you used it. I only ask that if you develop a fun and useful Plugin using this template, that you eventually upload it to GitHub or throw it in the supplemental materials of your paper so other people can benefit from it as well!
