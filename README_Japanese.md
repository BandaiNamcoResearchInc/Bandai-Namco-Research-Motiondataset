# Bandai-Namco-Research-Motiondataset
このリポジトリでは、株式会社バンダイナムコ研究所が収集したモーションキャプチャのデータセットを公開しています。

ゲームや映画といったメディアはリアルで表現力豊かなキャラクターアニメーション表現を追求しており、多様なスタイルのモーションをAIで生成することに長年の関心があります。コンテンツ制作の規模が大きくなるにつれ、モーションキャプチャなどの方法を使用した収録で多様なモーションを揃えられなくなる将来が予想されます。近年注目を集めているのは、特定のコンテンツを含むクリップ内のモーションを、同じコンテンツを維持しながら別のスタイルの別のモーションに変換することを目的としたモーションスタイル転送（Motion Style Transfer 以下、MST）です。モーションはコンテンツとスタイルで構成され、コンテンツはモーションのベースであり、スタイルはモーションに関連付けられたキャラクターの気分や性格などの属性で構成されます。

データセットには、日常の動作、格闘、ダンスなど、さまざまなコンテンツが含まれています。アクティブ、疲れ、幸せなどはスタイルです。これらは、MSTモデルのトレーニングデータとして使用できます。以下のアニメーションは、可視化されたモーションの例を示しています。

現在、このリポジトリには2つのデータセットがあり、どちらもdatasetディレクトリの下にあります。

- **Bandai-Namco-Research-Motiondataset-1** ([Details](dataset/Bandai-Namco-Research-Motiondataset-1/README.md))
    - 17種の幅広いコンテント、日常動作、格闘、ダンスなど
    - 15種のスタイル.
    - 総計36,673フレーム.

<img src="src/Bandai-Namco-Research-Motiondataset-1/movie_walk.gif" width="100%">

- **Bandai-Namco-Research-Motiondataset-2** ([Details](dataset/Bandai-Namco-Research-Motiondataset-2/README.md))
    - 10種のコンテント、主にロコモーションや手の動きについてのもの
    - 7種のスタイル
    - 総計384,931フレーム.

<img src="src/Bandai-Namco-Research-Motiondataset-2/movie_walk.gif" width="100%">

utilsディレクトリの下に、可視化用のサンプルスクリプト（Blender用）があります。詳しくは[こちら](utils/blender/README.md)をご覧ください。

# Download
データのダウンロードはGitHubのDownload zipか下記のリンクよりダウンロードができます.

https://github.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset/archive/refs/heads/master.zip

## Data Collection
各データセットは、バンダイナムコ内のモーションキャプチャスタジオで収集された3人のプロのモーションアクターの動きに基づいています。ノイズ除去、プロポーションの整形、クリッピングなどの後処理を適用しました。データはBVH形式で提供されます。

<img src='src/images/motion_capture_studio.png' width="50%"/>

## Citation Information

このデータセットの技術的詳細は下記の論文に記載されています。

データセットを利用した際などの引用は下記の論文の引用を推奨します。

[Motion Capture Dataset for Practical Use of AI-based Motion Editing and Stylization](https://arxiv.org/abs/2306.08861)

```
@misc{kobayashi2023motion,
      title={Motion Capture Dataset for Practical Use of AI-based Motion Editing and Stylization}, 
      author={Makito Kobayashi and Chen-Chieh Liao and Keito Inoue and Sentaro Yojima and Masafumi Takahashi},
      year={2023},
      eprint={2306.08861},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## License
データセットとスクリプトは、次のlincenseで利用できます。

- Bandai-Namco-Research-Motiondataset-1: [CC BY-NC 4.0](dataset/Bandai-Namco-Research-Motiondataset-1/LICENSE)
- Bandai-Namco-Research-Motiondataset-2: [CC BY-NC 4.0](dataset/Bandai-Namco-Research-Motiondataset-2/LICENSE)
- Motion visualization on Blender: [MIT](utils/blender/LICENSE)

もしもこのデータセットの商用利用について希望があれば下記までお問い合わせください。

https://acesinc.co.jp/projects/project-1760

## Related works
前述のように、MSTの分野は最近注目を集めています。このトピックに興味がある場合は、以下の調査とデータセットの網羅的ではないリストを参照してください。これらの論文で紹介されたモデルは、高レベルのパフォーマンスを示しており、MSTに関連するデータセットはさまざまなモーションデータを提供します。

### Papers
- (Jurnal of Sensors 2021) A Cyclic Consistency Motion Style Transfer Method Combined with Kinematic Constraints [[Paper]](https://www.hindawi.com/journals/js/2021/5548614/)
- (CVPR 2021) Autoregressive Stylized Motion Synthesis with Generative Flow [[Paper]](https://openaccess.thecvf.com/content/CVPR2021/papers/Wen_Autoregressive_Stylized_Motion_Synthesis_With_Generative_Flow_CVPR_2021_paper.pdf)
- (CVPR 2021) Understanding Object Dynamics for Interactive Image-to-Video Synthesis [[Paper]](https://ieeexplore.ieee.org/document/9577842)
- (ACM Trans. Graph 2020) Unpaired Motion Style Transfer from Video to Animation [[Paper]](https://deepmotionediting.github.io/papers/Motion_Style_Transfer-camera-ready.pdf)

### Datasets
- Deep-motion-editing [[GitHub]](https://github.com/DeepMotionEditing/deep-motion-editing)
- Ubisoft La Forge Animation Dataset [[GitHub]](https://github.com/ubisoft/ubisoft-laforge-animation-dataset)


&copy;  [2022] Bandai Namco Research Inc. All Rights Reserved
