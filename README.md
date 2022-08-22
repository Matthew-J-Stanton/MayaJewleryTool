# Jewellery Tool

The jewellery is a Maya plugin that allows the user to create procedural jewellery. Currently the only piece of jewellery available for creation is a jhumka.  

## Necessary additional Items:
- Houdini Engine Plugin for Maya
- Maya (Preferably 2020)
- Python 

## Installation

To install the plugin into Maya, download the jewlery tool directory, go into the terminal and enter the jewlery tool directory and run the installModule.py file using

```bash
./installModule.py
```
This should add the tool as a plugin within Maya.

This install file runs using Python so make sure this is installed on your device.

## Usage

To use the device within Maya, first make sure the MastersProject.py plugin is loaded into Maya. It is recommended to set the plugin to auto-load so that the jewellery shelf always has a link to the plugin.
Activating the plugin should create a new shelf within Maya called the jewellery shelf with a button called jewellery tool, pressing this launches the tool.

**_Warning:_**  If the jewellery tool shelf button does not work make sure that the plugin MastersProject.py is loaded as the shelf will still load even without the plugin being loaded.


This tool allows you to create and manage pieces of jewellery using the main window. When a new piece of jewellery is created or a old controls opened a controls tab will appear on the right this allows you to set parameters and, with the use of a create button, create pieces of jewellery.

**_Warning:_**  Make sure the attribute editor window is open when creating a new piece of jewllery otherwise the controls will not be initialised properly.