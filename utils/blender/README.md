# Motion visualization on Blender
![Blender](https://img.shields.io/badge/Blender-%3E=2.93.6-Orange?logo=blender)

This directory provides Python scripts to visualize motions in BVH format.

## Usage
### 1. Install blender
First, download the Blender application [here
](https://www.blender.org/download/).

<img src='../../src/images/Usage_1.png' width="70%"/>

After launching the Blender app, click `Scripting` to open the Python console.

<img src='../../src/images/Usage_1_1.png' width="70%"/>

### 2. Run
Please note that the provided script only works with python on blender.

#### 2.1 Copy scripts
Click `New` to create new Python script. 

<img src='../../src/images/Usage_2_1_1.png' width="70%"/>

Next, copy the provided script to the console.

<img src='../../src/images/Usage_2_1_2.png' width="70%"/>

#### 2.2 Modify path
Open the script and modify `input_path` to specify the data to be rendered, and `output_path` to specify the save location of the rendered data.

<img src='../../src/images/Usage_2_2.png' width="70%"/>

#### 2.3 Run
Click play button to run the script (see the figure above).

#### 2.4 Check outputs
Rendered data can be found in the `output_path` specified previously.


You may find more details of the Python API for Blender in [here](https://docs.blender.org/api/current/info_quickstart.html).

&copy;  [2022] Bandai Namco Research Inc. All Rights Reserved