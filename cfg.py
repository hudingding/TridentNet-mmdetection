# model settings
model = dict(
    type='FasterRCNN',
    pretrained='../basenet_weight/Pytorch/resnext101_64x4d-ee2c6f71.pth',
    #pretrained='open-mmlab://resnext101_64x4d',
    backbone=dict(
        type='TridentResNext',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=-1,
        style='pytorch',
        test_branch_idx=1,
        dcn=dict(
            modulated=False,
            groups=64,
            deformable_groups=1,
            fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True)),
#......
