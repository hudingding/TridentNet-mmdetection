# TridentNet-mmdetection
TridentNet in mmdetection

支持Backbobe为ResNet和ResNeXt中所有检测网络，主要用于解决尺度不变性

config参数修改，如下：

backbone=dict(
    type='TridentResNext', #TridentResNext 表示在ResNeXt基础上修改的， TridentResNet 表示在 ResNet基础上修改的
    depth=101,
    groups=64,
    base_width=4,
    num_stages=4,
    out_indices=(0, 1, 2, 3),
    frozen_stages=-1,
    style='pytorch',
    test_branch_idx=1,  # 推理时使用（0，1，2），0表示感受野最小的分支，2表示感受野最大的分支，1表示中间感受野的分支
    dcn=dict(
        modulated=False,
        groups=64,
        deformable_groups=1,
        fallback_on_stride=False),
    stage_with_dcn=(False, True, True, True)),

测试结果
在不增加运算量和参数量的前提下，相比于Bockbone为ResNet和ResNeXt网络，有一定的性能提升，具体视训练数据，以下比较的是采用自有的业务数据，Tesla P100卡，多尺度训练，单尺度测试

|                    |     AP50     | Inf time (fps) |
|--------------------|:------------:|:--------------:|
| ResNeXt101         |    0.766     |       7.1      |
| TridentResNext101  |    0.776     |       7.1      |