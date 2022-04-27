# Bandai-Namco-Research-Motiondataset-1

Find [here](README_Japanese.md) for a READEME in Japanese.

Bandai-Namco-Research-Motiondataset-1 is collected by Bandai Namco Research Inc. Compared with Bandai-Namco-Research-Motiondataset-2, this dataset contains fewer data, but has a wide variety of contents, as well as expression variety per style.

## Dataset
The dataset contains motion in BVH format with annotations in JSON format within `data.zip`. The motion is visualized in MP4 format in `videos.zip`. The annotations contain the ID of the content, and the style of the motion within the filename and corresponding labels can be found in `content_label.txt` and `style_label.txt` under the `cfg/` directory.

The data is named in correspondence to the following: `dataset-1_{MOTION}_{STYLE}_{ID}`  
For instance: `dataset-1_raise-up-both-hands_active`



### Basic Info
|Basic Info||
|--|--|
|Number of Data|175|
|Number of frame|36,673|
|Number of styles|15|
|Number of contents|20|
|Frame Rate|30|

### Contents
- walk
- run
- dash
- walk-back
- walk-right
- walk-left
- bow
- bye
- guide
- byebye
- respond
- call
- kick
- slash
- dance

Please note that `call`, `dance-long`, `dance-short`, `kick`, `punch` and `slash` have only normal motion. 

### Styles
- normal
- happy
- sad
- angry
- proud
- not-confident
- masculinity
- feminine
- children
- old
- tired
- active
- musical
- giant
- chimpira


## Visualization
The visualizations of the main motions are shown below. All combinations can be found in `videos.zip`.

### walk
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_walk.gif" width="100%">

### run
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_run.gif" width="100%">

### dash
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_dash.gif" width="100%">

### walk-back
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_walk-back.gif" width="100%">

### walk-left
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_walk-left.gif" width="100%">

### walk-right
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_walk-right.gif" width="100%">

### bow
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_bow.gif" width="100%">

### bye
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_bye.gif" width="100%">

### guide
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_guide.gif" width="100%">

### byebye
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_byebye.gif" width="100%">

### respond
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_respond.gif" width="20%">

### call
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_call.gif" width="20%">

### punch
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_punch.gif" width="20%">

### kick
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_kick.gif" width="20%">

### slash
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_slash.gif" width="20%">

### dance-long
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_dance-long.gif" width="20%">

### dance-short
<img src="../../src/Bandai-Namco-Research-Motiondataset-1/movie_dance-short.gif" width="20%">

&copy;  [2022] Bandai Namco Research Inc. All Rights Reserved
