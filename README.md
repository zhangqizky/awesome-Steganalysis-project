## 隐写分析的意义
隐写分析是通过对载体的统计特性进行分析，判断载体中是否隐藏有额外的信息甚至估计信息嵌入量、获取隐藏信息内容的技术。其研究对于防止机密信息泄露、打击恐怖主义与犯罪活动、维护互联网安全等方面都具有十分重要的意义。目前的隐写分析研究领域通常将隐写分析看成一个二分类问题，目标是区分正常载体和含密载体。虽然人类感知器官无法进行区分，研究者可以借助机器学习、模式识别等工具，并通过对图像统计特性进行分析来实现有效判别。根据应用范围的不同，隐写分析可以分为两种类型：专用隐写分析(SpecificSteganalysis)和通用隐写分析(Universal Steganalysis)。专用隐写分析利用某种隐写术中存在的特定的缺陷或漏洞进行针对性的攻击，检测准确率较高。但其局限性在于只对特定的一种或一类隐写术有效。由于目前的隐写算法千变万化，且新的算法层出不穷，针对性的隐写分析方法很难满足实际应用需求。在这
种情况下，不针对特定隐写算法的通用隐写分析技术受到了更多的重视，并成为了目前隐写分析领域主流的研究方向。通用隐写分析的基本思想是利用隐写算法对载体图像统计特性造成的改变中存在的共性来进行检测，可以对多种隐写术进行攻击，更接近实际应用需求。

### 著名期刊
IEEE Transactions on Information Forensics and Security (TIFS), Information Hiding and Multimedia Security
(IH&MMSec), Media Watermarking, Security, and Forensic (MWSF), International Workshop on Information
Forensics and Security (WIFS), International Workshop on Digital Watermarking (IWDW)

## 基于传统特征的图像隐写分析方法
### 概述
传统的图像通用隐写分析方法一般包括特征提取和训练分类器两个步骤。其中，隐写分析中的特征是对正常图像和载密图像具有区分能力的统计量。而分类器则是机器学习中常用的 SVM、集成分类器(Ensemble Classifier) [1]等可训练优化的类别判别工具。两个步骤中，特征表达是研究中的关键问题，其对检测性能起到决定性的作用。在传统的方法中，特征表达主要依赖于人工设计，且特征设计的基本思想是找到隐写操作前后图像中具有明显差异的统计量
### 传统特征方法整理

## 基于深度学习的图像隐写分析方法
### 概述
虽然基于人工设计特征的通用隐写分析技术近些年取得发展较快，但仍面临诸多困难及挑战。首先，人工设计特征是一种非常费力、启发式的方法，有效特征的设计选取更多的依赖于人的经验，且需要花费大量的时间精力。其次，作为互相对抗的两种技术，在隐写分析发展的同时，隐写术也在不断地进步。新型的隐写术层出不穷，且新提出的隐写术往往可以保持图像中更复杂的统计特性，这也给隐写分析提出了越来越高的要求。为了进行有效的检测，隐写分析特征也需要考虑更复杂的统计特性，特征设计难度不断加大。

### 深度学习的方法整理
[2015年的Deep learning for steganalysis via convolutional neural networks](http://xueshu.baidu.com/s?wd=paperuri%3A%281c85f9edc52b10af1f6157d44667da57%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fadsabs.harvard.edu%2Fcgi-bin%2Fnph-data_query%3Fbibcode%3D2015SPIE.9409E..0JQ%26amp%3Bdb_key%3DPHY%26amp%3Blink_type%3DABSTRACT%26amp%3Bhigh%3D567107244204418&ie=utf-8&sc_us=10775830153732577606)。
### 目前研究重点和展望
近年来隐写分析得到了快速的发展，并不断有新的成果涌现。本文着重讨论了近几年图像通用隐写分析领域发展情况，包括传统基于人工特征的方法的新进展以及基于深度学习在隐写分析方法新思路。今后隐写分析的进一步发展可以从以下几个方面考虑：
1) 特征表达仍将是隐写分析中的研究重点。基于深度学习的方法的提出开辟了隐写分领域的新范式，也将是接下来的研究重心所在。但目前基于深度学习的隐写分析研究仍是在初步阶段，仍有很多问题需要进一步的考虑与解决。首先，目前的基于深度学习的隐写分析框架中仍需要人工设计的高通滤波核进行图像预处理，未来是否能不需要依赖人工预处理，实现端到端学习是一个值得继续研究的问题；其次，目前基于深度学习的隐写分析模型的检测性能仍没有完全超过目前最好的基于人工设计特征的方
法，有待进一步提高；最后，目前提出的针对隐写分析的深度学习模型相对较简单，未来能否结合迁移学习，增强学习，对抗生成网络等深度学习领域内的研究热点提出更适合隐写分析的模型也值得关注。
2) 目前的通用隐写分析技术仍需要用到隐写算法、嵌入量等先验信息，例如在构建分类器时仍需要与待检测隐写术对应的载密图像进行训练，并不能真正做到“盲”检测。考虑到新的隐写算法层出不穷，因此研究独立于隐写术的通用隐写分析十分重要。
3) 面向实际应用的隐写分析，特别是社交网络平台大数据环境下的隐写分析研究是一个很值得关注的问题。目前的隐写分析研究大多局限在特定的小规模数据库等实验室条件下。而实际应用环境下隐写分析面临的则是社交网络背景下大数据、异质图像源等复杂的图像数据，实验室条件下取得成功的方法往往很难成功的进行实际应用。目前面向实际应用的隐写分析研究较少，但需求迫切，尚待进一步的研究。
4) 目前的隐写分析研究目标主要停留在检测隐写存在性这一层次上，而更高层次的定位隐写嵌入位置、提取出隐写信息等目标目前仍没有有效的方法，其也是今后隐写分析需要努力的方向。
### 一些开源项目和工具
1. [一个Steganaysis的python工具包](https://github.com/cedricbonhomme/Stegano)
2. [A steganalysis tool for detecting LSB steganography in images ](https://github.com/b3dk7/StegExpose)
3. [Least Significant Bit Steganography for bitmap images (.bmp and .png), WAV sound files, and byte sequences. Simple LSB Steganalysis (LSB extraction) for bitmap images.](https://github.com/ragibson/Steganography)
4. [Image steganalysis using state-of-the-art machine learning techniques](https://github.com/daniellerch/aletheia)
5. [caffe_deep_learning_for_steganalysis](https://github.com/GuanshuoXu/caffe_deep_learning_for_steganalysis)
6. [code of our paper entitled: Improving Blind Steganalysis in Spatial Domain using a Criterion to Choose the AppropriateSteganalyzer between CNN and SRM+EC ](https://github.com/rcouturier/steganalysis_with_CNN_and_SRM)
7. [Audio and image steganalysis with tensorflow1.3 or later](https://github.com/Charleswyt/tf_audio_steganalysis)
8. [Tensorflow implementation of "Deep Learning Hierarchical Representation for Image Steganalysis" ](https://github.com/Caenorst/YeNet-Tensorflow)
9. [Machine learning steganographic image detection. ](https://github.com/rokkuran/stegasawus)
10. [steganalysis_with_CNN_for_same_key_images](https://github.com/rcouturier/steganalysis_with_CNN_for_same_key_images)
11. [some code for deep steganalysis](https://github.com/jiangszzzzz/CAECNNcode)
12. [Steganalysis of JPEG images with CUDA optimizations ](https://github.com/id23cat/cujpgstego)
